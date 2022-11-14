import aiohttp, re

from selfcord.ext import commands
from PIL import Image
from io import BytesIO
from os.path import exists, join

from src.utils import *
from src.core import *

class Emoji(commands.Cog):
    """
    Emoji stealing, adding and downloading
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    async def clean_name(self, raw) -> str:
        """
        await clean_name(raw string) -> properly cleaned string

        Removes everything but alphanumeric characters, underscores and digits

        :param raw str: Raw string
        :returns str: Cleaned string
        """

        new = ''
        for char in raw:

            if char.isalpha() \
            or char == '_' \
            or char.isdigit():

                new += char
        
        return new
    
    @commands.command(aliases=['downloademoji', 'saveemoji', 'save-emoji'])
    async def download_emoji(self, ctx, emoji: selfcord.Emoji, name=None) -> None:
        """
        Downloads the emoji to the "emojis" folder
        """

        """
        await download_emojis(context, emoji, emoji name) -> nothing

        Downloads the emoji to the "emojis" folder

        :param context object: Context
        :param emoji selfcord.Emoji: Emoji object
        :param name str or None: Emoji name, None to let Caesar decide
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        # simple check to see if the emoji is an actual valid emoji
        try:
            if not emoji.available:
                return await sendmsg(ctx, '**Error**: `Emoji is unavaible`')

        except Exception:
            return await sendmsg(ctx, f'**Error**: `Expected emoji, but got "{emoji}" instead`')
        
        if not name:
            name = emoji.name
        
        try:
            path = join('src', 'emojis', name)
            
            if not exists(path):
                with open(join('src', 'emojis', name), 'wb') as fd:
                    fd.write(await emoji.read())

            else:
                return await sendmsg(ctx, '**Error**: `Image already exists`')

            await sendmsg(
                ctx, 
                (
                    f'<a:{emoji.name}:{emoji.id}>' if emoji.animated else f'<:{emoji.name}:{emoji.id}>'
                    ' downloaded'
                )
            )
            
        except Exception as e:
            await sendmsg(ctx, f'**Error**: `Unable to steal emoji: {str(e).rstrip()}`')
    
    @commands.command(aliases=['stealemoji', 'steal-emoji'])
    async def steal_emoji(self, ctx, emoji: selfcord.Emoji, name=None) -> None:
        """
        Steals the emoji and adds it
        """

        """
        await steal_emoji(context, emoji, emoji name) -> nothing

        Steals the emoji and adds it

        :param context object: Context
        :param emoji selfcord.Emoji: Message containing the emoji
        :param name str or None: Emoji name, None to let Caesar decide
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        # simple check to see if the emoji is an actual valid emoji
        try:
            if not emoji.available:
                return await sendmsg(ctx, '**Error**: `Emoji is unavaible`')

        except Exception:
            return await sendmsg(ctx, f'**Error**: `Expected emoji, but got "{emoji}" instead`')
        
        if not name:
            name = emoji.name
        
        try:
            emoji = await ctx.guild.create_custom_emoji(
                image=await emoji.read(), 
                name=name
            )

            await sendmsg(
                ctx, 
                (
                    f'<a:{emoji.name}:{emoji.id}>' if emoji.animated else f'<:{emoji.name}:{emoji.id}>'
                    ' added'
                )
            )
            
        except Exception as e:
            await sendmsg(ctx, f'**Error**: `Unable to steal emoji: {str(e).rstrip()}`')
    
    @commands.command(aliases=['add-emoji', 'emoji-from-url', 'addemoji'])
    async def add_emoji(self, ctx, link, name=None) -> None:
        """
        Downloads the image from the url and adds it
        """

        """
        await steal_emoji(context, emoji url, emoji name) -> nothing

        Downloads the image from the url and adds it

        :param context object: Context
        :param link str: Message to parse link from
        :param name str or None: Emoji name, None to let Caesar decide
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if not link.startswith('http'):
            return await sendmsg(ctx, f'**Error**: `Expected link, but got "{link}" instead`')
        
        if not link.endswith('.png') and not link.endswith('.jpg') and not link.endswith('.gif'):
            return await sendmsg(ctx, '**Error**: `Image not accepted. Only JPG, PNG and GIF images are supported`')
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(link, allow_redirects=True) as res:
                resp = await res.read()
        
        if len(resp) <= 0 or not resp:
            return await sendmsg(ctx, '**Error**: `Failed to download emoji`')
        
        extension = 'jpg'
        if not name:
            name, extension = link.split('/')[-1].split('.')
        
        im = Image.open(BytesIO(resp))
        if (im.height > 128 or im.width > 128) and im.format in ['PNG', 'JPG']:
            
            # scale down the image so discord doesn't cry
            try:
                im.thumbnail((128, 128), Image.Resampling.LANCZOS)

                ByteIO = io.BytesIO()
                im.save(ByteIO, format=extension.upper())
                resp = ByteIO.getvalue()
            except Exception as e:
                return await sendmsg(ctx, f'**Error**: `Unable to scale down emoji to 128x128: {str(e).rstrip()}`')
        
        im.close() # close the image

        try:
            emoji = await ctx.guild.create_custom_emoji(
                image=resp, 
                name=await self.clean_name(name)
            )

            await sendmsg(
                ctx, 
                (
                    f'<a:{emoji.name}:{emoji.id}>' if emoji.animated else f'<:{emoji.name}:{emoji.id}>'
                    ' added'
                )
            )
            
        except Exception as e:
            await sendmsg(ctx, f'**Error**: `Unable to add emoji: {str(e).rstrip()}`')

async def setup(client):
    await client.add_cog(Emoji(client))