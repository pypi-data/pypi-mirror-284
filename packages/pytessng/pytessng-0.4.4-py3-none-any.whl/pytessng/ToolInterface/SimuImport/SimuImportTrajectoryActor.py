import pandas as pd
from pyproj import Proj
from PySide2.QtCore import QPointF, QCoreApplication

from pytessng.GlobalVar import GlobalVar
from pytessng.Logger import logger


class SimuImportTrajectoryActor:
    def __init__(self, netiface, simuiface, Online):
        # TESSNG接口
        self.netiface = netiface
        self.simuiface = simuiface
        self.online = Online

        # 比例尺
        self.p2m = None  # function
        self.m2p = None  # function
        # 投影
        self.proj = None  # function
        # move
        self.move = None  # dict

        # 轨迹数据路径
        self.traj_file_path: str = ""
        # 运行状态
        self.is_running: bool = False
        # 车辆数据
        self.vehicles_data = None

    def ready(self):
        # 轨迹文件路径
        traj_file_path = GlobalVar.simu_import_traj_file_path
        if not traj_file_path:
            return

        # 比例尺
        scene_scale = self.netiface.sceneScale()
        self.p2m = lambda x: x * scene_scale
        self.m2p = lambda x: x / scene_scale
        # 投影关系
        traj_proj_string = GlobalVar.simu_import_traj_proj_string
        if traj_proj_string:
            self.proj = Proj(traj_proj_string)
        else:
            self.proj = lambda x, y: (x, y)
        # move
        move = self.netiface.netAttrs().otherAttrs().get("move_distance")
        if move is None or "tmerc" in traj_proj_string:
            self.move = {"x_move": 0, "y_move": 0}
        else:
            self.move = {"x_move": -move["x_move"], "y_move": -move["y_move"]}

        # 解析车辆数据
        # 网格化
        self.netiface.buildNetGrid(5)
        # 读取数据
        vehicles_data = pd.read_csv(traj_file_path)
        # 使时间戳从0开始
        vehicles_data["timestamp"] -= vehicles_data["timestamp"].min()
        # 获取车辆创建信息
        self.vehicles_data = vehicles_data.groupby("objId").apply(self.df_operation)
        # 释放内存
        vehicles_data = None

        # 更改运行状态
        self.is_running = True

    def operate(self):
        if self.is_running:
            # 当前仿真时间
            simu_time = self.simuiface.simuTimeIntervalWithAcceMutiples()  # ms
            # 当前需要创建的车辆
            current_vehicles = self.vehicles_data[self.vehicles_data["create_time"] <= simu_time]
            # 创建车辆
            for vehicle_id, vehicle_series in current_vehicles.iterrows():
                self.create_vehicle(vehicle_series, vehicle_id)
            # 删去当前创建的车辆
            self.vehicles_data = self.vehicles_data[self.vehicles_data["create_time"] > simu_time]

    def finish(self):
        self.traj_file_path: str = ""
        self.p2m = None  # function
        self.m2p = None  # function
        self.proj = None  # function
        self.move = None  # dict
        self.is_running: bool = False

    # 创建车辆
    def create_vehicle(self, vehicle_series: pd.Series, vehicle_id: str):
        try:
            dvp = self.online.DynaVehiParam()
            dvp.name = f"{vehicle_id}"
            dvp.vehiTypeCode = vehicle_series.type_code
            dvp.roadId = vehicle_series.road_id
            dvp.dist = vehicle_series.dist
            dvp.laneNumber = vehicle_series.lane_number
            if vehicle_series.to_lane_number is not None:
                dvp.toLaneNumber = vehicle_series.to_lane_number
            vehicle = self.simuiface.createGVehicle(dvp)
            # 设置路径
            if vehicle is not None:
                route_link_id_list = vehicle_series.route_link_id_list
                routing = self.create_vehicle_routing(route_link_id_list)
                if routing is not None:
                    vehicle.vehicleDriving().setRouting(routing)
                    print(vehicle.vehicleDriving().isOnRouting(), vehicle.name())
        except:
            vehicle = None
        return vehicle

    # 创建车辆路径
    def create_vehicle_routing(self, link_id_list: list):
        try:
            links = [self.netiface.findLink(link_id) for link_id in link_id_list]
            routing = self.netiface.createRouting(links)
        except:
            routing = None
        return routing

    # 对DataFrame的每个group做的操作
    def df_operation(self, vehi_traj_data: pd.DataFrame):
        # 立刻更新界面
        QCoreApplication.processEvents()
        first_row = vehi_traj_data.iloc[0]
        # 获取经纬度
        lon0, lat0 = first_row["longitude"], first_row["latitude"]
        # 获取平面坐标
        x0, y0 = self.proj(lon0, lat0)
        # 定位
        locations = self.netiface.locateOnCrid(QPointF(self.m2p(x0), -self.m2p(y0)), 9)
        if not locations:
            return pd.Series()

        location = locations[0]
        dist = location.distToStart
        lane_object = location.pLaneObject
        # 路段
        if lane_object.isLane():
            lane = location.pLaneObject.castToLane()
            link = lane.link()
            road_id = link.id()
            lane_number = lane.number()
            to_lane_number = None
        # 连接段
        else:
            lane_connector = location.pLaneObject.castToLaneConnector()
            connector = lane_connector.connector()
            road_id = connector.id()
            lane_number = lane_connector.fromLane().number()
            to_lane_number = lane_connector.toLane().number()

        create_time = int(first_row["timestamp"])  # ms
        type_code = int(first_row["typeCode"])
        if "roadId" in vehi_traj_data.columns:
            route_link_id_list = vehi_traj_data["roadId"].drop_duplicates().tolist()
        else:
            route_link_id_list = []
            for lon, lat in zip(vehi_traj_data["longitude"], vehi_traj_data["latitude"]):
                x, y = self.proj(lon, lat)
                locations = self.netiface.locateOnCrid(QPointF(self.m2p(x), -self.m2p(y)), 9)
                if locations:
                    location = locations[0]
                    lane_object = location.pLaneObject
                    if lane_object.isLane():
                        lane = location.pLaneObject.castToLane()
                        link_id = lane.link().id()
                        if not route_link_id_list or (route_link_id_list and route_link_id_list[-1] != link_id):
                            route_link_id_list.append(link_id)

        series = pd.Series(
            [create_time, type_code, road_id, dist, lane_number, to_lane_number, route_link_id_list],
            index=["create_time", "type_code", "road_id", "dist", "lane_number", "to_lane_number", "route_link_id_list"],
        )

        return series
