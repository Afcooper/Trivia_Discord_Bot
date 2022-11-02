import random
import requests
import html
import constants
from Classes import question_class


def create_question_list_from_api_response(api_url, category):
    response = requests.get(api_url)
    response_dict = response.json()['results']
    question_list = []
    for question in response_dict:
        title = question.get("question")
        correct_answer = question.get('correct_answer')
        answers = question.get("incorrect_answers")
        answers.append(correct_answer)
        random.shuffle(answers)
        correct_answer_index = answers.index(correct_answer) + 1
        question_list.append(
            question_class.Question(
                html.unescape(title),
                html.unescape(answers[0]),
                html.unescape(answers[1]),
                html.unescape(answers[2]),
                html.unescape(answers[3]),
                correct_answer_index,
                category=category
            )
        )
    return question_list


def generate_all_questions_from_api():
    question_class.questions_dict[constants.anime_category] = create_question_list_from_api_response(
        constants.anime_api_url, constants.anime_category)
    question_class.questions_dict[constants.animals_category] = create_question_list_from_api_response(
        constants.animal_api_url, constants.animals_category)
    question_class.questions_dict[constants.politics_category] = create_question_list_from_api_response(
        constants.politics_api_url, constants.politics_category)
    question_class.questions_dict[constants.computers_category] = create_question_list_from_api_response(
        constants.computers_api_url, constants.computers_category)
    question_class.questions_dict[constants.geography_category] = create_question_list_from_api_response(
        constants.geography_api_url, constants.geography_category)
    question_class.questions_dict[constants.general_knowledge_category] = create_question_list_from_api_response(
        constants.general_knowledge_api_url, constants.general_knowledge_category)


# if __name__ == "__main__":
    # get_api_trivia_questions()