import math
from typing import Dict, List, Tuple, Set
from microservice_story_manager import MicroserviceManager
from microservice_story_manager import SemanticSimilarityCalculator


class MicroserviceMetricsManager:
    def __init__(self, microservice_manager: MicroserviceManager):
        self.microservice_manager = microservice_manager
        self.semantic_calculator = SemanticSimilarityCalculator(microservice_manager.user_story_manager)

    def _initialize_semantic_similarity(self):
        stories = []
        print("Initializing Semantic Similarity:")
        for ms_id, ms in self.microservice_manager.microservices.items():
            print(f"Processing Microservice {ms_id}")
            for story_id in ms.stories:
                story = self.microservice_manager.user_story_manager.get_story(story_id)
                if story.identifier:
                    stories.append((story.identifier, story.title, story.description))
                    print(f"  Added story: {story.identifier}")
                else:
                    print(f"  Skipped story with None identifier: {story.title}")

        print(f"Total stories collected: {len(stories)}")
        self.semantic_calculator.build_similarity_dict(stories)
        print("Finished building similarity dictionary")

    def calculate_ais_metric(self) -> Dict[str, int]:
        ais_metrics = {ms_id: 0 for ms_id in self.microservice_manager.microservices}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            dependent_microservices = set()
            for other_ms_id, other_ms in self.microservice_manager.microservices.items():
                if other_ms_id != ms_id:
                    other_stories = self.microservice_manager.get_microservice_stories(other_ms_id)
                    for story in other_stories:
                        if any(dep in microservice.stories for dep in story.dependencies):
                            dependent_microservices.add(other_ms_id)
                            break
            ais_metrics[ms_id] = len(dependent_microservices)
        return ais_metrics

    def calculate_ads_metric(self) -> Dict[str, int]:
        ads_metrics = {ms_id: 0 for ms_id in self.microservice_manager.microservices}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            dependent_on_microservices = set()
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            for story in stories:
                for dep in story.dependencies:
                    for other_ms_id, other_ms in self.microservice_manager.microservices.items():
                        if other_ms_id != ms_id and dep in other_ms.stories:
                            dependent_on_microservices.add(other_ms_id)
            ads_metrics[ms_id] = len(dependent_on_microservices)
        return ads_metrics

    def calculate_siy_metric(self) -> Dict[str, int]:
        """
        Calculate the Microservice Interdependence (SIY) metric for each microservice.
        SIY is the number of other microservices that are interdependent with a given microservice.
        """
        siy_metrics = {ms_id: 0 for ms_id in self.microservice_manager.microservices}
        ais_metrics = self.calculate_ais_metric()
        ads_metrics = self.calculate_ads_metric()

        for ms_id in self.microservice_manager.microservices:
            interdependent_count = 0
            for other_ms_id in self.microservice_manager.microservices:
                if ms_id != other_ms_id:
                    if ais_metrics[ms_id] > 0 and ads_metrics[other_ms_id] > 0 and \
                            ais_metrics[other_ms_id] > 0 and ads_metrics[ms_id] > 0:
                        interdependent_count += 1
            siy_metrics[ms_id] = interdependent_count

        return siy_metrics

    def calculate_ais_total(self) -> float:
        """
        Calculate the total AIS value at the system level (AisT).
        """
        ais_values = list(self.calculate_ais_metric().values())
        return math.sqrt(sum(ais ** 2 for ais in ais_values))

    def calculate_ads_total(self) -> float:
        """
        Calculate the total ADS value at the system level (AdsT).
        """
        ads_values = list(self.calculate_ads_metric().values())
        return math.sqrt(sum(ads ** 2 for ads in ads_values))

    def calculate_siy_total(self) -> float:
        """
        Calculate the total SIY value at the system level (SiyT).
        """
        siy_values = list(self.calculate_siy_metric().values())
        return math.sqrt(sum(siy ** 2 for siy in siy_values))

    def get_ais_vector(self) -> List[int]:
        """
        Get the AIS vector containing the AIS value for each microservice.
        """
        ais_metrics = self.calculate_ais_metric()
        return [ais_metrics[ms_id] for ms_id in sorted(ais_metrics.keys())]

    def get_ads_vector(self) -> List[int]:
        """
        Get the ADS vector containing the ADS value for each microservice.
        """
        ads_metrics = self.calculate_ads_metric()
        return [ads_metrics[ms_id] for ms_id in sorted(ads_metrics.keys())]

    def get_siy_vector(self) -> List[int]:
        """
        Get the SIY vector containing the SIY value for each microservice.
        """
        siy_metrics = self.calculate_siy_metric()
        return [siy_metrics[ms_id] for ms_id in sorted(siy_metrics.keys())]

    def calculate_coupling_total(self) -> float:
        ais_total, ads_total, siy_total = self.get_coupling_indicators()
        cpt = 10 * math.sqrt(ais_total ** 2 + ads_total ** 2 + siy_total ** 2)
        return cpt

    def get_coupling_indicators(self) -> tuple[float, float, float]:
        ais_total = self.calculate_ais_total()
        ads_total = self.calculate_ads_total()
        siy_total = self.calculate_siy_total()

        return ais_total, ads_total, siy_total

    def calculate_lc_metric(self) -> Dict[str, int]:
        """
        Calculate the Lack of Cohesion (LC) metric for each microservice.
        LC is the number of pairs of microservices not having any interdependency with the given microservice.
        """
        lc_metrics = {}
        total_microservices = len(self.microservice_manager.microservices)

        for ms_id in self.microservice_manager.microservices:
            dependent_microservices = set()
            for other_ms_id, other_ms in self.microservice_manager.microservices.items():
                if ms_id != other_ms_id:
                    if self._has_interdependency(ms_id, other_ms_id):
                        dependent_microservices.add(other_ms_id)

            lc_metrics[ms_id] = total_microservices - 1 - len(dependent_microservices)

        return lc_metrics

    def _has_interdependency(self, ms_id1: str, ms_id2: str) -> bool:
        """
        Check if there's an interdependency between two microservices.
        """
        ms1_stories = self.microservice_manager.get_microservice_stories(ms_id1)
        ms2_stories = self.microservice_manager.get_microservice_stories(ms_id2)

        for story in ms1_stories:
            if any(dep in self.microservice_manager.microservices[ms_id2].stories for dep in story.dependencies):
                return True

        for story in ms2_stories:
            if any(dep in self.microservice_manager.microservices[ms_id1].stories for dep in story.dependencies):
                return True

        return False

    def calculate_coh_metric(self) -> Dict[str, float]:
        """
        Calculate the Lack of Cohesion Grade (Coh) metric for each microservice.
        Coh is the proportion of LC divided by the total number of microservices.
        """
        lc_metrics = self.calculate_lc_metric()
        total_microservices = len(self.microservice_manager.microservices)

        coh_metrics = {ms_id: lc / total_microservices for ms_id, lc in lc_metrics.items()}
        return coh_metrics

    def calculate_coh_total(self) -> float:
        """
        Calculate the total Coh value at the system level (CohT).
        """
        coh_values = list(self.calculate_coh_metric().values())
        return math.sqrt(sum(coh ** 2 for coh in coh_values))

    def get_coh_vector(self) -> List[float]:
        """
        Get the Coh vector containing the Coh value for each microservice.
        """
        coh_metrics = self.calculate_coh_metric()
        return [coh_metrics[ms_id] for ms_id in sorted(coh_metrics.keys())]

    def get_cohesion_metrics(self) -> Tuple[Dict[str, int], Dict[str, float], float]:
        """
        Get all cohesion metrics: LC, Coh, and CohT.
        """
        lc_metrics = self.calculate_lc_metric()
        coh_metrics = self.calculate_coh_metric()
        coh_total = self.calculate_coh_total()

        return lc_metrics, coh_metrics, coh_total

    def calculate_number_of_microservices(self) -> int:
        """
        Calculate the Number of Microservices (N) in the system.
        """
        return len(self.microservice_manager.microservices)

    def calculate_wsic_metric(self) -> Dict[str, int]:
        """
        Calculate the Weighted Service Interface Count (WSIC) for each microservice.
        WSIC is the number of user stories assigned to each microservice.
        """
        wsic_metrics = {}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            wsic_metrics[ms_id] = len(microservice.stories)
        return wsic_metrics

    def calculate_wsic_total(self) -> int:
        """
        Calculate the total WSIC value at the system level (WsicT).
        WsicT is the maximum number of user stories associated with any microservice.
        """
        wsic_values = self.calculate_wsic_metric().values()
        return max(wsic_values) if wsic_values else 0

    def get_granularity_metrics(self) -> Tuple[int, Dict[str, int], int]:
        """
        Get all granularity metrics: N, WSIC, and WsicT.
        """
        n = self.calculate_number_of_microservices()
        wsic_metrics = self.calculate_wsic_metric()
        wsic_total = self.calculate_wsic_total()

        return n, wsic_metrics, wsic_total

    def calculate_calls_metric(self) -> Dict[str, int]:
        """
        Calculate the number of calls (Calls) for each microservice.
        Calls corresponds to the number of invocations of MSi to other microservices.
        """
        calls_metrics = {ms_id: 0 for ms_id in self.microservice_manager.microservices}

        for ms_id, microservice in self.microservice_manager.microservices.items():
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            for story in stories:
                for dep in story.dependencies:
                    if dep not in microservice.stories:
                        calls_metrics[ms_id] += 1

        return calls_metrics

    def calculate_requests_metric(self) -> Dict[str, int]:
        """
        Calculate the number of requests (Requests) for each microservice.
        Requests corresponds to the number of invocations of other microservices to MSi.
        """
        requests_metrics = {ms_id: 0 for ms_id in self.microservice_manager.microservices}

        for ms_id, microservice in self.microservice_manager.microservices.items():
            for other_ms_id, other_microservice in self.microservice_manager.microservices.items():
                if ms_id != other_ms_id:
                    other_stories = self.microservice_manager.get_microservice_stories(other_ms_id)
                    for story in other_stories:
                        if any(dep in microservice.stories for dep in story.dependencies):
                            requests_metrics[ms_id] += 1

        return requests_metrics

    def calculate_average_calls(self) -> float:
        """
        Calculate the Average of calls of MSBA (Avg. Calls).
        Avg. Calls is the average of calls among microservices of MSBA.
        """
        calls_metrics = self.calculate_calls_metric()
        total_calls = sum(calls_metrics.values())
        number_of_microservices = len(self.microservice_manager.microservices)

        return total_calls / number_of_microservices if number_of_microservices > 0 else 0

    def get_performance_metrics(self) -> Tuple[Dict[str, int], Dict[str, int], float]:
        """
        Get all performance metrics: Calls, Requests, and Avg. Calls.
        """
        calls_metrics = self.calculate_calls_metric()
        requests_metrics = self.calculate_requests_metric()
        avg_calls = self.calculate_average_calls()

        return calls_metrics, requests_metrics, avg_calls

    def calculate_story_points(self) -> Dict[str, int]:
        """
        Calculate the total story points (P) for each microservice.
        """
        story_points = {}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            story_points[ms_id] = sum(story.story_points for story in stories)
        return story_points

    def calculate_cg(self) -> Dict[str, int]:
        """
        Calculate Cg for each microservice.
        Cg = P * (Calls + Requests)
        """
        story_points = self.calculate_story_points()
        calls_metrics = self.calculate_calls_metric()
        requests_metrics = self.calculate_requests_metric()

        cg = {}
        for ms_id in self.microservice_manager.microservices:
            cg[ms_id] = story_points[ms_id] * (calls_metrics[ms_id] + requests_metrics[ms_id])
        return cg

    def calculate_pf(self) -> Dict[str, int]:
        pf = {}
        for ms_id in self.microservice_manager.microservices:
            pf[ms_id] = self._calculate_max_depth(ms_id, set())
        return pf

    def _calculate_max_depth(self, ms_id: str, visited: Set[str]) -> int:
        if ms_id in visited:
            return 0
        visited.add(ms_id)
        max_depth = 0
        stories = self.microservice_manager.get_microservice_stories(ms_id)
        for story in stories:
            for dep in story.dependencies:
                for other_ms_id, other_ms in self.microservice_manager.microservices.items():
                    if other_ms_id != ms_id and dep in other_ms.stories:
                        depth = 1 + self._calculate_max_depth(other_ms_id, visited.copy())
                        max_depth = max(max_depth, depth)
        return max_depth

    def calculate_cognitive_complexity(self) -> float:
        cg = self.calculate_cg()
        story_points = self.calculate_story_points()
        pf = self.calculate_pf()
        wsic_total = self.calculate_wsic_total()
        siy_total = self.calculate_siy_total()

        n = len(self.microservice_manager.microservices)
        max_story_points = max(story_points.values()) if story_points else 0

        cxt = (sum(cg.values()) / 2) * \
              (max_story_points / 2) * \
              (n / 2) * \
              (wsic_total / 2) * \
              (sum(pf.values()) / 2) * \
              ((siy_total + 2) / 2)

        return cxt

    def get_complexity_metrics(self) -> Tuple[Dict[str, int], Dict[str, int], Dict[str, int], float]:
        """
        Get all complexity metrics: Story Points (P), Cg, Pf, and Cognitive Complexity Points (CxT).
        """
        story_points = self.calculate_story_points()
        cg = self.calculate_cg()
        pf = self.calculate_pf()
        cxt = self.calculate_cognitive_complexity()

        return story_points, cg, pf, cxt

    def calculate_microservice_development_time(self) -> Dict[str, float]:
        """
        Calculate the estimated development time (ti) for each microservice.
        ti is the sum of the estimated development time of each user story in the microservice.
        """
        development_times = {}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            development_times[ms_id] = sum(story.estimated_time for story in stories)
        return development_times

    def calculate_msba_development_time(self) -> float:
        """
        Calculate the estimated development time (T) for the entire MSBA.
        T is the maximum development time among all microservices.
        """
        development_times = self.calculate_microservice_development_time()
        return max(development_times.values()) if development_times else 0

    def get_development_time_metrics(self) -> Tuple[Dict[str, float], float]:
        """
        Get all development time metrics:
        Microservice Development Time (ti) and MSBA Development Time (T).
        """
        microservice_times = self.calculate_microservice_development_time()
        msba_time = self.calculate_msba_development_time()
        return microservice_times, msba_time

    def calculate_semantic_similarity(self) -> Dict[str, float]:
        """
        Calculate the Semantic Similarity (SSi) for each microservice.
        """
        similarities = {}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            story_ids = list(microservice.stories)
            if story_ids:
                similarity = self.semantic_calculator.calculate_microservice_similarity(story_ids)
                similarities[ms_id] = similarity
            else:
                similarities[ms_id] = 0.0
        return similarities

    def calculate_total_semantic_similarity(self) -> float:
        similarities = self.calculate_semantic_similarity()
        return 100 * sum(similarities.values()) / len(similarities) if similarities else 0

    def get_semantic_similarity_metrics(self) -> Tuple[Dict[str, float], float]:
        """
        Get all semantic similarity metrics:
        Microservice Semantic Similarity (SSi) and MSBA Semantic Similarity (SsT).
        """
        microservice_similarities = self.calculate_semantic_similarity()
        total_similarity = self.calculate_total_semantic_similarity()
        return microservice_similarities, total_similarity

    def verify_semantic_similarity(self):
        """
        Verify the semantic similarity dictionary and print its contents and statistics.
        """
        print("Verifying Semantic Similarity Dictionary:")
        self.semantic_calculator.print_similarity_dict()
        print("\n")
        self.semantic_calculator.print_similarity_dict_stats()

    def print_user_stories(self):
        print("User Stories:")
        for ms_id, microservice in self.microservice_manager.microservices.items():
            print(f"\nMicroservice {ms_id}:")
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            for story in stories:
                print(f"  ID: {story.identifier}")
                print(f"  Title: {story.title}")
                print(f"  Description: {story.description}")
                print("  ---")


