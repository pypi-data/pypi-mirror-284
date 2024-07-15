import math
from microservice_metrics import MicroserviceMetricsManager


class FitnessFunctions:
    def __init__(self, metrics_manager):
        self.metrics_manager = metrics_manager

    def f1(self) -> float:
        cpt, _, wsict, cxt, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + cxt ** 2 + wsict ** 2 + (100 - sst) ** 2) / 2

    def f2(self) -> float:
        cpt, _, wsict, _, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + wsict ** 2 + (100 - sst) ** 2) / 2

    def f3(self) -> float:
        _, _, _, cxt, sst = self._get_metrics()
        return math.sqrt(cxt ** 2 + (100 - sst) ** 2) / 2

    def f4(self) -> float:
        cpt, coht, _, _, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + coht ** 2 + (100 - sst) ** 2) / 2

    def f5(self) -> float:
        cpt, _, _, _, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + (100 - sst) ** 2) / 2

    def f6(self) -> float:
        cpt, coht, wsict, _, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + coht ** 2 + wsict ** 2 + (100 - sst) ** 2) / 2

    def f7(self) -> float:
        cpt, _, _, cxt, sst = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + cxt ** 2 + (100 - sst) ** 2) / 2

    def f8(self) -> float:
        cpt, coht, wsict, _, _ = self._get_metrics()
        return math.sqrt((10 * cpt) ** 2 + coht ** 2 + wsict ** 2) / 2

    def _get_metrics(self):
        cpt = self.metrics_manager.calculate_coupling_total()
        coht = self.metrics_manager.calculate_coh_total()
        wsict = self.metrics_manager.calculate_wsic_total()
        cxt = self.metrics_manager.calculate_cognitive_complexity()
        sst = self.metrics_manager.calculate_total_semantic_similarity()
        return cpt, coht, wsict, cxt, sst
