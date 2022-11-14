import asyncio

from selfcord.ext import commands
from random import choice, uniform, shuffle

from src.utils import *

# TODO: research dank memers captcha system
class Automation(commands.Cog):
    """
    Bot farmers
    """

    def __init__(self, client: commands.Bot):
        self.client = client

        self.dankmemer_id = 270904126974590976
        self.mudae_id = 432610292342587392
        self.reaction_emoji = ':nerd:' # 🤓

        # used for calculating per-day gifts/bonuses
        self.current_day = ''
        self.last_day = ''

        # toggle system
        self.dank_memer_enabled = False
        self.mee6_enabled = False
    
    async def run_slash(
        self, 
        channel, 
        command: str, 
        expected_id: int | None = None,
        wait_for: bool = False
        ) -> tuple:
        """
        await run_slash(channel, command, expected id, wait for) -> (status, response message)

        Runs the given slash command

        :param channel Optional[Union[.abc.GuildChannel, .Thread, .abc.PrivateChannel]]: Channel object
        :param command str: Slash command to execute
        :param expected_id int or None: ID of the expected message author
        :param wait_for bool: Wether to return the response of the bot (will wait an additional 5 sec)
        :returns tuple: (Status, response message)
        """

        def check(msg):
            return (msg.channel.id == channel.id
                and expected_id == msg.author.id)

        async for cmd in channel.slash_commands(query=command):
            if cmd.name.lower() == command.lower():
                try:
                    await cmd() # call the slash command

                    if wait_for:
                        try:
                            response = await self.client.wait_for(
                                'message', 
                                check=check,
                                timeout=5
                            )

                            return True, response
                        except Exception:
                            return True, None

                    return True, None
                    
                except Exception:
                    return False, None

        return False, None

    @commands.command(aliases=['mee6bot', 'automee6'])
    async def mee6(self, ctx) -> None:
        """
        MEE6 level up bot
        """

        """
        await mee6(context) -> nothing

        MEE6 level up bot

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        if self.mee6_enabled:
            self.mee6_enabled = False
            await sendmsg(ctx, 'MEE6 automation disabled!')

        else:
            self.mee6_enabled = True
            await sendmsg(ctx, 'MEE6 automation enabled!')
        
        chan = ctx.message.channel
        while self.mee6_enabled:
            
            await chan.send(
                await didyouknow(), 
                delete_after=uniform(1, 3)
            )

            await asyncio.sleep(uniform(10, 20))
    
    @commands.command(aliases=['dankmemerbot', 'autodankmemer'])
    async def dankmemer(self, ctx) -> None:
        """
        Dank memer automation
        """

        """
        await dankmemer(context) -> nothing

        Dank memer automation

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if self.dank_memer_enabled:
            self.dank_memer_enabled = False
            await sendmsg(ctx, 'Dank memer automation disabled!')

        else:
            self.dank_memer_enabled = True
            await sendmsg(ctx, 'Dank memer automation enabled!')

        while self.dank_memer_enabled:
            # (command, pick a random opt?)
            commands = [
                ('hunt', False),
                ('beg', False),
                ('fish', False),
                ('dig', False),
                ('crime', True),
                ('postmemes', True),
                ('trivia', True),
                ('search', True)
            ]

            # some random messages to bypass dank-memers anti-bot system
            bypass = [
                await didyouknow(),
                await didyouknow(),
                'man, this shit is boring',
                'bonk!',
                'dank memer SUUUCKS',
                'caesar rocks',
                'i love hotdogs',
                'i love pizza',
                'i use arch btw',
                'goofy ahh bot'
            ]

            # shuffle the lists
            shuffle(commands)
            shuffle(bypass)

            for cmd in commands:
                cmd_str, pick_opt = cmd

                await asyncio.sleep(uniform(3, 12))

                status, msg = await self.run_slash(
                    ctx.channel, 
                    cmd_str, 
                    self.dankmemer_id,
                    pick_opt, 
                )

                if status and msg:
                    # pick a random button and click it
                    button = choice(choice(msg.components).children)
                    await button.click()

                # 30% chance of sending a false msg to trick the antibot system
                if randint(1, 10) <= 3:
                    await ctx.send(choice(bypass))

                    await asyncio.sleep(uniform(0, 1))
            
            # now, there is a 50% chance we will deposit all our money in the bank to keep it safe
            if randint(1, 2) == 1:
                await self.run_slash(
                    ctx.channel, 
                    'deposit max'
                )

            await asyncio.sleep(uniform(10, 25))
    
async def setup(client):
    await client.add_cog(Automation(client))