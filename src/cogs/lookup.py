import aiohttp

from selfcord.ext import commands
from bs4 import BeautifulSoup as bs

from src.utils import *
from src.core import *

class Lookup(commands.Cog):
    """
    Lookup github accounts, instagram accounts, youtube channels and more
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    @commands.command(aliases=['lookupip'])
    async def iplookup(self, ctx, *, ip) -> None:
        """
        Looks the specified IP up
        """

        """
        await iplookup(context, ip) -> nothing

        :param ctx object: Context
        :param ip str: IPv4 address to look up
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        if not bool(Regex.ip.match(ip)):
            return await sendmsg(ctx, '**Error**: `Invalid IPv4`')
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'http://ip-api.com/json/{ip}?fields=18079743') as resp:
                res = await resp.json()
        
        if res['status'] == 'fail':
            msg = f'**Errror**: `{res["message"]}`'
        else:
            msg = (
                f'**IP**: `{ip}`\n'
                f'**ISP**: `{res["isp"]}`\n'
                f'**ASN**: `{res["as"]}`\n'
                f'**Organization**: `{res["org"]}`\n'
                f'**Location**: `{res["city"]}, {res["regionName"]}, {res["continent"]}`\n'
                f'**Zip code**: `{res["zip"]}`\n'
                f'**Reverse lookup**: `{res["reverse"]}`\n'
                f'**Latitude & longitude**: `{res["lat"]}, {res["lon"]}`\n'
                f'**Is mobile?**: `{"Yes" if res["mobile"] else "No"}`\n'
                f'**Is proxy?**: `{"Yes" if res["proxy"] else "No"}`\n'
                f'**Is hosting?**: `{"Yes" if res["hosting"] else "No"}`'
            )
        
        await sendmsg(
            ctx,
            msg
        )
    
    @commands.command(aliases=['githubinfo'])
    async def github(self, ctx, *, user) -> None:
        """
        Grabs the users github info
        """

        """
        await github(context, username) -> nothing

        Returns the github user info

        :param ctx object: Context
        :param user str: Username to look for
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        if not user.startswith('http'):
            user = f"https://github.com/{user}"

        async with aiohttp.ClientSession() as cs:
            async with cs.get(user) as req:
                resp = await req.read()

        scraper = bs(resp, "html.parser")

        profile_picture = scraper.find("img", {"alt": "Avatar"})["src"]
        repositories = scraper.find("span", {"class": "Counter"}).text
        bio = scraper.find('div', {'class': 'p-note user-profile-bio mb-3 js-user-profile-bio f4'}).text
        follow_find = scraper.find_all("span", {"class": "text-bold color-fg-default"})
        follow = [i.text.strip() for i in follow_find if i]

        followers, following = 0, 0
        if len(follow) >= 2:
            followers, following = follow

        await sendmsg(
            ctx,
            (
                f'**Username**: `{user}`\n'
                f'**Account**: `{user}`\n'
                f'**Bio**: `{bio}`\n'
                f'**Followers**: `{followers}`\n'
                f'**Following**: `{following}`\n'
                f'**Repositories**: `{repositories}`\n'
                f'**Avatar url**: `{profile_picture}`'
            )
        )

async def setup(client):
    await client.add_cog(Lookup(client))