from ..BaseNetworkAnalyser import BaseNetworkAnalyser
from .SignalDataAnalyzer import SignalDataAnalyzer
from pytessng.ProgressDialog import ProgressDialogClass as pgd


class AnnexNetworkAnalyser(BaseNetworkAnalyser):
    def __init__(self, netiface):
        super().__init__()
        self.netiface = netiface

    def analyse_all_data(self, annex_data: dict, params: dict = None) -> dict:
        analysed_data = {}

        # 解析信号配时数据
        original_signalGroups_data = annex_data.get("signalGroups")
        original_signalHeads_data = annex_data.get("signalHeads")
        if original_signalGroups_data is not None and original_signalHeads_data is not None:
            signalGroups_data, signalHeads_data = SignalDataAnalyzer(self.netiface).analyse_signal_data(original_signalGroups_data, original_signalHeads_data)
            analysed_data["signalGroups"] = signalGroups_data
            analysed_data["signalHeads"] = signalHeads_data

        return analysed_data
