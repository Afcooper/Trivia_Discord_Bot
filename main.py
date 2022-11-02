import datetime
import os
from dotenv import load_dotenv
import lightbulb
import hikari

from Classes import question_class
from Classes.User import User
from Classes.question_class import add_input_to_answers
from api import request_utils
from commands import trivia

load_dotenv()

# Create our bot.
bot = lightbulb.BotApp(
    os.getenv("DISCORD_TOKEN"),
    prefix='_',
    banner=None,
    intents=hikari.Intents.ALL,
    default_enabled_guilds=int(os.getenv("ENABLED_GUILD_IDS"))
)

# Add our commands to our bot.
bot.load_extensions_from("./commands/", must_exist=True)


@bot.listen()
async def listen_for_question_response(event: hikari.GuildMessageCreateEvent) -> None:
    if event.is_bot or not event.content:
        return
    if trivia.current_question is None:
        return
    user = User(event.author.username, event.author.discriminator, begin_date=datetime.datetime.now())
    add_input_to_answers(trivia.current_question, user, event.content)


if __name__ == '__main__':
    question_class.generate_all_questions()
    bot.run()
