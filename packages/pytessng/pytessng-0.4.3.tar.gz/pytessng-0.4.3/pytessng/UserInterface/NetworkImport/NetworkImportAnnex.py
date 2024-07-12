import os
from functools import partial
from PySide2.QtWidgets import QLineEdit, QPushButton

from .BaseNetworkImport import BaseNetworkImport, MyQHBoxLayout, MyQVBoxLayout


class NetworkImportAnnex(BaseNetworkImport):
    name: str = "导入路网附属元素"
    mode: str = "annex"
    format: list = [("Json", "json")]
    is_network: bool = False

    def set_widget_layout(self) -> None:
        # 第一行：文本框和按钮
        self.line_edit = QLineEdit()
        self.line_edit.setFixedWidth(500)
        self.button_select = QPushButton('文件选择')
        # 第二行：按钮
        self.button_import = QPushButton('生成路网元素')

        # 总体布局
        layout = MyQVBoxLayout([
            MyQHBoxLayout([self.line_edit, self.button_select]),
            self.button_import
        ])
        self.setLayout(layout)

    def set_monitor_connect(self) -> None:
        self.line_edit.textChanged.connect(self.apply_monitor_state)

    def set_button_connect(self) -> None:
        self.button_select.clicked.connect(partial(self.select_file, self.line_edit))
        self.button_import.clicked.connect(self.apply_button_action)

    def apply_monitor_state(self) -> None:
        file_path = self.line_edit.text()
        is_file = os.path.isfile(file_path)

        # 设置可用状态
        enabled = all([is_file])
        self.button_import.setEnabled(enabled)

    # 重写父类方法
    def get_params(self) -> dict:
        # 获取文件路径
        file_path = self.line_edit.text()

        return {
            "file_path": file_path,
        }
