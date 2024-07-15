import random
import numpy as np  # Add this line
from typing import List, Dict, Tuple, Callable
from deap import base, creator, tools, algorithms

from microservice_story_manager import MicroserviceVisualizer
from microservice_story_manager.metrics_visualizer import MetricsVisualizer
from user_story_manager import UserStoryManager
from microservice_manager import MicroserviceManager
from microservice_metrics import MicroserviceMetricsManager
from fitness_functions import FitnessFunctions


class GeneticMicroserviceAssigner:
    def __init__(self, user_story_manager: UserStoryManager, microservice_manager: MicroserviceManager,
                 fitness_function: Callable, minimize: bool = True):
        self.user_story_manager = user_story_manager
        self.microservice_manager = microservice_manager
        self.metrics_manager = MicroserviceMetricsManager(microservice_manager)
        self.fitness_functions = FitnessFunctions(self.metrics_manager)
        self.fitness_function = fitness_function
        self.minimize = minimize

        self.n_stories = len(self.user_story_manager.get_all_stories())
        self.n_microservices = len(self.microservice_manager.microservices)


    def create_individual(self) -> List[int]:
        """Create a random individual (chromosome)"""
        return [random.randint(0, self.n_microservices - 1) for _ in range(self.n_stories)]

    def setup_genetic_algorithm(self):
        if self.minimize:
            creator.create("Fitness", base.Fitness, weights=(-1.0,))
        else:
            creator.create("Fitness", base.Fitness, weights=(1.0,))

        creator.create("Individual", list, fitness=creator.Fitness)

        toolbox = base.Toolbox()
        toolbox.register("individual", tools.initIterate, creator.Individual, self.create_individual)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)

        def evaluate(individual):
            self.assign_stories_to_microservices(individual)
            return (self.fitness_function(),)  # Note: removed self.metrics_manager

        toolbox.register("evaluate", evaluate)
        toolbox.register("mate", tools.cxTwoPoint)
        toolbox.register("mutate", tools.mutUniformInt, low=0, up=self.n_microservices - 1, indpb=0.1)
        toolbox.register("select", tools.selTournament, tournsize=3)

        return toolbox

    def assign_stories_to_microservices(self, individual: List[int]) -> None:
        """Assign stories to microservices based on the individual"""
        # Clear existing assignments
        for ms in self.microservice_manager.microservices.values():
            ms.stories.clear()

        # Assign stories based on the individual
        stories = list(self.user_story_manager.get_all_stories().keys())
        for story_idx, ms_idx in enumerate(individual):
            ms_id = list(self.microservice_manager.microservices.keys())[ms_idx]
            self.microservice_manager.add_story_to_microservice(ms_id, stories[story_idx])

        # Print final assignments
        """for ms_id, ms in self.microservice_manager.microservices.items():
            print(f"Microservice {ms_id} has stories: {ms.stories}")"""

    def run_genetic_algorithm(self, toolbox, generations=50, population_size=100):
        """Run the genetic algorithm"""
        population = toolbox.population(n=population_size)
        hof = tools.HallOfFame(1)
        stats = tools.Statistics(lambda ind: ind.fitness.values)
        stats.register("avg", np.mean)
        stats.register("min", np.min)
        stats.register("max", np.max)

        population, logbook = algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2,
                                                  ngen=generations, stats=stats, halloffame=hof, verbose=True)

        return hof[0], logbook

    def optimize_assignments(self, generations=50, population_size=100) -> Tuple[
        MicroserviceManager, float, Dict, Dict[str, List[str]]]:
        print(f"\nOptimizing using provided fitness function")
        toolbox = self.setup_genetic_algorithm()
        best_individual, logbook = self.run_genetic_algorithm(toolbox, generations, population_size)

        optimized_microservice_manager = self.create_optimized_microservice_manager(best_individual)

        # Calculate detailed metrics
        detailed_metrics = self.calculate_detailed_metrics(optimized_microservice_manager)

        # Get story assignments
        story_assignments = self.get_story_assignments(optimized_microservice_manager)

        return optimized_microservice_manager, best_individual.fitness.values[0], detailed_metrics, story_assignments

    def get_story_assignments(self, microservice_manager: MicroserviceManager) -> Dict[str, List[str]]:
        assignments = {}
        for ms_id, microservice in microservice_manager.microservices.items():
            stories = microservice_manager.get_microservice_stories(ms_id)
            assignments[ms_id] = [f"{story.title}" for story in stories]
        return assignments

    def calculate_detailed_metrics(self, microservice_manager: MicroserviceManager) -> Dict:
        metrics = MicroserviceMetricsManager(microservice_manager)
        return {
            "coupling": metrics.calculate_coupling_total(),
            "cohesion": metrics.calculate_coh_total(),
            "granularity": metrics.calculate_wsic_total(),
            "complexity": metrics.calculate_cognitive_complexity(),
            "semantic_similarity": metrics.calculate_total_semantic_similarity()
        }

    def create_optimized_microservice_manager(self, individual: List[int]) -> MicroserviceManager:
        """Create a new MicroserviceManager with the optimized assignments"""
        optimized_manager = MicroserviceManager(self.user_story_manager)

        # Create the same number of microservices as in the original manager
        for _ in range(self.n_microservices):
            optimized_manager.create_microservice()

        # Assign stories based on the individual
        stories = list(self.user_story_manager.get_all_stories().keys())
        for story_idx, ms_idx in enumerate(individual):
            ms_id = list(optimized_manager.microservices.keys())[ms_idx]
            optimized_manager.add_story_to_microservice(ms_id, stories[story_idx])

        return optimized_manager

    def get_microservice_assignments(self, chromosome: List[int]) -> Dict[str, List[str]]:
        """Get microservice assignments from a chromosome"""
        assignments = {ms_id: [] for ms_id in self.microservice_manager.microservices}
        stories = list(self.user_story_manager.get_all_stories().keys())
        for story_idx, ms_idx in enumerate(chromosome):
            ms_id = list(self.microservice_manager.microservices.keys())[ms_idx]
            assignments[ms_id].append(stories[story_idx])
        return assignments

    def print_results(self, results: Dict[str, Tuple[List[int], float]]) -> None:
        """Print optimization results"""
        for fitness_name, (best_chromosome, fitness_value) in results.items():
            print(f"\nBest assignment for fitness function {fitness_name}:")
            assignments = self.get_microservice_assignments(best_chromosome)
            for ms_id, stories in assignments.items():
                print(f"  Microservice {ms_id}: {stories}")

            print(f"  Fitness value: {fitness_value}")

            # Calculate and display metrics for this assignment
            self.assign_stories_to_microservices(best_chromosome)
            cpt = self.metrics_manager.calculate_coupling_total()
            coht = self.metrics_manager.calculate_coh_total()
            wsict = self.metrics_manager.calculate_wsic_total()
            cxt = self.metrics_manager.calculate_cognitive_complexity()
            sst = self.metrics_manager.calculate_total_semantic_similarity()

            print(f"  Metrics:")
            print(f"    Coupling (CpT): {cpt}")
            print(f"    Cohesion (CohT): {coht}")
            print(f"    Granularity (WsicT): {wsict}")
            print(f"    Complexity (CxT): {cxt}")
            print(f"    Semantic Similarity (SsT): {sst}")



