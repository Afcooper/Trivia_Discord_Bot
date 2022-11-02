import time

import hikari
import lightbulb
import constants
from Classes import trivia_game
from Classes.question_class import Question, is_answer_correct
from Classes.trivia_game import TriviaGame
from datetime import datetime
from utils import trivia_ui

trivia_plugin = lightbulb.Plugin('trivia')
db = trivia_game.get_trivia_db()
current_question = None
current_trivia_game = None


@trivia_plugin.command
@lightbulb.option(
    'trivia_type', 'Type of trivia you would like to answer.', str, required=True, choices=trivia_game.get_categories()
)
@lightbulb.option(
    'number_of_questions', 'The number of trivia questions you would like to answer.', int, required=False, min_value=1
    , max_value=20, default=5
)
@lightbulb.option(
    'seconds_per_questions', 'The number of trivia questions you would like to answer.', int, required=False
    , min_value=10, max_value=90, default=30
)
@lightbulb.command('trivia_game', 'Creates a game of trivia!')
@lightbulb.implements(lightbulb.SlashCommand)
async def create_trivia_game(ctx: lightbulb.Context):
    global current_trivia_game
    if current_trivia_game is not None:
        return
    try:
        created_by = ctx.author
        created_date = datetime.now()
        trivia_type = ctx.options.trivia_type
        number_of_questions = ctx.options.number_of_questions
        seconds_per_questions = ctx.options.seconds_per_questions
        trivia_game = TriviaGame(trivia_type, created_by, num_of_questions=number_of_questions
                                 , seconds_per_question=seconds_per_questions, created_date=created_date)
        current_trivia_game = trivia_game
        trivia_start_embed = trivia_ui.create_trivia_game_embed(trivia_game)
        await ctx.respond(trivia_start_embed)
        time.sleep(constants.trivia_game_embed_delay)
        print("Creating a game of trivia")
        await start_questions(ctx, trivia_game.questions, trivia_game.seconds_per_question)
        print("Finished the game of trivia")
        results_dict = generate_question_results(trivia_game.questions)
        results_embed = trivia_ui.create_results_embed(results_dict, trivia_game)
        await ctx.respond(results_embed)
        current_trivia_game = None
    except Exception as e:
        print(f"Issue with trivia game : {e}")
        current_trivia_game = None


async def start_question(ctx: lightbulb.Context, question: Question, question_duration):
    global current_question
    try:
        print(f"Starting question {question.title}.")
        embed = trivia_ui.create_question_embed(question)
        await ctx.respond(embed)
        current_question = question
        print(f"Awaiting user responses...")
        time.sleep(question_duration - constants.question_finishing_warning_time)
        await ctx.respond(
            hikari.Embed(
                title=f'Time is almost up... get your answers in now.',
                colour=0x3B9DFF,
                timestamp=datetime.now().astimezone(),
            )
        )
        time.sleep(constants.question_finishing_warning_time)
        print(f"Question can no longer take responses.")
        await ctx.respond(
            hikari.Embed(
                title=f'Times up!',
                colour=0x3B9DFF,
                timestamp=datetime.now().astimezone(),
            )
        )
        time.sleep(constants.question_wait_time_before_cleanup)
        # Cleanup trivia messages
        print(f"Cleaning up question notifications.")
        await ctx.delete_last_response()
        await ctx.delete_last_response()
        # Update question to display correct answer now that it is finished.
        print(f"Editing question to display correct answer.")
        embed = trivia_ui.create_question_embed(question, question_complete=True)
        await ctx.edit_last_response(embed=embed)
        current_question = None
    except Exception as e:
        current_question = None
        print(f"Issue with creating question {e}")


async def start_questions(ctx: lightbulb.Context, questions: list[Question], question_duration):
    for question in questions:
        await start_question(ctx, question, question_duration)


def generate_question_results(questions: list[Question]):
    user_scores = {}
    for question in questions:
        for full_name, answer in question.user_answers.items():
            current_user_scores = user_scores.get(full_name, {'points': 0, 'questions_correct': 0, 'questions_answered': 0})
            current_user_scores['questions_answered'] = current_user_scores['questions_answered'] + 1
            if not is_answer_correct(question, answer):
                user_scores[full_name] = current_user_scores
                continue
            current_user_scores['questions_correct'] = current_user_scores['questions_correct'] + 1
            current_user_scores['points'] = current_user_scores['points'] + constants.default_win_points
            user_scores[full_name] = current_user_scores
    for full_name, details in user_scores.items():
        db.update_user_score(full_name, points=details['points'], questions_correct=details['questions_correct'],
                             questions_answered=details['questions_answered'])
    return user_scores


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(trivia_plugin)
