import random

import constants
from Classes import trivia_game
from api import request_utils

questions_dict = {}


class Question:
    def __init__(self, title: str, answer1: str, answer2: str, answer3: str, answer4: str, correct_answer: int
                 , user_answers=None, created_by="Jimmy the Alcoholic", category="Any"):
        self.correct_answer = correct_answer
        self.answer4 = answer4.replace('"', "").replace("'", "")
        self.answer3 = answer3.replace('"', "").replace("'", "")
        self.answer2 = answer2.replace('"', "").replace("'", "")
        self.answer1 = answer1.replace('"', "").replace("'", "")
        self.title = title.replace('"', "").replace("'", "")
        if user_answers is None:
            self.user_answers = {}
        self.created_by = created_by
        self.category = category
        db = trivia_game.get_trivia_db()
        db.add_question(self)


def get_questions(category, num_of_questions):
    question_list = get_questions_from_category(category)
    if num_of_questions > len(question_list):
        num_of_questions = len(question_list)
    return random.sample(question_list, num_of_questions)


def get_questions_from_category(category):
    question_list = []
    if category == constants.plum_category:
        question_list = questions_dict.get(constants.plum_category)
    elif category == constants.any_category:
        for questions in questions_dict.values():
            question_list += questions
    elif category == constants.geography_category:
        question_list = questions_dict.get(constants.geography_category)
    elif category == constants.computers_category:
        question_list = questions_dict.get(constants.computers_category)
    elif category == constants.politics_category:
        question_list = questions_dict.get(constants.politics_category)
    elif category == constants.general_knowledge_category:
        question_list = questions_dict.get(constants.general_knowledge_category)
    elif category == constants.animals_category:
        question_list = questions_dict.get(constants.animals_category)
    elif category == constants.anime_category:
        question_list = questions_dict.get(constants.anime_category)
    elif category == constants.coop_category:
        question_list = questions_dict.get(constants.coop_category)
    else:
        print(f"failed to find a category for category {category}")
    return question_list


def add_input_to_answers(question: Question, user, user_input: str):
    print(f"Trying to add {user_input} to {user.full_name}'s answers")
    if user_input == "1" or user_input.lower() == "one":
        question.user_answers[user.full_name] = 1
    elif user_input == "2" or user_input.lower() == "two":
        question.user_answers[user.full_name] = 2
    elif user_input == "3" or user_input.lower() == "three":
        question.user_answers[user.full_name] = 3
    elif user_input == "4" or user_input.lower() == "four":
        question.user_answers[user.full_name] = 4


def is_answer_correct(question: Question, answer: int):
    if answer == question.correct_answer:
        return True
    return False


def create_answer_list(answers_dict: dict):
    answer1, answer2, answer3, answer4 = [], [], [], []
    for user, answer in answers_dict.items():
        if answer == 1:
            answer1.append(user)
        elif answer == 2:
            answer2.append(user)
        elif answer == 3:
            answer3.append(user)
        elif answer == 4:
            answer4.append(user)
    return [answer1, answer2, answer3, answer4]


def create_answer_string_list(answers_dict: dict):
    answers_list = create_answer_list(answers_dict)
    res = []
    for answer in answers_list:
        res.append(", ".join(answer))
    return res


def generate_all_questions():
    request_utils.generate_all_questions_from_api()
    generate_plum_questions()
    generate_coop_questions()


def generate_plum_questions():
    plum_questions = [
        Question(
            "What is Noah Seuberts favorite fruit?",
            "Cherries",
            "Eggplants",
            "Plums",
            "Bananas",
            3,
            category="Plum"
        ),
        Question(
            "Plum used to live on this street...",
            "Morning Wood Drive",
            "Rainbow Court",
            "3rd Street",
            "Anchor Ave",
            1,
            category="Plum"
        ),
        Question(
            "Plum created his discord account on this day.",
            "Jan 23rd, 2015",
            "September 25th, 2015",
            "August 25th, 2015",
            "June 23rd, 2015",
            2,
            category="Plum"
        ),
        Question(
            "Where was Hammond born?",
            "Hammond was born to a poor family in the hills of Buckland",
            "Hammond was born by aristocrats in the southern castle of Hammburg",
            "Hammond wasn't born, he was manufactured in a secret laboratory underneath the Great Halls of Burnsworth.",
            "Hammond was born from the druids of the Great Forest.",
            1,
            category="Plum"
        ),
        Question(
            "Plum has how much dog in him?",
            "No dog",
            "A wee bit",
            "He got dog in him",
            "The dog so far in him he bouta bust",
            4,
            category="Plum"
        ),
        Question(
            "Plum is a champion at which of these sports?",
            "Valorant",
            "Bags",
            "Basketball",
            "Plum plays sports?",
            2,
            category="Plum"
        ),
        Question(
            "Who was Hammonds employer?",
            "Hammonds Father",
            "Kartha Bo",
            "Guldor Abarr",
            "Randalf",
            3,
            category="Plum"
        ),
        Question(
            "How did plum puke that one infamous night?",
            "He did not puke, he shat",
            "He pukey in the toilet",
            "He did not he inked",
            "It was sober october",
            3,
            category=constants.plum_category
        ),
        Question(
            "Titty, ass, hands in the air, its a party over here. Shake it for the man of the year, man-man of the year...",
            "man-man of the bounce!",
            "bruh, I see girls everywhere",
            "REEEEEEEEEEEEEEEEEEEEEEEEEEEE",
            "oh shoot my league minimized it",
            4,
            category=constants.plum_category
        ),
        Question(
            "What is Plums IQ?",
            "Below 60",
            "at least 100",
            "over 120 at the very least, possible genius",
            "Never took an IQ Test",
            3,
            category=constants.plum_category
        ),
        Question(
            "What is Plums favorite TV show?",
            "Better Call Saul",
            "Succession",
            "Chernobyl",
            "Game of Thrones",
            1,
            category=constants.plum_category
        ),
        Question(
            "What does Plum really do in Wisconsin?",
            "Eats a shit ton of cheese",
            "Kills animals for fun",
            "Visits his long distance girlfriend Hailey",
            "Goes golfing with the fam",
            2,
            category=constants.plum_category
        )
    ]
    questions_dict["Plum"] = questions_dict.get("Plum", []) + plum_questions


