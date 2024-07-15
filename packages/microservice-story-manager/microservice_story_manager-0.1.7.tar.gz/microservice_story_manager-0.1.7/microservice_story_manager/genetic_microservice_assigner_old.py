import random
from typing import Callable, List, Tuple

from deap import algorithms, base, creator, tools

from microservice_story_manager import MicroserviceManager, UserStoryManager


class GeneticMicroserviceAssigner:
    def __init__(self, user_story_manager: UserStoryManager, microservice_manager: MicroserviceManager):
        self.user_story_manager = user_story_manager
        self.microservice_manager = microservice_manager
        self.stories = list(user_story_manager.get_all_stories().keys())
        self.microservices = list(microservice_manager.microservices.keys())

    def setup_genetic_algorithm(self, fitness_func: Callable[[List[int]], Tuple[float,]]):
        creator.create("FitnessMax", base.Fitness, weights=(1.0,))
        creator.create("Individual", list, fitness=creator.FitnessMax)

        self.toolbox = base.Toolbox()
        self.toolbox.register("attr_int", random.randint, 0, len(self.microservices) - 1)
        self.toolbox.register("individual", tools.initRepeat, creator.Individual, self.toolbox.attr_int,
                              n=len(self.stories))
        self.toolbox.register("population", tools.initRepeat, list, self.toolbox.individual)

        self.toolbox.register("evaluate", fitness_func)
        self.toolbox.register("mate", tools.cxTwoPoint)
        self.toolbox.register("mutate", tools.mutUniformInt, low=0, up=len(self.microservices) - 1, indpb=0.1)
        self.toolbox.register("select", tools.selTournament, tournsize=3)

    def run_genetic_algorithm(self, population_size: int = 100, generations: int = 50) -> List[int]:
        population = self.toolbox.population(n=population_size)
        algorithms.eaSimple(population, self.toolbox, cxpb=0.7, mutpb=0.2, ngen=generations, verbose=False)

        best_individual = tools.selBest(population, k=1)[0]
        return best_individual

    def assign_stories_to_microservices(self, assignment: List[int]) -> None:
        # Clear existing assignments
        for ms in self.microservice_manager.microservices.values():
            ms.stories.clear()

        # Assign stories based on the genetic algorithm result
        for story_id, ms_index in zip(self.stories, assignment):
            ms_id = self.microservices[ms_index]
            self.microservice_manager.add_story_to_microservice(ms_id, story_id)

    def optimize_assignment(self, fitness_func: Callable[[List[int]], Tuple[float,]], population_size: int = 100,
                            generations: int = 50) -> None:
        self.setup_genetic_algorithm(fitness_func)
        best_assignment = self.run_genetic_algorithm(population_size, generations)
        self.assign_stories_to_microservices(best_assignment)
