from discord.ext import commands

class bottest(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  @commands.hybrid_command(name="about", description="About")
  async def test1(self,ctx):
    await ctx.send("heyoooo skylar fans!! I know your excited but the bot is still WIP and will be done soon okiee?? i hope to have fun with yall soon, luv yall :D")

def setup(client):
  return client.add_cog(bottest(client))
