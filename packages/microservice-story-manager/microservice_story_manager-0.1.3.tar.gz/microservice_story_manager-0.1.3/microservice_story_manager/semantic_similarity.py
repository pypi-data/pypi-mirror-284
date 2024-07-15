# semantic_similarity.py

import spacy
from typing import List, Dict, Tuple


class SemanticSimilarityCalculator:
    def __init__(self, user_story_manager):
        self.nlp = spacy.load("en_core_web_md")
        self.similarity_dict = {}
        self.user_story_manager = user_story_manager

    def preprocess_text(self, text: str) -> str:
        doc = self.nlp(text)
        lemmas = [token.lemma_ for token in doc if token.pos_ in ["NOUN", "VERB", "ADJ"]]
        return " ".join(lemmas)

    def calculate_similarity(self, story_id1: str, story_id2: str) -> float:
        story1 = self.user_story_manager.get_story(story_id1)
        story2 = self.user_story_manager.get_story(story_id2)
        if story1 is None or story2 is None:
            return 0.0
        text1 = f"{story1.title} {story1.description}"
        text2 = f"{story2.title} {story2.description}"
        doc1 = self.nlp(self.preprocess_text(text1))
        doc2 = self.nlp(self.preprocess_text(text2))
        similarity = doc1.similarity(doc2)
        return similarity

    def calculate_microservice_similarity(self, story_ids: List[str]) -> float:
        total_similarity = 0.0
        comparisons = 0
        for i, id1 in enumerate(story_ids):
            for id2 in story_ids[i+1:]:
                similarity = self.calculate_similarity(id1, id2)
                total_similarity += similarity
                comparisons += 1
        return total_similarity / comparisons if comparisons > 0 else 0.0
