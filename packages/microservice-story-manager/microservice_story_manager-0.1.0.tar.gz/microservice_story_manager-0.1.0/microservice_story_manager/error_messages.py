ERROR_MESSAGES = {
    'story_exists': {
        'en': "A story with the identifier {} already exists.",
        'es': "Ya existe una historia con el identificador {}."
    },
    'invalid_story_points': {
        'en': "Story points must be a positive integer.",
        'es': "Los story points deben ser un número entero positivo."
    },
    'invalid_estimated_time': {
        'en': "Estimated time must be a positive number.",
        'es': "El tiempo estimado debe ser un número positivo."
    },
    'story_not_found': {
        'en': "There is no story with the identifier {}.",
        'es': "No existe una historia con el identificador {}."
    },
    'missing_dependencies': {
        'en': "The following stories are referenced but do not exist: {}",
        'es': "Las siguientes historias son referenciadas pero no existen: {}"
    },
    'microservice_empty': {
        'en': "Microservice cannot be empty.",
        'es': "El microservicio no puede estar vacío."
    },
    'story_already_assigned': {
        'en': "The story {} is already assigned to another microservice.",
        'es': "La historia {} ya está asignada a otro microservicio."
    },
    'story_not_in_backlog': {
        'en': "The story {} is not in the backlog.",
        'es': "La historia {} no está en el backlog."
    }
}


def get_error_message(key: str, language: str) -> str:
    return ERROR_MESSAGES[key][language]


def add_language(language: str, messages: dict) -> None:
    for key in ERROR_MESSAGES:
        if key in messages:
            ERROR_MESSAGES[key][language] = messages[key]
        else:
            print(f"Warning: Message for key '{key}' not provided for language '{language}'")
