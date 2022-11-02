# Import the command handler
import lightbulb

ping_plugin = lightbulb.Plugin('ping')
# Register the command to the bot
@ping_plugin.command
# Use the command decorator to convert the function into a command
@lightbulb.command("ping", "checks the bot is alive")
# Define the command type(s) that this command implements
@lightbulb.implements(lightbulb.SlashCommand)
# Define the command's callback. The callback should take a single argument which will be
# an instance of a subclass of lightbulb.context.Context when passed in
async def ping(ctx: lightbulb.Context) -> None:
    # Send a message to the channel the command was used in
    await ctx.respond("Pong!")


def load(bot: lightbulb.BotApp) -> None:
    bot.add_plugin(ping_plugin)
