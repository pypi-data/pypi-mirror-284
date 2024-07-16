import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import networkx as nx


class MicroserviceVisualizer:
    def __init__(self, microservice_manager):
        self.microservice_manager = microservice_manager

    def plot_microservices(self, base_color='lightblue', title=None):
        G = nx.DiGraph()

        # Create nodes and calculate sizes
        max_story_points = 1  # To avoid division by zero
        for ms_id, microservice in self.microservice_manager.microservices.items():
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            total_story_points = sum(story.story_points for story in stories)
            G.add_node(ms_id, story_points=total_story_points)
            max_story_points = max(max_story_points, total_story_points)

        # Add edges based on dependencies and calculate weights
        edge_weights = {}
        for ms_id, microservice in self.microservice_manager.microservices.items():
            stories = self.microservice_manager.get_microservice_stories(ms_id)
            for story in stories:
                for dep in story.dependencies:
                    for other_ms_id, other_microservice in self.microservice_manager.microservices.items():
                        if other_ms_id != ms_id:
                            if dep in other_microservice.stories:
                                edge = (other_ms_id, ms_id)
                                edge_weights[edge] = edge_weights.get(edge, 0) + 1

        # Add edges to the graph with calculated weights
        for edge, weight in edge_weights.items():
            G.add_edge(edge[0], edge[1], weight=weight)

        # Create figure and axes
        fig, ax = plt.subplots(figsize=(16, 12))

        # Use a layout that separates the nodes more
        pos = nx.spring_layout(G, k=1.5, iterations=50)

        # Draw nodes with color based on story points
        node_sizes = [G.nodes[node]['story_points'] * 30 for node in G.nodes()]
        node_colors = [self.adjust_color_intensity(base_color, G.nodes[node]['story_points'] / max_story_points) for
                       node in G.nodes()]
        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, ax=ax)

        # Draw edges
        edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
        nx.draw_networkx_edges(G, pos, ax=ax, width=edge_weights, edge_color='gray',
                               arrows=True, arrowsize=20, arrowstyle='->', connectionstyle='arc3,rad=0.1')

        # Add node labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold", ax=ax)

        # Add edge labels (weight)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, ax=ax)

        if title:
            ax.set_title(title)
        else:
            ax.set_title("Microservices Dependency Graph")

        ax.axis('off')

        # Adjust graph limits
        ax.margins(0.2)  # Add margin around the graph

        # Adjust layout and display
        fig.tight_layout()
        plt.show()

    def adjust_color_intensity(self, base_color, intensity):
        """Adjust the intensity of the base color based on the number of story points"""
        rgb = mcolors.to_rgb(base_color)
        hsv = mcolors.rgb_to_hsv(rgb)
        # Adjust saturation and value (brightness) based on intensity
        hsv[1] = min(hsv[1] + 0.6 * intensity, 1.0)  # Increase saturation
        hsv[2] = max(hsv[2] - 0.6 * intensity, 0.2)  # Decrease brightness (darker)
        return mcolors.hsv_to_rgb(hsv)
