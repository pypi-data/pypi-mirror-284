from microservice_story_manager import UserStoryManager, MicroserviceManager, MicroserviceVisualizer, \
    GeneticMicroserviceAssigner, FitnessFunctions, MetricsVisualizer, MicroserviceMetricsManager

# Initialize managers
user_story_manager = UserStoryManager()
user_story_manager.load_stories_from_csv('../examples/user_stories.csv')

microservice_manager = MicroserviceManager(user_story_manager)

# Create microservices
for _ in range(5):
    microservice_manager.create_microservice()

# Create FitnessFunctions instance
fitness_functions = FitnessFunctions(MicroserviceMetricsManager(microservice_manager))

# Choose fitness functions to compare
functions_to_compare = [
    (fitness_functions.f1, "f1", True),
    (fitness_functions.f2, "f2", True)
]

results = []

for func, name, minimize in functions_to_compare:
    assigner = GeneticMicroserviceAssigner(user_story_manager, microservice_manager, func, minimize)
    optimized_manager, fitness_value, detailed_metrics, story_assignments = assigner.optimize_assignments(generations=3, population_size=10)
    results.append((name, optimized_manager, fitness_value, detailed_metrics, story_assignments))

    print(f"\nResults for fitness function {name}:")
    print(f"Best fitness: {fitness_value}")
    print(f"Detailed metrics: {detailed_metrics}")
    print("\nStory Assignments:")
    for ms_id, stories in story_assignments.items():
        print(f"\nMicroservice {ms_id}:")
        for story in stories:
            print(f"  - {story}")

# Compare metrics
MetricsVisualizer.compare_metrics(results[0][3], results[1][3], results[0][0], results[1][0])

# Compare fitness values
MetricsVisualizer.compare_fitness_values([result[2] for result in results], [result[0] for result in results])

# Visualize the optimized microservices
for name, manager, _, _, _ in results:
    visualizer = MicroserviceVisualizer(manager)
    visualizer.plot_microservices(title=f"Optimized Microservices using {name}")
