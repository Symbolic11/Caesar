import re, aiohttp

from selfcord.ext import commands

from src.utils import *
from src.core import *
from src.config import *

# TODO: add more
giveaway_bots = {
    294882584201003009: {
        'emoji': '🎉'
    }, # GiveawayBot

    582537632991543307: {
        'emoji': '🎉'
    }, # Santa Lunar

    396464677032427530: {
        'emoji': '🎉'
    }, # Giveaway

    239631525350604801: {
        'emoji': '🎁'
    }, # Pancake

    530082442967646230: {
        'emoji': '🎉'
    }, # Giveaway Boat
}

async def is_nitro(msg) -> bool:
    """
    is_nitro(message) -> status

    Checks if the given string matches a discord nitro invite code

    :param msg selfcord.Message: Message to check
    :returns bool: True if it's a valid code, False if not
    """

    body = msg.content
    return (
        'discordapp.com/gifts/' in body or 
        'discord.gift/' in body or 
        'discord.com/gifts/' in body
    )

async def is_giveaway(msg) -> bool:
    """
    is_giveaway(message) -> status

    Checks if the given message is from an invite bot

    :param msg selfcord.Message: Message to check
    :returns bool: True if it's a giveaway, False if not
    """

    return 'giveaway' in msg.content.lower() and msg.author.id in giveaway_bots

async def is_slotbot(msg) -> bool:
    """
    is_slotbot(message) -> status

    Checks if the given message is a message from slotbot

    :param msg selfcord.Message: Message to check
    :returns bool: True if it's a giveaway, False if not
    """

    return 'someone just dropped' in msg.content.lower() and msg.author.id == 346353957029019648