def generate_coop_questions():
    coop_questions = [
        Question(
            "Coop won a chess trophy for his school in what grade?",
            "4th grade",
            "5th grade",
            "6th grade",
            "7th grade",
            2,
            category=constants.coop_category
        ),
        Question(
            "Coop is missing how many teeth (not including wisdom teeth)?",
            "0",
            "1",
            "2",
            "3",
            2,
            category=constants.coop_category
        ),
        Question(
            "Coop was a D1 athlete in which e-sport",
            "Overwatch",
            "World of Warcraft",
            "Hearthstone",
            "League of Legends",
            4,
            category=constants.coop_category
        ),
        Question(
            "Coop got married on what day?",
            "September 18th 2021",
            "September 6th 2021",
            "September 18th 2020",
            "September 6th 2020",
            4,
            category=constants.coop_category
        ),
        Question(
            "Who were coops roomates freshman year of college?",
            "Kenny, Ryan, Matt",
            "Kenny, Ryan",
            "Kenny, Ryan, Avery",
            "Kenny, Ryan, Nathan",
            1,
            category=constants.coop_category
        ),
        Question(
            "When and where did Raevyn get Ash?",
            "July 5th in Washington Iowa",
            "August 11th in Independence Iowa",
            "June 8th in Des Moines Iowa",
            "May 21st in Port Byron Illinois",
            2,
            category=constants.coop_category
        ),
        Question(
            "When was Ash born?",
            "April 23rd, 2021",
            "April 23rd, 2020",
            "June 29th, 2021",
            "June 29th, 2020",
            4,
            category=constants.coop_category
        ),
        Question(
            "When was Alex born?",
            "September 2nd, 1996",
            "September 2nd, 1997",
            "September 25th, 1997",
            "September 27th, 1997",
            3,
            category=constants.coop_category
        ),
        Question(
            "Alex did not play which of these sports in high school?",
            "Swimming",
            "Soccer",
            "Golf",
            "Baseball",
            4,
            category=constants.coop_category
        ),
        Question(
            "Coop did not work at which one of these places?",
            "Phone Repair Shop",
            "Plumbing Shop",
            "Corn Fields",
            "Burger Flipper",
            1,
            category=constants.coop_category
        ),
        Question(
            "Coops grandmothers name is...",
            "Gwendolyn",
            "Agatha",
            "Elaine",
            "Caryl",
            1,
            category=constants.coop_category
        ),
        Question(
            "The last name Cooper stands for what?",
            "Bumblebee",
            "Woodworker",
            "Barrel maker",
            "Farmer",
            4,
            category=constants.coop_category
        ),
        Question(
            "Coop was punched by which discord member at a LAN Party",
            "Joe",
            "Cam",
            "One of the Matts",
            "One of the Noahs",
            2,
            category=constants.coop_category
        ),
        Question(
            "Which of these drugs has coop not taken?",
            "Adderall",
            "Cocaine",
            "Hydrocodone",
            "Xanax",
            4,
            category=constants.coop_category
        ),
        Question(
            "What does coop do when he has a hang over?",
            "Drink lots of gatorade",
            "Coop does not get hangovers",
            "Takes several showers",
            "Eats burrito house",
            3,
            category=constants.coop_category
        ),
        Question(
            "What does coop do when he has a hang over?",
            "Drink lots of gatorade",
            "Coop does not get hangovers",
            "Takes several showers",
            "Eats burrito house",
            3,
            category=constants.coop_category
        ),
        Question(
            "Coop got in trouble for drinking where?",
            "A dorm room",
            "In class",
            "Jack Foardes basement",
            "Noah Hummels bathroom",
            1,
            category=constants.coop_category
        )
    ]
    questions_dict[constants.coop_category] = questions_dict.get(constants.coop_category, []) + coop_questions
