from datetime import datetime
import constants
from sqlite.functions import TriviaDatabase

_db = TriviaDatabase()


def get_categories():
    categories = [
        constants.plum_category,
        constants.coop_category,
        constants.any_category,
        constants.anime_category,
        constants.animals_category,
        constants.computers_category,
        # constants.politics_category, # Problem with api
        constants.geography_category,
        constants.general_knowledge_category
    ]
    return categories


class TriviaGame:
    def __init__(self, type_of_trivia, created_by, num_of_questions=5, seconds_per_question=30, is_complete=False, created_date=None, end_date=None):
        self.type_of_trivia = type_of_trivia
        self.num_of_questions = num_of_questions
        self.seconds_per_question = seconds_per_question
        self.is_complete = is_complete
        self.created_by = created_by
        if created_date is None:
            created_date = datetime.now()
        self.created_date = created_date
        self.end_date = end_date
        #
        # if db:
        #     db.insert_trivia_game(self)
        from Classes.question_class import get_questions
        self.questions = get_questions(type_of_trivia, self.num_of_questions)


def get_trivia_db():
    return _db

