from pytessng.DLLs.Tessng import PyCustomerSimulator, tessngIFace, Online
from pytessng.ToolInterface import SimuExportTrajectoryActor
from pytessng.ToolInterface import SimuImportTrajectoryActor


class MySimulator(PyCustomerSimulator):
    def __init__(self):
        super().__init__()
        self.iface = tessngIFace()
        self.netiface = self.iface.netInterface()
        self.simuiface = self.iface.simuInterface()

        # 轨迹数据导入者
        self.import_traj_actor = SimuImportTrajectoryActor(self.netiface, self.simuiface, Online)
        # 轨迹数据导出者
        self.export_traj_actor = SimuExportTrajectoryActor(self.netiface, self.simuiface)

    # 每次仿真前
    def beforeStart(self, ref_keepOn):
        self.import_traj_actor.ready()
        self.export_traj_actor.ready()

    # 每帧仿真后
    def afterOneStep(self):
        # 创建车辆
        self.import_traj_actor.operate()
        # 发送轨迹数据
        self.export_traj_actor.operate()

    # 每次仿真后
    def afterStop(self):
        self.export_traj_actor.finish()
        self.import_traj_actor.finish()
