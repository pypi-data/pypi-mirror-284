from PySide2.QtGui import QVector3D

from pytessng.DLLs.Tessng import PyCustomerNet, tessngIFace
from pytessng.GlobalVar import GlobalVar


class MyNet(PyCustomerNet):
    def __init__(self):
        super().__init__()
        self.iface = tessngIFace()
        self.netiface = self.iface.netInterface()

    # 加载路网后
    def afterLoadNet(self):
        # =============== 能执行这里说明是正版key就开启相关功能 ===============
        # 路段编辑-打断路段
        if GlobalVar.action_network_edit_split is not None:
            GlobalVar.action_network_edit_split.setEnabled(True)
        # 路段编辑-删除路段
        GlobalVar.action_network_edit_remove.setEnabled(True)
        # 路段编辑-逆序路段
        GlobalVar.action_network_edit_reverse.setEnabled(True)
        # 仿真数据导入-导入轨迹数据
        GlobalVar.action_simu_import_trajectory.setEnabled(True)
        # 仿真数据导出-导出轨迹数据
        GlobalVar.action_simu_export_trajectory.setEnabled(True)
        # 配置文件导出-导出选区数据
        if GlobalVar.action_file_export_grid is not None:
            GlobalVar.action_file_export_grid.setEnabled(True)

        # =============== 打印属性信息 ===============

        attrs = self.netiface.netAttrs().otherAttrs()
        print("=" * 66)
        print("Load network! Network attrs:")
        if attrs:
            for k, v in attrs.items():
                print(f"\t{k:<15}:{' '*5}{v}")
        else:
            print("\t(EMPTY)")
        print("=" * 66, "\n")

    # 控制曲率最小距离
    def ref_curvatureMinDist(self, itemType: int, itemId: int, ref_minDist):
        ref_minDist.value = 0.1
        return True

    # 鼠标点击后触发
    def afterViewMousePressEvent(self, event):
        # 路段编辑-打断路段
        if GlobalVar.is_need_select_network_edit_split:
            GlobalVar.function_network_edit_split(event)
        # 路段编辑-删除路段
        if GlobalVar.is_need_select_network_edit_remove:
            GlobalVar.function_network_edit_remove(event, 1)
        # 路段编辑-逆序路段
        if GlobalVar.is_need_select_network_edit_reverse:
            GlobalVar.function_network_edit_reverse(event, 1)
        # 配置文件导出-导出选区数据
        if GlobalVar.is_need_select_file_export_grid:
            GlobalVar.function_file_export_grid(event)

    # 鼠标释放后触发
    def afterViewMouseReleaseEvent(self, event):
        # 路段编辑-删除路段
        if GlobalVar.is_need_select_network_edit_remove:
            GlobalVar.function_network_edit_remove(event, 2)
        # 路段编辑-逆序路段
        if GlobalVar.is_need_select_network_edit_reverse:
            GlobalVar.function_network_edit_reverse(event, 2)

    # 鼠标移动后触发
    def afterViewMouseMoveEvent(self, event) -> None:
        # 路段编辑-删除路段
        if GlobalVar.is_need_select_network_edit_remove:
            GlobalVar.function_network_edit_remove(event, 3)
        # 路段编辑-逆序路段
        if GlobalVar.is_need_select_network_edit_reverse:
            GlobalVar.function_network_edit_reverse(event, 3)

    # # 拖拽路段后触发
    # def afterLinkVertexMove(self, link, index: int, pressPoint, releasePoint):
    #     points = link.centerBreakPoint3Ds()
    #     points[index] = QVector3D(releasePoint.x(), releasePoint.y(), points[index].z())
    #     self.netiface.updateLink3DWithPoints(link, points)