class Snipers(commands.Cog):
    """
    Nitro, giveaway and slotbot snipers
    """

    def __init__(self, client: commands.Bot):
        self.client = client

        self.nitrosniper_toggle = config.nitrosniper_toggle
        self.nitrosniper_stealth = config.nitrosniper_stealth
        self.giveawaysniper_toggle = config.giveawaysniper_toggle
        self.giveawaysniper_stealth = config.giveawaysniper_stealth
        self.slotbotsniper_toggle = config.slotbotsniper_toggle
        self.slotbotsniper_stealth = config.slotbotsniper_stealth
        self.nitrocode_regex = re.compile(r'(discord\.com/gifts|discord\.gift|discordapp\.com/gifts)/(\w+)')
        self.paymentid_regex = re.compile(r'("id": ")([0-9]+)"')
        self.id_history = []

    async def snipe(self, message) -> None:
        """
        await snipe(message) -> nothing

        Sniper function, snipers nitro, giveaways and slotbot drops

        :param message selfcord.Message: Message object
        :returns None: Nothing
        """

        if await is_nitro(message) and self.nitrosniper_toggle:
            codes = self.nitrocode_regex.findall(message.content)

            for code in codes:
                code = code[1]

                if not len(code) in [16, 24]: # check for valid code length
                    continue

                async with aiohttp.ClientSession(headers={
                    'Authorization': config.token,
                    'Content-Type': 'application/json'
                }) as cs:

                    if self.nitrosniper_stealth:
                        await asyncio.sleep(uniform(0, 1)) # slight delay, adds a bit of stealth at the cost of getting the gift faster

                    async with cs.post(
                        f"https://discordapp.com/api/v9/entitlements/gift-codes/{code}/redeem", 
                        data=json.dumps({
                                'channel_id': message.channel.id,
                                'payment_source_id': await self.get_payment_id(cs)
                            })
                        ) as res:

                        if res.status == 200:
                            print(f'\n> Claimed nitro code in {message.guild}')
            
        # TODO: implement embed giveaway joining
        if await is_giveaway(message) and self.giveawaysniper_toggle:

            if self.giveawaysniper_stealth:
                await asyncio.sleep(uniform(1, 2))

            await message.add_reaction(
                giveaway_bots[message.author.id]['emoji']
            )

            print(f'\n> Joined giveaway in {message.guild}')

        if message.author.id in giveaway_bots \
        and (f'congratulations <@{self.client.user.id}>' in message.content.lower() \
            or f'<@{self.client.user.id}> won' in message.content):

            print(f'\n> Won giveaway in "{message.guild}"')
        
        if await is_slotbot(message) and self.slotbotsniper_toggle:

            if self.slotbotsniper_stealth:
                await asyncio.sleep(uniform(0, 1))
            
            try:
                await message.channel.send('~grab')

                print(f'\n> Grabbed slotbot drop in {message.guild}')
            except Exception:
                pass
    
    async def get_payment_id(self, cs) -> str | None:
        """
        await get_payment_id(client session) -> payment id or None

        Tries to grab the payment ID

        :param cs aiohttp.ClientSession: AioHTTP session
        :returns str or None: None of payment id was not found, else the payment id is returned
        """

        async with cs.get('https://discord.com/api/v9/users/@me/billing/payment-sources') as res:
            resp = await res.text()
        
        payment_id = self.paymentid_regex.findall(resp)
        if not payment_id:
            return None
        
        if len(payment_id) > 1:
            payment_id = payment_id[2]
        
        return str(payment_id)
    
    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after) -> None:
        """
        await on_message_edit(message before edit, message after edit) -> nothing

        Event that runs when a message is edited

        :param message_before selfcord.Message: Message object, before edited
        :param message_after selfcord.Message: Message object, after edited
        :returns None: Nothing
        """
        
        async for message in message_after.channel.history(limit=1):

            # prevents duplicate messages and the user triggering the sniper
            if message.id in self.id_history \
            or message.author.id == self.client.user.id:
                continue

            if len(self.id_history) >= 5: # clean the list of messages up
                self.id_history = []

            self.id_history.append(message.id)

            await self.snipe(message)

    @commands.Cog.listener()
    async def on_message(self, message) -> None:
        """
        await on_message(message) -> nothing

        Event that runs when a message is sent

        :param message selfcord.Message: Message object
        :returns None: Nothing
        """

        async for message in message.channel.history(limit=1):
            # prevents duplicate messages and the user triggering the sniper
            if message.id in self.id_history \
            or message.author.id == self.client.user.id:
                continue

            if len(self.id_history) >= 5: # clean the list of messages up
                self.id_history = []

            self.id_history.append(message.id)

            await self.snipe(message)
    
    @commands.command()
    async def nitrosniper(self, ctx, *, stealth: str = 'y') -> None:
        """
        Enables/disables the nitro sniper
        """

        """
        await nitrosniper(context,  enable stealth mode?) -> nothing

        Enables/disables the nitro sniper

        :param ctx object: Context
        :param stealth str: Enable stealth mode
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if not self.nitrosniper_toggle:
            self.nitrosniper_toggle = True
            config.nitrosniper_toggle = True    
        else:
            self.nitrosniper_toggle = False
            config.nitrosniper_toggle = False
        
        self.nitrosniper_stealth = stealth.lower().startswith('y') or stealth.lower() in ['enable', 'on']
        
        save_config()

        await sendmsg(
            ctx,
            (
                f'**Nitro sniper**: `{"disabled" if not self.nitrosniper_toggle else "enabled"}`\n'
                f'**Stealth mode**: `{"yes" if self.nitrosniper_stealth else "no"}`'
            ),
            True
        )
    
    @commands.command()
    async def giveawaysniper(self, ctx, stealth: str = 'y') -> None:
        """
        Enables/disables the giveaway sniper
        """

        """
        await giveawaysniper(context, enable stealth mode?) -> nothing

        Enables/disables the giveaway sniper

        :param ctx object: Context
        :param stealth str: Enable stealth mode
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if not self.giveawaysniper_toggle:
            self.giveawaysniper_toggle = True     
            config.giveawaysniper_toggle = True   
        else:
            self.giveawaysniper_toggle = False
            config.giveawaysniper_toggle = False
        
        self.giveawaysniper_stealth = stealth.lower().startswith('y') or stealth.lower() in ['enable', 'on']
        
        save_config()

        await sendmsg(
            ctx,
            (
                f'**Giveaway sniper**: `{"enabled" if self.giveawaysniper_toggle else "disabled"}`\n'
                f'**Stealth mode**: `{"yes" if self.giveawaysniper_stealth else "no"}`'
            ),
            True
        )
    
    @commands.command()
    async def slotbotsniper(self, ctx, stealth: str = 'y') -> None:
        """
        Enables/disables the slotbot sniper
        """

        """
        await slotbotsniper(context, enable stealth mode?) -> nothing

        Enables/disables the slotbot sniper

        :param ctx object: Context
        :param stealth str: Enable stealth mode
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if not self.slotbotsniper_toggle:
            self.slotbotsniper_toggle = True     
            config.slotbotsniper_toggle = True   
        else:
            self.slotbotsniper_toggle = False
            config.slotbotsniper_toggle = False
        
        self.slotbotsniper_stealth = stealth.lower().startswith('y') or stealth.lower() in ['enable', 'on']
        
        save_config()

        await sendmsg(
            ctx,
            (
                f'**Slotbot sniper**: `{"enabled" if self.slotbotsniper_toggle else "disabled"}`\n'
                f'**Stealth mode**: `{"yes" if self.slotbotsniper_stealth else "no"}`'
            ),
            True
        )

async def setup(client):
    await client.add_cog(Snipers(client))