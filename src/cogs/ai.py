import replicate, os

from selfcord.ext import commands
from random import choice

from src.utils import *
from src.config import *

class AI(commands.Cog):
    """
    Contains everything related to robots, artificial intelligence and hamsters
    """

    def __init__(self, client: commands.Bot):
        self.client = client

        # set env key  
        if type(config.apikeys['replicate']) == list:
            apikey = choice(config.apikeys['replicate'])

        else:
            apikey = config.apikeys['replicate'] 

        os.environ['REPLICATE_API_TOKEN'] = apikey

        self._stable = replicate.models.get('stability-ai/stable-diffusion')
        self._waifu = replicate.models.get('cjwbw/waifu-diffusion')
        self._erlich = replicate.models.get('laion-ai/erlich')
        self._text2img = replicate.models.get('pixray/text2image')
        self._swinir = replicate.models.get('jingyunliang/swinir')
    
    @commands.command(aliases=['ai_swinir', 'ai_upscale'])
    async def upscale(self, ctx) -> None:
        """
        Upscales the given image, can be very slow depending on the image
        """

        """
        await upscale(context) -> nothing

        Upscales the first image in the attachment(s)

        :param ctx context: Context
        :returns None: Nothing
        """

        url = None
        if len(ctx.message.attachments) != 0:
            attachment = ctx.message.attachments[0]

            # allowed file extensions
            if attachment.filename.endswith(".jpg") \
            or attachment.filename.endswith(".jpeg") \
            or attachment.filename.endswith(".png"):
                url = attachment.url
            
        if not url:
            await sendmsg(ctx, '**Error**: `Please add an image`')
            return

        resp = await async_run(
            self._swinir.predict, 
            image=url
        )

        await sendmsg(
            ctx,
            '',
            delete_after=False,
            img=resp
        )
    
    @commands.command(aliases=['ai_stable', 'ai_stablediffusion'])
    async def stablediffusion(self, ctx, *, prompt) -> None:
        """
        Creates art from your prompt using Stable Diffusion, can take a bit
        """

        """
        await stablediffusion(context, prompt) -> nothing

        Creates AI generated art from your prompt, using Stable Diffusion

        :param ctx object: Context
        :param prompt str: Prompt to give to the model
        :returns None: Nothing
        """

        resp = await async_run(
            self._stable.predict, 
            prompt=prompt
        )

        await sendmsg(
            ctx,
            '',
            delete_after=False,
            img=resp[0]
        )
    
    @commands.command(aliases=['ai_waifu', 'ai_makewaifu'])
    async def waifudiffusion(self, ctx, *, prompt) -> None:
        """
        Creates waifus using Waifu-Diffusion, can take a bit
        """

        """
        await waifudiffusion(context, prompt) -> nothing

        Creates waifus using Waifu-Diffusion

        :param ctx object: Context
        :param prompt str: Prompt to give to the model
        :returns None: Nothing
        """

        resp = await async_run(
            self._waifu.predict, 
            prompt=prompt
        )
        await sendmsg(
            ctx,
            '',
            delete_after=False,
            img=resp[0]
        )
    
    @commands.command(aliases=['ai_erlich', 'ai_makelogo'])
    async def erlich(self, ctx, *, prompt) -> None:
        """
        Creates logos based off your prompts
        """

        """
        await erlich(context, prompt) -> nothing

        Creates logos based off user prompts

        :param ctx object: Context
        :param prompt str: Prompt to give to the model
        :returns None: Nothing
        """

        resp = list(await async_run(
            self._erlich.predict, 
            prompt=prompt
        ))

        await sendmsg(
            ctx,
            '',
            delete_after=False,
            img=choice(resp)
        )

async def setup(client):
    if config.apikeys.get('replicate'):
        await client.add_cog(AI(client))

    else:
        print('\nUnable to load AI cog: missing API key "replicate"\n')