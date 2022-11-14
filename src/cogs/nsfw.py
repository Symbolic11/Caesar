from selfcord.ext import commands
from random import choice, shuffle

from src.utils import * 

class Nsfw(commands.Cog):
    """
    Lots of boobies
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    async def meme_api(self, tag) -> str:
        """
        await meme_api(tag) -> url

        Even tho the name has meme in it, it supplies more than just memes

        :param tag str: The tag
        :returns str: The image url
        """

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://meme-api.herokuapp.com/gimme/{tag}") as res:
                res = await res.json()
        
        return res['url']
    
    async def rule34(self, tag) -> str:
        """
        await rule34(tag) -> url

        Lookups the given tag(s) on rule34.xxx

        :param tag str: The tag
        :returns str: The image url
        """

        tag = tag.replace(' ', '+').replace(',', '')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.rule34.xxx/index.php?page=dapi&s=post&q=index&limit=15&json=1&tags={tag}") as res:
                if res.status != 200:
                    print(f'Could not fetch image from rule34: {res.status}')
                    return ''

                res = await res.json()
        
        shuffle(res)
        return choice(res)['file_url']
    
    async def gelbooru(self, tag) -> str:
        """
        await gelbooru(tag) -> url

        Lookups the given tag on gelbooru.com

        :param tag str: The tag
        :returns str: The image url
        """

        tag = tag.replace(' ', '+').replace(',', '')
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://gelbooru.com/index.php?page=dapi&s=post&q=index&limit=15&json=1&tags={tag}") as res:
                res = await res.json()
        
        posts = res['post']
        shuffle(posts)

        return choice(posts)['file_url']
    
    async def nekobot(self, imgtype: str) -> str:
        """
        await nekobot(image type) -> url

        Builds the nekobot url from the given image type

        :param imgtype str: Image type
        :returns str: The url, empty string incase of errors
        """

        if not imgtype in [
            'hass', 
            'hmidriff', 
            'pgif', 
            '4k', 
            'hentai', 
            'hneko',  
            'hkitsune', 
            'kemonomimi', 
            'anal', 
            'hanal', 
            'gonewild', 
            'kanna', 
            'ass', 
            'pussy', 
            'thigh', 
            'hthigh',
            'paizuri', 
            'tentacle', 
            'boobs', 
            'hboobs', 
            'yaoi']:
            return ''
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/image?type={imgtype}") as res:
                if res.status != 200:
                    return ''

                res = await res.json()
        
        return res.get('message')
    
    @commands.command(aliases=['pgif'])
    async def porngif(self, ctx) -> None:
        """
        Sends a random porn gif
        """

        """
        await porngif(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('pgif'),
            False
        )
    
    @commands.command(aliases=['hgif'])
    async def hentaigif(self, ctx) -> None:
        """
        Sends a random hentai gif
        """

        """
        await hentaigif(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hentai'),
            False
        )
    
    @commands.command(aliases=['4k'])
    async def fourk(self, ctx) -> None:
        """
        Sends a random 4K porn gif
        """

        """
        await fourk(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('4k'),
            False
        )
    
    @commands.command(aliases=['hanal'])
    async def hentaianal(self, ctx) -> None:
        """
        Sends random anal hentai
        """

        """
        await hentaianal(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hanal'),
            False
        )
    
    @commands.command()
    async def anal(self, ctx) -> None:
        """
        Sends random anal
        """

        """
        await anal(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('anal'),
            False
        )
    
    @commands.command(aliases=['hneko'])
    async def hentaineko(self, ctx) -> None:
        """
        Sends random neko hentai
        """

        """
        await hentaineko(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hneko'),
            False
        )
    
    @commands.command(aliases=['hkitsune'])
    async def hentaikitsune(self, ctx) -> None:
        """
        Sends random kitsune hentai
        """

        """
        await hentaikitsune(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hkitsune'),
            False
        )
    
    @commands.command()
    async def ass(self, ctx) -> None:
        """
        Sends random a$$
        """

        """
        await ass(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('ass'),
            False
        )
    
    @commands.command(aliases=['hass'])
    async def hentaiass(self, ctx) -> None:
        """
        Sends random ass hentai
        """

        """
        await hentaiass(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hass'),
            False
        )
    
    @commands.command()
    async def boobs(self, ctx) -> None:
        """
        Sends boobas
        """

        """
        await boobs(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('boobs'),
            False
        )
    
    @commands.command(aliases=['hboobs'])
    async def hentaiboobs(self, ctx) -> None:
        """
        Sends hentai boobas
        """

        """
        await hentaiboobs(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hboobs'),
            False
        )
    
    @commands.command()
    async def tentacle(self, ctx) -> None:
        """
        Yeah, no.
        """

        """
        await tentacle(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('tentacle'),
            False
        )
    
    @commands.command(aliases=['thighs'])
    async def thigh(self, ctx) -> None:
        """
        Sends thights, yum
        """

        """
        await thigh(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('thigh'),
            False
        )
    
    @commands.command(aliases=['hthighs', 'hthigh'])
    async def hentaithigh(self, ctx) -> None:
        """
        Sends 2D thighs, yum
        """

        """
        await hentaithigh(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hthigh'),
            False
        )
    
    @commands.command(aliases=['hmidriff'])
    async def hentaimidriff(self, ctx) -> None:
        """
        Sends 2D midriff images
        """

        """
        await hentaimidriff(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('hmidriff'),
            False
        )
    
    @commands.command()
    async def gonewild(self, ctx) -> None:
        """
        Gone wild (idk what that means)
        """

        """
        await gonewild(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('gonewild'),
            False
        )
    
    @commands.command()
    async def pussy(self, ctx) -> None:
        """
        Sends cats (no jk its porn)
        """

        """
        await pussy(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.nekobot('pussy'),
            False
        )
    
    @commands.command()
    async def ecchi(self, ctx) -> None:
        """
        Sends ecchi images
        """

        """
        await ecchi(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.meme_api('ecchi'),
            False
        )
    
    @commands.command()
    async def sideboob(self, ctx) -> None:
        """
        Sideboob view
        """

        """
        await sideboob(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.meme_api('sideoppai'),
            False
        )
    
    @commands.command()
    async def ahegao(self, ctx) -> None:
        """
        Random ahegao
        """

        """
        await ahegao(context) -> nothing

        Ambatakum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await self.meme_api('ahegao'),
            False
        )
    
    @commands.command(aliases=['gelbooru'])
    async def gelboorulookup(self, ctx, *, tags) -> None:
        """
        Gelbooru.com lookup
        """

        """
        await gelboorulookup(context, tags) -> nothing

        Ambatakum

        :param ctx object: Context
        :param tags str: Tags to look for
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await sendmsg(
            ctx,
            await self.gelbooru(tags),
            False
        )
    
    @commands.command(aliases=['rule34'])
    async def r34(self, ctx, *, tags) -> None:
        """
        Rule34.xxx lookup
        """

        """
        await r34(context, tags) -> nothing

        Ambatakum

        :param ctx object: Context
        :param tags str: Tags to look for
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await sendmsg(
            ctx,
            await self.rule34(tags),
            False
        )
        
async def setup(client):
    await client.add_cog(Nsfw(client))