user_story_manager = UserStoryManager()
user_story_manager.set_project_language('en')
user_story_manager.load_stories_from_csv('../examples/user_stories.csv')

microservice_manager = MicroserviceManager(user_story_manager)
microservice_manager.set_project_language('en')

# Create initial microservices (adjust the number as needed)
for _ in range(8):
    microservice_manager.create_microservice()

    # Create and run the genetic algorithm
# Create FitnessFunctions instance
fitness_functions = FitnessFunctions(MicroserviceMetricsManager(microservice_manager))


# Define the two fitness functions to compare
functions_to_compare = [
    (fitness_functions.f1, "f1", True),
    (fitness_functions.f2, "f2", True)
]

results = []

for func, name, minimize in functions_to_compare:
    assigner = GeneticMicroserviceAssigner(user_story_manager, microservice_manager, func, minimize)
    optimized_manager, fitness_value, detailed_metrics, story_assignments = assigner.optimize_assignments(generations=5, population_size=10)
    results.append((name, optimized_manager, fitness_value, detailed_metrics, story_assignments))

    print(f"\nResultados para la función de fitness {name}:")
    print(f"Mejor fitness: {fitness_value}")
    print(f"Métricas detalladas: {detailed_metrics}")
    print("\nAsignaciones de historias:")
    for ms_id, stories in story_assignments.items():
        print(f"\nMicroservicio {ms_id}:")
        for story in stories:
            print(f"  - {story}")

# Compare metrics
MetricsVisualizer.compare_metrics(
    results[0][3], results[1][3],
    results[0][0], results[1][0]
)

# Compare fitness values
MetricsVisualizer.compare_fitness_values(
    [result[2] for result in results],
    [result[0] for result in results]
)

# Visualize the optimized microservices
for name, manager, _, _, _ in results:
    visualizer = MicroserviceVisualizer(manager)
    visualizer.plot_microservices(title=f"Microservicios optimizados usando {name}")
