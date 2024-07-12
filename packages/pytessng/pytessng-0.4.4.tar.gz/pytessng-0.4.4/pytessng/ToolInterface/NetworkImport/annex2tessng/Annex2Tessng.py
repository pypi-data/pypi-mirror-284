import json

from ..BaseOther2Tessng import BaseOther2Tessng
from .AnnexNetworkAnalyser import AnnexNetworkAnalyser
from ...public.NetworkCreator import NetworkCreator


class Annex2Tessng(BaseOther2Tessng):
    """
    params:
        - file_path: json
    """

    data_source = "Annex"
    pgd_index_create_network = (3, 4)

    def read_data(self, params: dict) -> dict:
        file_path = params["file_path"]
        annex_data = json.load(open(file_path, encoding="utf-8"))
        return annex_data

    def analyze_data(self, annex_data: dict, params: dict) -> dict:
        # 解析数据
        network_analyser = AnnexNetworkAnalyser(self.netiface)
        analysed_data = network_analyser.analyse_all_data(annex_data)
        return analysed_data

    # 重写父类方法
    def create_network(self, analyzed_network_data: dict) -> dict:
        # 实例化路网创建者
        network_creator = NetworkCreator(
            self.netiface,
            pgd_index=self.pgd_index_create_network
        )
        # 创建路网
        network_creator.create_network(analyzed_network_data, update_scene_size=False)

        return {
            "status": True,
            "message": "创建成功",
        }
