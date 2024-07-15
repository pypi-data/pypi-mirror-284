from typing import Dict, List, Set, Union
import csv
import networkx as nx
import matplotlib.pyplot as plt
from microservice_story_manager.error_messages import get_error_message


class UserStory:
    def __init__(self, title: str, description: str, language: str, dependencies: List[str],
                 story_points: int, estimated_time: float, scenario: str, observations: str):
        self.identifier = None
        self.title = title
        self.description = description
        self.language = language
        self.dependencies = dependencies
        self.story_points = story_points
        self.estimated_time = estimated_time
        self.scenario = scenario
        self.observations = observations


class UserStoryManager:
    def __init__(self):
        self.stories: Dict[str, UserStory] = {}
        self.pending_dependencies: Dict[str, Set[str]] = {}
        self.project_language: str = 'en'  # Default language

    def set_project_language(self, language: str) -> None:
        self.project_language = language

    def add_story(self, identifier: str, title: str, description: str, language: str,
                  dependencies: List[str], story_points: Union[int, str],
                  estimated_time: Union[float, str], scenario: str, observations: str) -> None:
        if identifier in self.stories:
            raise ValueError(get_error_message('story_exists', self.project_language).format(identifier))

        try:
            story_points = int(story_points)
            if story_points <= 0:
                raise ValueError
        except ValueError:
            raise ValueError(get_error_message('invalid_story_points', self.project_language))

        try:
            estimated_time = float(estimated_time)
            if estimated_time <= 0:
                raise ValueError
        except ValueError:
            raise ValueError(get_error_message('invalid_estimated_time', self.project_language))

        self.stories[identifier] = UserStory(title, description, language, dependencies,
                                             story_points, estimated_time, scenario, observations)

        if identifier in self.pending_dependencies:
            del self.pending_dependencies[identifier]

        for dep in dependencies:
            if dep not in self.stories:
                if dep not in self.pending_dependencies:
                    self.pending_dependencies[dep] = set()
                self.pending_dependencies[dep].add(identifier)

    def get_story(self, identifier: str) -> UserStory:
        if identifier not in self.stories:
            raise ValueError(get_error_message('story_not_found', self.project_language).format(identifier))
        return self.stories[identifier]

    def get_all_stories(self) -> Dict[str, UserStory]:
        return self.stories

    def validate_integrity(self) -> bool:
        if self.pending_dependencies:
            missing = ", ".join(self.pending_dependencies.keys())
            raise ValueError(get_error_message('missing_dependencies', self.project_language).format(missing))
        return True

    def get_total_story_points(self) -> int:
        return sum(story.story_points for story in self.stories.values())

    def get_total_estimated_time(self) -> float:
        return sum(story.estimated_time for story in self.stories.values())

    def plot_stories(self) -> None:
        G = nx.DiGraph()

        for identifier, story in self.stories.items():
            G.add_node(identifier,
                       story_points=story.story_points,
                       title=story.title)
            for dep in story.dependencies:
                G.add_edge(dep, identifier)

        pos = nx.spring_layout(G)

        plt.figure(figsize=(12, 8))

        node_sizes = [story.story_points * 100 for story in self.stories.values()]

        nx.draw(G, pos, with_labels=False, node_color='lightblue',
                node_size=node_sizes, arrows=True)

        labels = {identifier: f"{story.title}\n({story.story_points} SP)" for identifier, story in self.stories.items()}
        nx.draw_networkx_labels(G, pos, labels, font_size=8)

        plt.title("User Stories Dependency Graph")
        plt.axis('off')
        plt.tight_layout()
        plt.show()

    def load_stories_from_csv(self, file_path: str) -> None:
        with open(file_path, 'r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    dependencies = [dep.strip() for dep in row['dependencies'].split(',') if dep.strip()]
                    self.add_story(
                        identifier=row['identifier'],
                        title=row['title'],
                        description=row['description'],
                        language=row['language'],
                        dependencies=dependencies,
                        story_points=row['story_points'],
                        estimated_time=row['estimated_time'],
                        scenario=row['scenario'],
                        observations=row['observations']
                    )
                except Exception as e:
                    print(f"Error adding story {row['identifier']}: {str(e)}")

        try:
            self.validate_integrity()
            print("All stories were loaded correctly and integrity is valid.")
        except ValueError as e:
            print(f"Integrity error: {str(e)}")

    def update_story_identifier(self, old_identifier: str, new_identifier: str) -> None:
        if old_identifier not in self.stories:
            raise ValueError(f"Story with ID {old_identifier} does not exist.")

        story = self.stories[old_identifier]
        story.identifier = new_identifier
        self.stories[new_identifier] = story
        del self.stories[old_identifier]
