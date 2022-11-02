import datetime
import hikari
from Classes.trivia_game import TriviaGame
from Classes.question_class import Question, create_answer_string_list


def create_question_embed(question: Question, question_complete=False):
    answers_list = []
    if question_complete:
        answers_list = create_answer_string_list(question.user_answers)
    return (
        hikari.Embed(
            title=f'{question.title}',
            colour=0x3B9DFF,
            timestamp=datetime.datetime.now().astimezone(),
        )
        .add_field(
            name=f"1. {question.answer1} {'- Correct answer' if question_complete and question.correct_answer==1 else ''} {answers_list[0] if question_complete else ''}",
            value='\u200b'
        )
        .add_field(
            name=f"2. {question.answer2} {'- Correct answer' if question_complete and question.correct_answer==2 else ''} {answers_list[1] if question_complete else ''}",
            value='\u200b'
        )
        .add_field(
            name=f"3. {question.answer3} {'- Correct answer' if question_complete and question.correct_answer==3 else ''} {answers_list[2] if question_complete else ''}",
            value='\u200b'
        )
        .add_field(
            name=f"4. {question.answer4} {'- Correct answer' if question_complete and question.correct_answer==4 else ''} {answers_list[3] if question_complete else ''}",
            value='\u200b'
        )
    )


def create_results_embed(results: dict, trivia_game: TriviaGame):
    max_winners = 10
    embed_title = f"The results for {trivia_game.type_of_trivia} trivia are in! \nHere are the winners...\n"
    embed_description = ""
    sorted_results = sorted(results.items(), key=lambda x: x[1]['points'], reverse=True)
    print(f"Displaying results {results} for trivia game.")
    for i, results_tuple in enumerate(sorted_results):
        if i >= max_winners:
            break
        points = results_tuple[1]['points']
        questions_correct = results_tuple[1]['questions_correct']
        questions_answered = results_tuple[1]['questions_answered']
        embed_description += f"{i+1}. {results_tuple[0]} received a score of {questions_correct} out of {questions_answered} questions correct, earning {points} points.\n"
    return (
        hikari.Embed(
            title=embed_title,
            description=embed_description,
            colour=0x3B9DFF,
            timestamp=datetime.datetime.now().astimezone(),
        )
    )


def create_trivia_game_embed(trivia_game: TriviaGame):
    return (
        hikari.Embed(
            title=f'Starting a trivia game with the category {trivia_game.type_of_trivia}',
            description=f"To answer a question type in the chat the number associated with your answer (e.g. '1', '2', "
                        f"'3', '4').\n If you struggle to do this you probably struggle with everything else in your"
                        f" pathetic life and trivia is not recommended for you!\n I will take your last answer given if"
                        f"you wish to change it. \n You have to answer "
                        f"{trivia_game.num_of_questions} question with {trivia_game.seconds_per_question} seconds for "
                        f"each question.",
            colour=0x3B9DFF,
            timestamp=datetime.datetime.now().astimezone(),
        )
    )
