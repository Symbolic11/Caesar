from selfcord.ext import commands

from src.utils import *

class Currency(commands.Cog):
    """
    All commands related to currency
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    async def coingecko_api(
        self, 
        currency: str | None = None
        ) -> list:
        """
        await coingecko_api(currency) -> list of strings

        Gets the price and information of the given currency

        :param currency str or None: Currency to look for
        :returns list: List of lines with info
        """

        if not currency:
            currency = 'monero'
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.coingecko.com/api/v3/coins/{currency}") as res:
                data = await res.json()
        
        if data.get('error'):
            return [f'**Error**: `{data["error"]}`']
        
        return [
            f'**Name**: `{data["name"]}`',
            f'**Hashing algorithm**: `{data["hashing_algorithm"]}`',
            f'**Homepage**: {"".join(["<"+x+">" for x in data["links"]["homepage"] if x != ""])}`',
            f'**Subreddit**: <{data["links"]["subreddit_url"]}>',
            f'**Prices**: `€{data["market_data"]["current_price"]["eur"]}, £{data["market_data"]["current_price"]["gbp"]}, ${data["market_data"]["current_price"]["usd"]}`'
        ]
    
    async def coincap_api(
        self, 
        currency: str
        ) -> list:
        """
        await coincap_api(currency) -> list of strings

        Gets the price and information of the given currency

        :param currency str: Currency to look for
        :returns list: List of lines with info
        """
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.coincap.io/v2/assets?search={currency}") as res:
                res = await res.json()
            
        if res['data'] == []:
            return ['**Error**: `Invalid coin`']
        
        res = res['data'][0] # pick the first coin

        return [
            f'**Name**: `{res["name"]}`',
            f'**Supply**: `{str(res["supply"])}`',
            f'**Market Cap**: `${str(res["marketCapUsd"])}`',
            f'**Price**: `${str(res["priceUsd"])}`',
            f'**Explorer**: <{res["explorer"]}>'
        ]
    
    @commands.command(aliases=['monero', 'moneroprice', 'xmrprice'])
    async def xmr(self, ctx) -> None:
        """
        Shows information about the Monero cryptocurrency
        """

        """
        await xmr(context) -> nothing

        Gets the price of monero

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx, 
            '\n'.join(await self.coingecko_api('monero')),
            False
        )
    
    @commands.command(aliases=['bitcoin', 'bitcoinprice', 'btcprice'])
    async def btc(self, ctx) -> None:
        """
        Shows information about the Bitcoin cryptocurrency
        """

        """
        await btc(context) -> nothing

        Gets the price of bitcoin

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
            
        await sendmsg(
            ctx, 
            '\n'.join(await self.coingecko_api('bitcoin')),
            False
        )
    
    @commands.command(aliases=['ethereum', 'ethereumprice', 'ethprice'])
    async def eth(self, ctx) -> None:
        """
        Shows information about the Ethereum cryptocurrency
        """

        """
        await eth(context) -> nothing

        Gets the price of ethereum

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
            
        await sendmsg(
            ctx, 
            '\n'.join(await self.coingecko_api('ethereum')),
            False
        )
    
    @commands.command()
    async def coingecko(self, ctx, coin: str = 'monero') -> None:
        """
        Shows information about the given cryptocurrency, using CoinGecko's API
        """

        """
        await coingecko(context, coin) -> nothing

        Gets the price of the specified coin

        :param ctx object: Context
        :param coin str: Coin to lookup
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
            
        await sendmsg(
            ctx, 
            '\n'.join(await self.coingecko_api(coin)),
            False
        )
    
    @commands.command()
    async def coincap(self, ctx, coin: str = 'monero') -> None:
        """
        Shows information about the given cryptocurrency, using CoinCap's API
        """

        """
        await coincap(context, coin) -> nothing

        Gets the price of the specified coin

        :param ctx object: Context
        :param coin str: Coin to lookup
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
            
        await sendmsg(
            ctx, 
            '\n'.join(await self.coincap_api(coin)),
            False
        )

async def setup(client):
    await client.add_cog(Currency(client))