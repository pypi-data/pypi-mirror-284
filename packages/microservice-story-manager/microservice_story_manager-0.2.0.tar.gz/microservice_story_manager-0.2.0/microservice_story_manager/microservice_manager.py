# microservice_manager.py

from typing import Dict, List, Set

from microservice_story_manager import UserStoryManager, UserStory
from microservice_story_manager.error_messages import get_error_message


class Microservice:
    def __init__(self, identifier: str):
        self.identifier = identifier
        self.stories: Set[str] = set()


class MicroserviceManager:
    def __init__(self, user_story_manager: UserStoryManager):
        self.microservices: Dict[str, Microservice] = {}
        self.user_story_manager = user_story_manager
        self.project_language: str = 'en'  # Default language
        self.next_id: int = 1
        self.story_counter = {}

    def set_project_language(self, language: str) -> None:
        self.project_language = language

    def create_microservice(self) -> str:
        identifier = f"ms{self.next_id:03d}"
        self.microservices[identifier] = Microservice(identifier)
        self.next_id += 1
        return identifier

    def add_story_to_microservice(self, microservice_id: str, story_id: str) -> None:
        if microservice_id not in self.microservices:
            raise ValueError(f"Microservice with ID {microservice_id} does not exist.")

        story = self.user_story_manager.get_story(story_id)
        if story is None:
            raise ValueError(f"Story with ID {story_id} does not exist.")

        self.microservices[microservice_id].stories.add(story_id)
        """print(f"Added story {story_id} to microservice {microservice_id}")
        print(f"Story dependencies: {story.dependencies}")"""

    def remove_story_from_microservice(self, microservice_id: str, story_id: str) -> None:
        if microservice_id not in self.microservices:
            raise ValueError(get_error_message('story_not_found', self.project_language).format(microservice_id))

        if story_id not in self.microservices[microservice_id].stories:
            raise ValueError(get_error_message('story_not_found', self.project_language).format(story_id))

        self.microservices[microservice_id].stories.remove(story_id)

        if not self.microservices[microservice_id].stories:
            raise ValueError(get_error_message('microservice_empty', self.project_language))

    def get_microservice_stories(self, microservice_id: str) -> List[UserStory]:
        if microservice_id not in self.microservices:
            raise ValueError(get_error_message('story_not_found', self.project_language).format(microservice_id))

        return [self.user_story_manager.get_story(story_id) for story_id in self.microservices[microservice_id].stories]

    def get_all_microservices(self) -> Dict[str, List[UserStory]]:
        return {ms_id: self.get_microservice_stories(ms_id) for ms_id in self.microservices}

    def validate_all_stories_assigned(self) -> bool:
        all_stories = set(self.user_story_manager.get_all_stories().keys())
        assigned_stories = set()
        for ms in self.microservices.values():
            assigned_stories.update(ms.stories)

        unassigned_stories = all_stories - assigned_stories
        if unassigned_stories:
            raise ValueError(
                f"The following stories are not assigned to any microservice: {', '.join(unassigned_stories)}")
        return True

    def get_microservice_dependencies(self) -> Dict[str, Set[str]]:
        dependencies = {ms_id: set() for ms_id in self.microservices}
        for ms_id, ms in self.microservices.items():
            for story_id in ms.stories:
                story = self.user_story_manager.get_story(story_id)
                for dep_story_id in story.dependencies:
                    for dep_ms_id, dep_ms in self.microservices.items():
                        if dep_story_id in dep_ms.stories and dep_ms_id != ms_id:
                            dependencies[ms_id].add(dep_ms_id)
        return dependencies


