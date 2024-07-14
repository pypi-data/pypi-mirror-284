from microservice_story_manager import UserStoryManager, MicroserviceManager, GeneticMicroserviceAssigner, \
    MicroserviceVisualizer


user_story_manager = UserStoryManager()
user_story_manager.set_project_language('en')
user_story_manager.load_stories_from_csv('../examples/user_stories.csv')

user_story_manager.plot_stories()

microservice_manager = MicroserviceManager(user_story_manager)
microservice_manager.set_project_language('en')

# Create some microservices
for _ in range(8):
    microservice_manager.create_microservice()


# Define a simple fitness function (to be replaced with a more sophisticated one)
def simple_fitness(assignment):
    # This fitness function aims to balance the number of stories across microservices
    microservice_loads = [0] * len(microservice_manager.microservices)
    for ms_index in assignment:
        microservice_loads[ms_index] += 1
    return (1 / (max(microservice_loads) - min(microservice_loads) + 1),)


# Create and run the genetic algorithm
assigner = GeneticMicroserviceAssigner(user_story_manager, microservice_manager)
assigner.optimize_assignment(simple_fitness, population_size=100, generations=50)

# Validate and visualize the result
try:
    microservice_manager.validate_all_stories_assigned()
    print("All stories are assigned to microservices.")
except ValueError as e:
    print(f"Error: {str(e)}")

visualizer = MicroserviceVisualizer(microservice_manager)
visualizer.plot_microservices(base_color='lightgreen')
