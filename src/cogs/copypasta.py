from selfcord.ext import commands
from urllib.parse import unquote
from random import choice, shuffle

from src.utils import *

class Copypasta(commands.Cog):
    """
    Cursed, blessed and blursed copypastas
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command()
    async def copypasta(self, ctx) -> None:
        """
        Sends a random copypasta from r/copypastas
        """

        """
        await copypasta(conext) -> nothing

        Sends a randomly chosen copypasta from r/copypastas

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://old.reddit.com/r/copypasta.json') as res:
                resp = await res.json()

        async def pick():
            messages = resp['data']['children'][1:] # skip the first message since it's a pinned mod message

            shuffle(messages)
            message = choice(messages)

            # clean the message
            return unquote(
                message['data']['selftext'].strip()
                    .replace(r"&amp;#x200B;","")
                    .replace("\n"," ")
                    .replace("      ","")
            )

        message = await pick()
        while len(message) > 2000: # prevents messages longer than 2000 characters
            message = await pick()

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content=message)
    
    @commands.command()
    async def whoasked(self, ctx) -> None:
        """
        Who asked? No one
        """

        """
        await whoasked(context) -> nothing

        Who asked?

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content="ɴᴏᴡ ᴘʟᴀʏɪɴɢ: Who asked (Feat: No one)\n  ───────────⚪─────────────\n◄◄⠀▐▐ ⠀►► 5:12/ 7:56 ───○ 🔊⠀ ᴴᴰ ⚙️")

    @commands.command()
    async def snap(self, ctx) -> None:
        """
        Snapchat
        """

        """
        await snap(context) -> nothing

        Snapchat? No i want my neck snap

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content="I 👆 don't 🙅‍♂️ want your snapchat 👻 I want 👅 💦 you 😍 to snap 🙇‍♂️ my neck 💀🤠👌")
    
    @commands.command()
    async def britishavatar(self, ctx) -> None:
        """
        Avatar, but bri'ish
        """

        """
        await britishavatar(context) -> nothing

        Bri'ish avatar

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content="wo'ah, earf, birming'am, fish n' chips… long ago, the fou' nations live togedah in ah'mony. then ev'ryfing changed when the IRA attacked…. only the avatah, mastah of all fou' elements could stop 'em but when the queen needed ‘im most, ‘e vanished. 100 yea's passed and me bruv and i found the new avatah. a fish n' chips bendah named aang. although ‘is chipbendin' skills ah great, ‘e still ‘as a lo' to lea'n ‘fore ‘e's ready to save anyone m8.")
    
    @commands.command(name='okand?')
    async def okayand(self, ctx) -> None:
        """
        Ok and?
        """

        """
        await okand(context) -> nothing

        Ok and?

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content='"ok and?" and? and what? suck my dick? what the fuck do you want me to say? i already got my point across to your pubic brain and here you are acting like a smug smartass in a miserable way to be funny and trying to win an argument against me cause you won\'t accept fair criticism')
    
    @commands.command()
    async def based(self, ctx) -> None:
        """
        Very based and redpilled yes
        """

        """
        await based(context) -> nothing

        Sends a very based copypasta

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content='Based on fucking what? BASED ON FUCKING WHAT? You fucking cunt, you motherfucker. All I read is "based based based cringe cringe based", can\'t you fucking come up with anything else? It feels as if I\'m talking to people with fucking dementia or something and they keep repeating the same fucking words on loop. BASED ON FUCKING WHAT??? THE BIBLE? THE OXFORD DICTIONARY? MY HAIRY ASSHOLE? OH my God just shut the fuck up it\'s like you can\'t form a coherent sentence without using one of these saturated, retarded words that lost all meaning overtime. "BASED BASED BASED CRINGE CRINGE WOKE REDPILL CRINGE WOKE GO FUCK YOURSELF YOU LITTLE BITCH YOU CUNT YOU FUCking asshole you bitch you cunt little shit Based? Based on what? On your dick? Please shut the fuck up and use words properly you fuckin troglodyte, do you think God gave us a freedom of speech just to spew random words that have no meaning that doesn\'t even correlate to the topic of the conversation? Like please you always complain about why no one talks to you or no one expresses their opinions on you because you\'re always spewing random shit like poggers based cringe and when you try to explain what it is and you just say that it\'s funny like what? What the fuck is funny about that do you think you\'ll just become a stand-up comedian that will get a standing ovation just because you said "cum" on the stage? HELL NO YOU FUCKIN IDIOT, so please shut the fuck up and use words properly you dumb bitch')

async def setup(client):
    await client.add_cog(Copypasta(client))