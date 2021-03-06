import numexpr
from discord.ext import commands


class Math:
    """
    Commands for simple math functions
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True, no_pm=False)
    async def math(self, ctx, *, msg: str):
        await self.bot.send_typing(ctx.message.channel)
        try:
            result = numexpr.evaluate(msg).item()
            await self.bot.say(
                "```py\n>>>\t{}\n<<<\t{}\n```".format(msg, result)
            )
        except Exception as e:
            await self.bot.say(
                "```py\n>>>\t{}\n<<<\t{}\n```".format(msg, e)
            )

    @commands.command(pass_context=True, no_pm=False)
    async def roll_dice(self, ctx, *, msg: str):
        pass
