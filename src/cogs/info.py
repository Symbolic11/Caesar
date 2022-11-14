from selfcord.ext import commands

from src.utils import *
from src.core import *

class Info(commands.Cog):
    """
    Bot information
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(aliases=['latency'])
    async def ping(self, ctx) -> None:
        """
        Checks the bot latency
        """

        """
        await ping(context) -> nothing

        Checks the latency

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        latency = round(self.client.latency * 1000)

        await sendmsg(
            ctx,
            f'**Ping**: `{str(latency)} ms`',
            True
        )
    
    @commands.command()
    async def uptime(self, ctx) -> None:
        """
        Returns the bots uptime
        """

        """
        await uptime(context) -> nothing

        Returns the bots uptime

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            f'**Uptime**: `{str(get_time(Core.start_time))}`',
            True
        )
    
    @commands.command()
    async def contime(self, ctx) -> None:
        """
        Returns the bots connection time
        """

        """
        await contime(context) -> nothing

        Returns the bots connected time

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            f'**Connected**: `{str(get_time(Core.connect_time))}`',
            True
        )
    
    @commands.command()
    async def info(self, ctx) -> None:
        """
        Shows general information about the bot
        """

        """
        await contime(context) -> nothing

        Shows general information about the bot

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        latency = round(self.client.latency * 1000)
        msg = (
            '**Repository**: `https://github.com/sym-p1337/Caesar`'
            f'\n**Author**: `Sym-p1337`'
            f'\n**Ping**: `{str(latency)} ms`'
            f'\n**Uptime**: `{str(get_time(Core.start_time))}`'
            f'\n**Connected**: `{str(get_time(Core.connect_time))}`'
            f'\n**Extensions loaded**: `{str(len(self.client.extensions))}`'
        )

        await sendmsg(
            ctx,
            msg,
            True
        )

async def setup(client):
    await client.add_cog(Info(client))