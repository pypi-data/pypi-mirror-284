from microservice_story_manager import UserStoryManager, MicroserviceManager, GeneticMicroserviceAssigner, \
    MicroserviceVisualizer, MicroserviceMetricsManager, FitnessFunctions

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


metrics_manager = MicroserviceMetricsManager(microservice_manager)

ais_total, ads_total, siy_total = metrics_manager.get_coupling_indicators()
print(f"AIS Total: {ais_total:.2f}")
print(f"ADS Total: {ads_total:.2f}")
print(f"SIY Total: {siy_total:.2f}")

cpt = metrics_manager.calculate_coupling_total()
print(f"Coupling Total (CpT): {cpt:.2f}")

coh_vector = metrics_manager.get_coh_vector()
print(f"Vector Coh: {coh_vector}")

lc_metrics, coh_metrics, coh_total = metrics_manager.get_cohesion_metrics()
print("Métricas de cohesión:")
print(f"LC: {lc_metrics}")
print(f"Coh: {coh_metrics}")
print(f"Coh Total: {coh_total:.4f}")



n, wsic_metrics, wsic_total = metrics_manager.get_granularity_metrics()
print("Métricas de granularidad:")
print(f"N: {n}")
print(f"WSIC: {wsic_metrics}")
print(f"WsicT: {wsic_total}")

calls_metrics, requests_metrics, avg_calls = metrics_manager.get_performance_metrics()
print("Métricas de rendimiento:")
print(f"Calls: {calls_metrics}")
print(f"Requests: {requests_metrics}")
print(f"Avg. Calls: {avg_calls:.2f}")

story_points, cg, pf, cxt = metrics_manager.get_complexity_metrics()

print("Métricas de complejidad:")

print(f"\nCognitive Complexity Points (CxT): {cxt:.2f}")


microservice_times, msba_time = metrics_manager.get_development_time_metrics()

print("Métricas de Tiempo de Desarrollo:")
print("\nTiempo de Desarrollo por Microservicio (ti):")
for ms_id, time in microservice_times.items():
    print(f"  Microservice {ms_id}: {time:.2f} horas")

print(f"\nTiempo de Desarrollo Estimado de MSBA (T): {msba_time:.2f} horas")

metrics_manager.verify_semantic_similarity()

print("Printing User Stories:")
metrics_manager.print_user_stories()

print("\nVerifying Semantic Similarity:")
metrics_manager.verify_semantic_similarity()

microservice_similarities, total_similarity = metrics_manager.get_semantic_similarity_metrics()
print("Métricas de Similitud Semántica:")
print("\nSimilitud Semántica por Microservicio (SSi):")
for ms_id, similarity in microservice_similarities.items():
    print(f"  Microservice {ms_id}: {similarity:.2f}")

print(f"\nSimilitud Semántica Total de MSBA (SsT): {total_similarity:.2f}")


fitness1 = FitnessFunctions(metrics_manager).f1()
fitness2 = FitnessFunctions(metrics_manager).f2()
print(fitness1, fitness2)
