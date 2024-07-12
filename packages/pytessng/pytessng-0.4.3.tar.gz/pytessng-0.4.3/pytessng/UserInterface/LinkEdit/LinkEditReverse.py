from PySide2.QtWidgets import QGraphicsRectItem, QGraphicsPathItem, QMessageBox
from PySide2.QtCore import QRectF, Qt
from PySide2.QtGui import QColor, QPainterPath, QPen

from ..BaseUI import BaseClass
from pytessng.GlobalVar import GlobalVar
from pytessng.ToolInterface import MyOperation


class LinkEditReverse(BaseClass):
    name: str = "框选反转路段"
    mode: str = "reverse"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 按钮
        self.action = GlobalVar.action_network_edit_reverse

        # 获取画布
        self.netiface = self.iface.netInterface()
        self.scene = self.netiface.graphicsScene()
        # 关联按钮
        self.guiiface = self.iface.guiInterface()
        self.guiiface.actionNullGMapTool().trigger()
        # 把其他关联上
        custom_actions = [GlobalVar.action_network_edit_split, GlobalVar.action_network_edit_remove, GlobalVar.action_file_export_grid]
        for actions in [self.guiiface.netToolBar().actions(), self.guiiface.operToolBar().actions(), custom_actions]:
            for action in actions:
                if action.text() == "取消工具":
                    continue
                action.triggered.connect(self.after_stop)

        # 坐标
        self.pos1 = None
        self.pos2 = None
        # 透明框
        self.transparent_box_item = None
        # 高亮路段
        self.highlighted_line_items = []

    # 重写抽象父类BaseUserInterface的方法
    def load(self):
        # 开启
        if self.action.isChecked():
            self.action.setChecked(True)
            GlobalVar.is_need_select_network_edit_reverse = True
            # 回调函数
            GlobalVar.function_network_edit_reverse = self.apply_reverse_link
        # 关闭
        else:
            self.action.setChecked(False)
            GlobalVar.is_need_select_network_edit_reverse = False

    # 关闭
    def after_stop(self):
        self.action.setChecked(False)
        GlobalVar.is_need_select_network_edit_reverse = False

    def apply_reverse_link(self, event, mode: int = 1):
        # 按下左键
        if mode == 1 and event.button() == Qt.LeftButton:
            self.pos1 = self.netiface.graphicsView().mapToScene(event.pos())

        # 弹起左键
        elif mode == 2 and event.button() == Qt.LeftButton:
            self.pos2 = self.netiface.graphicsView().mapToScene(event.pos())

            # 执行删除
            params = {
                "p1": self.pos1,
                "p2": self.pos2,
                "confirm_function": self.show_confirm_dialog,
                "highlight_function": self.highlighted_links,
            }
            MyOperation.apply_edit_link(self, params)

            # 还原
            self.pos1 = None
            if self.transparent_box_item is not None:
                self.scene.removeItem(self.transparent_box_item)
            for item in self.highlighted_line_items:
                self.scene.removeItem(item)

        # 移动
        else:
            if self.pos1 is None:
                return

            # 清除上一个
            if self.transparent_box_item is not None:
                self.scene.removeItem(self.transparent_box_item)

            # 计算位置和长宽
            p1 = self.pos1
            p2 = self.netiface.graphicsView().mapToScene(event.pos())
            x1, x2 = sorted([p1.x(), p2.x()])
            y1, y2 = sorted([p1.y(), p2.y()])
            width = x2 - x1
            height = y2 - y1

            # 创建透明方框item
            rect = QRectF(x1, y1, width, height)
            self.transparent_box_item = QGraphicsRectItem(rect)
            self.transparent_box_item.setPen(QColor(0, 255, 0))  # 设置边框颜色
            self.transparent_box_item.setBrush(QColor(0, 255, 0, 50))  # 设置填充颜色和透明度

            # 添加item到scene
            self.scene.addItem(self.transparent_box_item)

    # 显示确认删除对话框，作为参数
    def show_confirm_dialog(self, link_count: int, mode: int):
        text = "全部" if mode == 1 else "部分"
        messages = {
            "title": "反转框选路段",
            "content": f"有{link_count}条路段被{text}选中，是否反转",
            "yes": "反转",
        }
        confirm = self.utils.show_confirm_dialog(messages)
        return confirm == QMessageBox.Yes

    # 高亮路段
    def highlighted_links(self, links):
        for link in links:
            for points in [link.centerBreakPoints(), link.leftBreakPoints(), link.rightBreakPoints()]:
                # 创建一个 QPainterPath 并将点添加到路径中
                path = QPainterPath()
                path.moveTo(points[0])
                for point in points[1:]:
                    path.lineTo(point)
                # 创建一个 QGraphicsPathItem 并设置路径
                path_item = QGraphicsPathItem(path)

                # 创建一个 QPen 并设置宽度和颜色
                pen = QPen(QColor(255, 255, 0))
                pen.setWidth(1)
                # 将 QPen 设置到路径项上
                path_item.setPen(pen)

                # 将路径项添加到场景中
                self.scene.addItem(path_item)
                self.highlighted_line_items.append(path_item)
