from typing import Callable
from PySide2.QtWidgets import QAction


class GlobalVar:
    # ========== MyNet.py ==========
    # 按钮：打断路段
    action_network_edit_split: QAction = None
    # 是否需要选择
    is_need_select_network_edit_split: bool = False
    # 回调函数：定位路段
    function_network_edit_split: Callable = None

    # 按钮：删除路段
    action_network_edit_remove: QAction = None
    # 是否需要选择
    is_need_select_network_edit_remove: bool = False
    # 回调函数：
    function_network_edit_remove: Callable = None

    # 按钮：逆序路段
    action_network_edit_reverse: QAction = None
    # 是否需要选择
    is_need_select_network_edit_reverse: bool = False
    # 回调函数：
    function_network_edit_reverse: Callable = None

    # 按钮：导出轨迹数据
    action_simu_export_trajectory: QAction = None
    # 按钮：导入轨迹数据
    action_simu_import_trajectory: QAction = None

    # 按钮：导出选区数据
    action_file_export_grid: QAction = None
    # 是否需要选择
    is_need_select_file_export_grid: bool = False
    # 回调函数
    function_file_export_grid: Callable = None

    # ========== MySimulator.py ==========
    # 车辆轨迹读取JSON文件路径
    simu_import_traj_file_path: str = ""
    # 车辆轨迹的投影
    simu_import_traj_proj_string: str = ""

    # 车辆轨迹的投影
    simu_export_traj_proj_string: str = ""
    # 车辆轨迹保存为JSON文件路径
    simu_export_traj_config_json: str = ""
    # 车辆轨迹上传至kafka的配置
    simu_export_traj_config_kafka: dict = dict()
