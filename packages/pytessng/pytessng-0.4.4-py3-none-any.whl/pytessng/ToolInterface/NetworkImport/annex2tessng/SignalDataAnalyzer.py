from ...BaseTool import BaseTool
from ...public.Line.LineBase import LineBase
from pytessng.Config import NetworkImportConfig
from pytessng.Logger import logger
from pytessng.ProgressDialog import ProgressDialogClass as pgd


class SignalDataAnalyzer(BaseTool):
    valid_duration = NetworkImportConfig.VALID_DURATION

    # 解析信号配时数据
    def analyse_signal_data(self, original_signal_groups_data: dict, original_signal_heads_data: dict) -> (list, list):
        # 获取处理过待行区的信号灯组数据
        signal_groups_data = self.get_signal_groups_data(original_signal_groups_data)

        # 获取路网数据，包括进口道与面域ID的映射关系，各面域的各方向的各转向
        link2area_data, areas_data = self.get_areas_data()

        # 获取面域与信号灯组的映射关系
        area2signal_data = self.get_area2signal_data(original_signal_heads_data, link2area_data)

        # 获取信号灯头数据
        signal_heads_data = self.get_signal_heads_data(area2signal_data, areas_data, signal_groups_data)

        # 获取用于创建信号灯组和信号灯头的标准数据
        signal_groups_data, signal_heads_data = self.get_standard_signal_data(signal_groups_data, signal_heads_data)

        return signal_groups_data, signal_heads_data

    def get_areas_data(self) -> (dict, dict):
        # 各面域的上游路段ID集合
        area2link_data = dict()
        for connector_area in self.netiface.allConnectorArea():
            all_connector = connector_area.allConnector()
            # 只有少数连接段的面域视为路段中间
            if len(all_connector) > 2:
                area2link_data[connector_area.id()] = set()
                for connector in connector_area.allConnector():
                    from_link = connector.fromLink()
                    area2link_data[connector_area.id()].add(from_link.id())

        # 进口道路段ID对应的面域
        link2area_data = {
            link_id: connector_area_id
            for connector_area_id, link_id_list in area2link_data.items()
            for link_id in link_id_list
        }

        # 确定每个面域的进口道方向，和进口道的流向
        areas_data = {}
        for connector_area_id, from_link_list in area2link_data.items():
            direction_record = {"东": {}, "南": {}, "西": {}, "北": {}}
            for link_id in from_link_list:
                link = self.netiface.findLink(link_id)
                for to_connector in link.toConnectors():
                    for lane_connector in to_connector.laneConnectors():
                        from_lane = lane_connector.fromLane()
                        to_lane = lane_connector.toLane()
                        from_lane_id = from_lane.id()
                        to_lane_id = to_lane.id()
                        from_lane_points = self._qtpoint2list(from_lane.centerBreakPoint3Ds())
                        to_lane_points = self._qtpoint2list(to_lane.centerBreakPoint3Ds())

                        start_angle = LineBase.calculate_angle_with_y_axis(from_lane_points[0], from_lane_points[1])
                        end_angle = LineBase.calculate_angle_with_y_axis(to_lane_points[0], to_lane_points[1])
                        # 角度差 -180~180
                        angle_diff = (end_angle - start_angle + 180) % 360 - 180

                        # 进口道方向
                        start_angle -= 180
                        if -45 <= start_angle <= 45:
                            direction = "南"
                        elif 45 <= start_angle <= 135:
                            direction = "西"
                        elif -135 <= start_angle <= -45:
                            direction = "东"
                        else:
                            direction = "北"

                        # 转向
                        if -45 <= angle_diff <= 45:
                            turn_type = "直"
                        elif -135 <= angle_diff <= -45:
                            turn_type = "左"
                        elif 45 <= angle_diff <= 135:
                            turn_type = "右"
                        else:
                            turn_type = "左"

                        if from_lane_id not in direction_record[direction]:
                            direction_record[direction][from_lane_id] = {}
                        if turn_type not in direction_record[direction][from_lane_id]:
                            direction_record[direction][from_lane_id][turn_type] = []
                        direction_record[direction][from_lane_id][turn_type].append(to_lane_id)

            areas_data[connector_area_id] = direction_record

        return link2area_data, areas_data

    def get_area2signal_data(self, original_signal_heads_data: dict, link2area_data: dict) -> dict:
        area2signal_data = {}
        for signal_head in original_signal_heads_data:
            link_id_list: list = signal_head["roadId"]
            signal_group_id: int = signal_head["signalGroupId"]
            area_id_set = set([link2area_data[link_id] for link_id in link_id_list])

            if len(area_id_set) != 1:
                logger.logger_pytessng.warning("The roadId can not match to a unique intersection!")
                continue

            area_id = area_id_set.pop()
            area2signal_data[area_id] = signal_group_id

        return area2signal_data

    def get_signal_groups_data(self, original_signal_groups_data: dict) -> dict:
        def _handle_phase(colors, durations):
            if len(colors) == 3:
                if colors == ["绿", "黄", "红"]:
                    colors = ["红"] + colors
                    durations = [0] + durations
                elif colors == ["红", "绿", "黄"]:
                    colors = colors + ["红"]
                    durations = durations + [0]
                else:
                    raise Exception("No support!")
            elif len(colors) == 4:
                assert colors == ["红", "绿", "黄", "红"]
            else:
                raise Exception("No support!")
            return colors, durations

        def _handle_phases(phases, signal_group_id):
            # 处理相位灯色和持续时间
            for phase in phases:
                colors = phase["colors"]
                durations = phase["durations"]
                phase["colors"], phase["durations"] = _handle_phase(colors, durations)

            # 按第一个灯色（红）时长排序
            phases = sorted(phases, key=lambda x: x["durations"][0])
            # 新相位列表
            waiting_phases = []

            # 根据是否有待行区创建新相位
            for i, phase in enumerate(phases[1:], start=1):
                direction = phase["direction"]
                waiting_area = phase.get("waitingArea", False)
                # 如果有待行区
                if waiting_area:
                    # 找上一个不一样的相位 TODO: 第一个就找不到
                    last_phase = None
                    j = i - 1
                    while j >= 0:
                        if phases[j]["durations"] == phase["durations"]:
                            j -= 1
                        else:
                            last_phase = phases[j]
                            break
                    if last_phase is not None:
                        duration0 = last_phase["durations"][0]
                        duration1 = phase["durations"][0] + phase["durations"][1] - duration0
                        duration2 = phase["durations"][2]
                        duration3 = phase["durations"][3]
                        # 添加新相位
                        new_phase = {
                            "id": "0",
                            "colors": ["红", "绿", "黄", "红"],
                            "durations": [duration0, duration1, duration2, duration3],
                            "direction": f"{direction}-待行"
                        }
                        waiting_phases.append(new_phase)

            # 按第一个灯色（红）时长排序
            waiting_phases = sorted(waiting_phases, key=lambda x: x["durations"][0])

            # 处理相位的ID
            phase_id = 1
            for phase in phases + waiting_phases:
                phase["id"] = f"{signal_group_id}-{phase_id}"
                phase_id += 1

            phases_dict = {phase["direction"]: phase for phase in phases}
            waiting_phases_dict = {phase["direction"]: phase for phase in waiting_phases}

            return phases_dict, waiting_phases_dict

        signal_groups_data = {}
        for signal_group in original_signal_groups_data:
            signal_group_id = signal_group["id"]
            cycle_time = signal_group["cycleTime"]
            phases, waiting_phases = _handle_phases(signal_group["phases"], signal_group_id)
            signal_groups_data[signal_group_id] = {
                "cycle_time": cycle_time,
                "phases": phases,
                "waiting_phases": waiting_phases,
            }

        return signal_groups_data

    def get_signal_heads_data(self, area2signal_data: dict, areas_data: dict, signal_groups_data: dict) -> list:
        signal_heads_data = []

        for area_id, signal_group_id in area2signal_data.items():
            area_data = areas_data[area_id]
            signal_group_data = signal_groups_data[signal_group_id]
            phases, waiting_phases = signal_group_data["phases"], signal_group_data["waiting_phases"]

            for direction0, direction_record in area_data.items():
                for from_lane_id, turn_record in direction_record.items():
                    # 单个车道包含的转向
                    turn_type_list = sorted(turn_record.keys())
                    if len(turn_type_list) > 1 and "右" in turn_type_list and f"{direction0}右" not in phases:
                        in_connector = True
                        turn_type_list.remove("右")
                    else:
                        in_connector = False

                    # 一个车道只能有一个信号灯头，就选择第一个
                    turn_type, to_lane_id_list = turn_type_list[0], turn_record[turn_type_list[0]]
                    # 构建方向
                    direction = f"{direction0}{turn_type}"
                    # 如果需要设置信号灯
                    if direction in phases:
                        # 需要设置待行相位
                        if waiting_phases and f"{direction}-待行" in waiting_phases:
                            this_phase_id = waiting_phases[f"{direction}-待行"]["id"]
                            waiting_phase_id = phases[direction]["id"]
                        else:
                            this_phase_id = phases[direction]["id"]
                            waiting_phase_id = None

                        lane_id = str(from_lane_id)
                        # 遍历to_lane
                        for to_lane_id in to_lane_id_list:
                            # 不是在连接段
                            if not in_connector:
                                dist = -1
                                to_lane_id_ = "0"
                            # 是在连接段
                            else:
                                dist = 0.1
                                to_lane_id_ = str(to_lane_id)

                            signal_head_data = {
                                "phase_id": this_phase_id,
                                "dist": dist,
                                "lane_id": lane_id,
                                "to_lane_id": to_lane_id_,
                            }
                            signal_heads_data.append(signal_head_data)

                            # 待行相位
                            if waiting_phase_id is not None:
                                # 一定在连接段上
                                lane_connector = self.netiface.findLaneConnector(from_lane_id, to_lane_id)
                                dist = min([8, 0.5 * self._p2m(lane_connector.length())])
                                to_lane_id_ = str(to_lane_id)

                                signal_head_data = {
                                    "phase_id": waiting_phase_id,
                                    "dist": dist,
                                    "lane_id": lane_id,
                                    "to_lane_id": to_lane_id_,
                                }
                                signal_heads_data.append(signal_head_data)

        return signal_heads_data

    def get_standard_signal_data(self, signal_groups_data: dict, signal_heads_data) -> (list, list):
        standard_signal_groups_data = []
        for signal_group_id, signal_group_data in signal_groups_data.items():
            phases = list(signal_group_data["phases"].values()) + list(signal_group_data["waiting_phases"].values())
            standard_signal_group_data = {
                "id": signal_group_id,
                "cycle_time": signal_group_data["cycle_time"],
                "phases": phases,
                "duration": self.valid_duration
            }
            # 去除多余字段
            for phase in standard_signal_group_data["phases"]:
                if "direction" in phase:
                    phase.pop("direction")
                if "waitingArea" in phase:
                    phase.pop("waitingArea")
            standard_signal_groups_data.append(standard_signal_group_data)

        standard_signal_heads_data = []
        signal_head_id = 1
        for signal_head_data in signal_heads_data:
            # 加上ID字段
            signal_head_data["id"] = str(signal_head_id)
            signal_head_id += 1
            standard_signal_heads_data.append(signal_head_data)

        return standard_signal_groups_data, standard_signal_heads_data
