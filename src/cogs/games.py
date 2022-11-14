from selfcord.ext import commands
from random import shuffle, randint

from src.utils import *
from src.core import *

class Games(commands.Cog):
    """
    Minigames to play inside of Discord
    """

    def __init__(self, client: commands.Bot):
        self.client = client
        
    @commands.command()
    async def minesweeper(self, ctx, size: int = 5) -> None:
        """
        Allows you to play minesweeper, in discord!
        """

        """
        await minesweeper(context, field size) -> nothing

        Allows you to play minesweeper, thanks to spoilered messages

        :param context object: Context
        :param size int: Size of the field (max 8, min 2)
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        size = max(min(size, 8), 2)

        bombs = [
            [randint(0, size - 1), 
            randint(0, size - 1)]
            for _ in range(int(size - 1))
        ]

        shuffle(bombs)

        has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]

        message = ''
        for y in range(size):
            for x in range(size):

                tile = f'||{chr(11036)}||'
                if has_bomb(x, y):
                    tile = f'||{chr(128163)}||'

                message += tile
            message += "\n"
        
        await sendmsg(
            ctx,
            message,
            False
        )

async def setup(client):
    await client.add_cog(Games(client))