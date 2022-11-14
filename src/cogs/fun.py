import string

from selfcord.ext import commands
from random import choice, randint, shuffle
from datetime import datetime

from src.utils import *

class Fun(commands.Cog):
    """
    Fun commands
    """

    def __init__(self, client: commands.Bot):
        self.client = client

        self.computers = [
            'Windows',
            'Linux',
            'MacOS',
            'iOS',
            'Android',
            'TempleOS',
            'Unknown',
            'Arch (btw)',
            'FemboyOS'
        ]

        self.countries = [
            'Afghanistan',
            'Albania',
            'Algeria',
            'Andorra',
            'Angola',
            'Anguilla',
            'Argentina',
            'Armenia',
            'Aruba',
            'Australia',
            'Austria',
            'Azerbaijan',
            'Bahamas',
            'Bahrain',
            'Bangladesh',
            'Barbados',
            'Belarus',
            'Belgium',
            'Belize',
            'Benin',
            'Bermuda',
            'Bhutan',
            'Bolivia',
            'Bosnia & Herzegovina',
            'Botswana',
            'Brazil',
            'British Virgin Islands',
            'Brunei',
            'Bulgaria',
            'Burkina Faso',
            'Burundi',
            'Cambodia',
            'Cameroon',
            'Cape Verde',
            'Cayman Islands',
            'Chad',
            'Chile',
            'China',
            'Colombia',
            'Congo',
            'Cook Islands',
            'Costa Rica',
            'Cote D Ivoire',
            'Croatia',
            'Cruise Ship',
            'Cuba',
            'Cyprus',
            'Czech Republic',
            'Denmark',
            'Djibouti',
            'Dominica',
            'Dominican Republic',
            'Ecuador',
            'Egypt',
            'El Salvador',
            'Equatorial Guinea',
            'Estonia',
            'Ethiopia',
            'Falkland Islands',
            'Faroe Islands',
            'Fiji',
            'Finland',
            'France',
            'French Polynesia',
            'French West Indies',
            'Gabon',
            'Gambia',
            'Georgia',
            'Germany',
            'Ghana',
            'Gibraltar',
            'Greece',
            'Greenland',
            'Grenada',
            'Guam',
            'Guatemala',
            'Guernsey',
            'Guinea',
            'Guinea Bissau',
            'Guyana',
            'Haiti',
            'Honduras',
            'Hong Kong',
            'Hungary',
            'Iceland',
            'India',
            'Indonesia',
            'Iran',
            'Iraq',
            'Ireland',
            'Isle of Man',
            'Israel',
            'Italy',
            'Jamaica',
            'Japan',
            'Jersey',
            'Jordan',
            'Kazakhstan',
            'Kenya',
            'Kuwait',
            'Kyrgyz Republic',
            'Laos',
            'Latvia',
            'Lebanon',
            'Lesotho',
            'Liberia',
            'Libya',
            'Liechtenstein',
            'Lithuania',
            'Luxembourg',
            'Macau',
            'Macedonia',
            'Madagascar',
            'Malawi',
            'Malaysia',
            'Maldives',
            'Mali',
            'Malta',
            'Mauritania',
            'Mauritius',
            'Mexico',
            'Moldova',
            'Monaco',
            'Mongolia',
            'Montenegro',
            'Montserrat',
            'Morocco',
            'Mozambique',
            'Namibia',
            'Nepal',
            'Netherlands',
            'Netherlands Antilles',
            'New Caledonia',
            'New Zealand',
            'Nicaragua',
            'Niger',
            'Nigeria',
            'Norway',
            'Oman',
            'Pakistan',
            'Palestine',
            'Panama',
            'Papua New Guinea',
            'Paraguay',
            'Peru',
            'Philippines',
            'Poland',
            'Portugal',
            'Puerto Rico',
            'Qatar',
            'Reunion',
            'Romania',
            'Russia',
            'Rwanda',
            'Saint Pierre & Miquelon',
            'Samoa',
            'San Marino',
            'Saudi Arabia',
            'Senegal',
            'Serbia',
            'Seychelles',
            'Sierra Leone',
            'Singapore',
            'Slovakia',
            'Slovenia',
            'South Africa',
            'South Korea',
            'Spain',
            'Sri Lanka',
            'St Kitts & Nevis',
            'St Lucia',
            'St Vincent',
            'St. Lucia',
            'Sudan',
            'Suriname',
            'Swaziland',
            'Sweden',
            'Switzerland',
            'Syria',
            'Taiwan',
            'Tajikistan',
            'Tanzania',
            'Thailand',
            'Timor L\'Este',
            'Togo',
            'Tonga',
            'Trinidad & Tobago',
            'Tunisia',
            'Turkey',
            'Turkmenistan',
            'Turks & Caicos',
            'Uganda',
            'Ukraine',
            'United Arab Emirates',
            'United Kingdom',
            'Uruguay',
            'Uzbekistan',
            'Venezuela',
            'Vietnam',
            'Virgin Islands (US)',
            'Yemen',
            'Zambia',
            'Zimbabwe',
            'Reddit Isle'
        ]

        self.insults = [
            'fatass',
            'bald motherfucker',
            'crackhead',
            'cunt',
            'idiot',
            'fatso',
            'bald ass mf',
            'skin tone chickenbone',
            'bitch',
            'fuck you',
            'fat ass bitch',
            'retard',
            'nerd',
            ':nerd:',
            'rat looking mf',
            'motherfucker',
        ]

        self.responses = [
            'yes',
            'no',
            'absolutely',
            'absolutely not',
            'gay.',
            'totally',
            'no way!',
            'for sure!',
            'doubtable',
            'depends',
            'don\'t know for sure',
            'B33P, B00P. C4N\'T R3SP0ND. 3RR0R.',
            'fuck you, no.',
            'fuck you, yes.',
            'well yes, but actually no',
            'whatever, yes',
            'whatever, no',
            'ok.',
            'thats gross, i am not gonna answer that',
            'yeah, no.',
            'yeah, not sure',
            'reply hazy, try again',
            'failed to parse response, try again',
            'most likely',
            'possibly',
            'perhaps',
            'yes - definitly',
            'no - definitly',
            'signs point to yes',
            'god created and put you on this planet, just for you to ask this question.',
            'outlook not so good',
            'concentrate and ask again',
            'my reply is no',
            'my reply is yes',
            'too hard to tell'
        ]

        self.emails = [
            'protonmail.com', 
            'keemail.me', 
            'gmail.com', 
            'yahoo.com', 
            '420blaze.it', 
            'cumallover.me', 
            'cocaine.ninja',
            'waifu.club', 
            'dicksinhisan.us', 
            'wants.dicksinhisan.us',
            'fbi.gov',
            'loves.co.ck',
            'outlook.com',
            'ma-web.nl',
            'lovescock.uphisan.us',
            'cock.li',
            'airmail.cc',
            'goat.si',
            'horsefucker.org',
            'national.shitposting.agency',
            'tfwno.gf',
            'cock.lu',
            'cock.email',
            'firemail.cc',
            'memeware.net',
            'loves.dicksinhisan.us',
            'dicksinmyan.us',
            'loves.dicksinmyan.us',
            'wants.dicksinmyan.us',
            'nsa.gov'
        ]
    
    @commands.command()
    async def quote(self, ctx) -> None:
        """
        Returns a random quote
        """

        """
        await quote(context) -> nothing

        Returns a quote

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.quotable.io/random") as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            resp['content'],
            False
        )
    
    @commands.command()
    async def httpcat(self, ctx, *, code: int = 206) -> None:
        """
        Returns a random http.cat image, code is 206 if no code is provided else the given code is used
        """

        """
        await httpcat(context, user) -> nothing

        Returns a http.cat image

        :param ctx object: Context
        :param code int: HTTP status code
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            '',
            img=f'https://http.cat/{str(code)}', # http.cat returns the 404 image on invalid code, so no checking is needed :)
            delete_after=False
        )
    
    @commands.command()
    async def socialcredits(self, ctx, *, user: selfcord.User) -> None:
        """
        Calculates the given users social credits
        """

        """
        await socialcredits(context, user) -> nothing

        Calculates the given users social credits

        :param ctx object: Context
        :param user selfcord.User: The target user
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        socialcredits = randint(-5000000, 100000000)

        await sendmsg(
            ctx,
            f'{user.mention}, your social credit score is {str(socialcredits)}',
            False
        )
    
    @commands.command(aliases=['doxgen'])
    async def dox(self, ctx, *, user: selfcord.User) -> None:
        """
        Fake-doxxes the target user
        """

        """
        await dox(context, user) -> nothing

        Doxxes the target user

        :param ctx object: Context
        :param user selfcord.User: The target user
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        # shuffle everything
        shuffle(self.countries)
        shuffle(self.computers)
        shuffle(self.emails)

        await sendmsg(
            ctx,
            (
                f'**Username**: {user.name}\n'
                f'**IP address**: {".".join([str(randint(1, 255)) for _ in range(4)])}\n'
                f'**Country**: {choice(self.countries)}\n'
                f'**Computer**: {choice(self.computers)}\n'
                f'**Email**: {user.name.replace(" ","_").replace(".","_")}@{choice(self.emails)}'
            ),
            False
        )
    
    @commands.command()
    async def insult(self, ctx, *, user: selfcord.User) -> None:
        """
        Insults the target user
        """

        """
        await insult(context, user) -> nothing

        Insults the target user

        :param ctx object: Context
        :param user selfcord.User: The target user
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        shuffle(self.insults)
        await sendmsg(
            ctx,
            f'{user.mention}, {choice(self.insults)}',
            False
        )
    
    @commands.command()
    async def lennygun(self, ctx) -> None:
        """
        ( ͡° ͜ʖ ͡°)︻̷┻̿═━一-
        """

        """
        await lennygun(context) -> nothing

        ( ͡° ͜ʖ ͡°)︻̷┻̿═━一-

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            '( ͡° ͜ʖ ͡°)︻̷┻̿═━一-',
            False
        )
    
    @commands.command()
    async def lenny(self, ctx) -> None:
        """
        ( ͡° ͜ʖ ͡°)
        """

        """
        await lenny(context) -> nothing

        ( ͡° ͜ʖ ͡°)

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            '( ͡° ͜ʖ ͡°)',
            False
        )
    
    @commands.command(aliases=['fakenitro'])
    async def nitro(self, ctx) -> None:
        """
        Generates a random nitro code (might be valid, who knows?)
        """

        """
        await nitro(context) -> nothing

        Generates a random nitro code

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            f'https://discord.com/gifts/{await randomstr(16)}',
            False
        )
    
    @commands.command(aliases=['letmegooglethatforyou'])
    async def lmgtfy(self, ctx, *, message) -> None:
        """
        lmgtfy's the given message: https://lmgtfy.app/?qtype=search&q=lgmtfy
        """

        """
        await lmgtfy(context, query) -> nothing

        https://lmgtfy.app/?qtype=search&q=lgmtfy

        :param ctx object: Context
        :param message str: Messsage to query
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await sendmsg(
            ctx,
            f'https://lmgtfy.app/?qtype=search&q={message.replace(" ", "%20")}',
            False
        )
    
    @commands.command(aliases=['clap'])
    async def clapclap(self, ctx, *, message) -> None:
        """
        Puts the :clap: emoji inbetween every word
        """

        """
        await clapclap(context, message) -> nothing

        Puts the :clap: emoji inbetween every word

        :param ctx object: Context
        :param message str: Message to convert
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await sendmsg(
            ctx,
            f':clap:{message.replace(" ", ":clap:")}:clap:',
            False
        )
    
    @commands.command(aliases=['owo', 'uwuify', 'uwu-ify'])
    async def uwu(self, ctx, *, message) -> None:
        """
        owo wats dis?
        """

        """
        await uwu(context, message) -> nothing

        owo wats dis?

        :param ctx object: Context
        :param message str: Message to convert
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        for old, new in {
                'r': 'w', 
                'R': 'W', 
                'l': 'w', 
                'L': 'W', 
                ' n': ' ny', 
                ' N': ' NY', 
                'ove': 'uv', 
                'OVE': 'OV'
            }.items():
            message = message.replace(old, new)
            
        message += ' ' + choice([
            'owo', 
            'OwO', 
            'uwu', 
            'UwU', 
            '>w<', 
            '^w^', 
            '♥w♥', 
            'O3O', 
            '-w-', 
            'XwX'
        ])

        await sendmsg(
            ctx,
            message,
            False
        )
    
    @commands.command(aliases=['coinflip'])
    async def flip(self, ctx) -> None:
        """
        Flips a coin
        """

        """
        await flip(context) -> nothing

        Flips a coin

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            choice(['Tails', 'Heads']),
            False
        )
    
    @commands.command()
    async def catfact(self, ctx) -> None:
        """
        Sends a random fact about cats
        """

        """
        await catfact(context) -> nothing

        Sends a random fact about cats

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://majoexe.xyz/api/v1/fun/cat_fact") as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            resp['cat_fact'],
            False
        )
    
    @commands.command(aliases=['gimme-dog', 'showdog'])
    async def dog(self, ctx) -> None:
        """
        Sends a random image of a dog
        """

        """
        await dog(context) -> nothing

        Sends a random image of a dog

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://dog.ceo/api/breeds/image/random') as res:
                resp = await res.json()
        
        await sendmsg(
            ctx,
            delete_after=False,
            img=resp['message']
        )
    
    @commands.command(aliases=['gimme-fox', 'showfox'])
    async def fox(self, ctx) -> None:
        """
        Sends a random image of a fox
        """

        """
        await fox(context) -> nothing

        Sends a random image of a fox

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://randomfox.ca/floof') as res:
                resp = await res.json()
        
        await sendmsg(
            ctx,
            delete_after=False,
            img=resp['image']
        )
    
    @commands.command(aliases=['gimme-panda', 'showpanda'])
    async def panda(self, ctx) -> None:
        """
        Sends a random image of a panda
        """

        """
        await panda(context) -> nothing

        Sends a random image of a panda

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://some-random-api.ml/img/panda') as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            delete_after=False,
            img=resp['link']
        )
    
    @commands.command(aliases=['femboycalculator'])
    async def howfemboy(self, ctx, *, user: selfcord.User) -> None:
        """
        Calculates the femboy-ness of an user
        """

        """
        await howfemboy(context, user) -> nothing

        Calculates the femboy-ness of an user

        :param ctx object: Context
        :param user selfcord.User: User to calculate the femboy-ness
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        femboyness = randint(1, 100)

        if user.id == self.client.user.id:
            femboyness = 0
        
        await sendmsg(
            ctx,
            f'🏳️‍🌈 {user.mention} is {str(femboyness)}% a femboy',
            False
        )
    
    @commands.command(aliases=['furrycalculator', 'furgeiger'])
    async def howfurry(self, ctx, *, user: selfcord.User) -> None:
        """
        Calculates the furryness of an user
        """

        """
        await howfurry(context, user) -> nothing

        Calculates the furryness of an user

        :param ctx object: Context
        :param user selfcord.User: User to calculate the furryness
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        # calculate furryness
        if "furry" in user.name \
        or user.id == 369758936099848193 \
        or user.id == 923275490041659422:
            furryness = 100
        
        elif user.id == self.client.user.id:
            furryness = 0

        else:
            furryness = randint(1, 100)
        
        await sendmsg(
            ctx,
            f'🐺 {user.mention} is {str(furryness)}% a furry',
            False
        )
    
    @commands.command(aliases=['gaycalculator', 'howhomo', 'homocalculator', 'gaygeiger'])
    async def howgay(self, ctx, *, user: selfcord.User) -> None:
        """
        Calculates the gayness of the target user
        """

        """
        await howgay(context, user) -> nothing

        Calculates the gayness of the target user

        :param ctx object: Context
        :param user selfcord.User: User to calculate the gayness of
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        # calculate gayness
        if "blm" in user.name \
        or "lgbtq+" in user.name \
        or "kpop" in user.name \
        or "antifa" in user.name:
            gayness = 100
            
        elif user.id == self.client.user.id:
            gayness = 0

        else:
            gayness = randint(0, 100)
        
        await sendmsg(
            ctx,
            f'🏳️‍🌈 {user.mention} is {str(gayness)}% gay',
            False
        )
    
    @commands.command(aliases=['dong', 'dongsize', 'dick', 'dicksize', 'penissize'])
    async def penis(self, ctx, *, user: selfcord.User) -> None:
        """
        Dong size calculator
        """

        """
        await penis(context, user) -> nothing

        Dong size calculator

        :param ctx object: Context
        :param user selfcord.User: User to calculate the dong size
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        # calculate dong size
        if "nig" in user.name \
        or "based" in user.name \
        or "nationalist" in user.name \
        or "sigma" in user.name:
            dong = "="*randint(50, 100)
        else:
            dong = "="*randint(1, 50)

        await sendmsg(
            ctx,
            f'{user.mention}\'s dickdize: 8{dong}D',
            False
        )
    
    @commands.command()
    async def spam(self, ctx, times, *, msg) -> None:
        """
        Spams the given message for the given amount of times
        """

        """
        await spam(context, amount of times, message) -> nothing

        Spams the given message for the given amount of times

        :param ctx object: Context
        :param times int: Times to loop
        :param msg str: Message to send
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        await ctx.message.edit(content=msg)
        for _ in range(int(times)):
            await ctx.send(msg)
    
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx) -> None:
        """
        Hmm, yes
        """

        """
        await eightball(context) -> nothing

        Hmm, yes

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        shuffle(self.responses)
        await sendmsg(
            ctx,
            choice(self.responses),
            False
        )
    
    @commands.command(aliases=['fact', 'randomfact'])
    async def random_fact(self, ctx) -> None:
        """
        Sends a random fact
        """

        """
        await random_fact(context) -> nothing

        Sends a random fact from "src/files/facts.txt"

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        await sendmsg(
            ctx,
            await didyouknow(),
            False
        )
    
    @commands.command(aliases=['meme', 'gimme-meme', 'meem'])
    async def gimme_meme(self, ctx) -> None:
        """
        Sends a random meme
        """

        """
        await gimme_meme(context) -> nothing

        Sends a random meme

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://meme-api.herokuapp.com/gimme") as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            delete_after=False,
            img=resp['url']
        )
    
    @commands.command(aliases=['darkjoke', 'edgyjoke'])
    async def gimme_darkjoke(self, ctx) -> None:
        """
        Sends a dark joke
        """

        """
        await gimme_darkjoke(context) -> nothing

        Muslim women are horrible competitors.
        No matter what they do, they always get beat.

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://v2.jokeapi.dev/joke/Dark?format=txt") as res:
                resp = await res.text()

        await sendmsg(
            ctx,
            resp.rstrip(),
            False
        )
    
    @commands.command(aliases=['dadjoke', 'gimme-dadjoke', 'joke'])
    async def gimme_dadjoke(self, ctx) -> None:
        """
        Sends dad jokes
        """

        """
        await gimme_dadjoke(context) -> nothing

        Dad jokes

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession(headers={'Accept': 'application/json'}) as cs:

            async with cs.get(f"https://icanhazdadjoke.com/") as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            resp['joke'],
            False
        )
    
    @commands.command(aliases=['yomama', 'yo-mama'])
    async def yo_mama(self, ctx) -> None:
        """
        Yo mama so dumb, she thought twitter was social media!
        """

        """
        await yo_mama(context) -> nothing

        Yo mama so dumb, she thought twitter was social media!

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://api.yomomma.info/") as res:
                resp = await res.json()

        await sendmsg(
            ctx,
            resp['joke'],
            False
        )
    
    @commands.command(aliases=['hack', 'fakehack', 'pwn'])
    async def fake_hack(self, ctx, user) -> None:
        """
        Fake hacks the target user
        """

        """
        await fake_hack(context, username of target) -> nothing

        Fake hacks the target user

        :param ctx object: Context
        :param user str: Username of the target user
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        user = await self.client.fetch_user(
            user.replace('<@', '') \
                .replace('>', '') \
                .replace('!', '')
        ) # clean it up a bit

        user_name = str(user).split("#")
        if len(user_name) == 2: # while testing, it would sometimes give me the # aswell
            user_name = user_name[0]

        passwords = [
            'bestpasswordnocap',
            'password1',
            'root',
            ''.join(choice(
                string.ascii_letters
                + string.punctuation
                + string.digits
            ) for _ in range(randint(4,10)))
        ]

        shuffle(self.emails); shuffle(passwords)

        rand_cve = f'CVE-{str(randint(1995, datetime.now().year))}-{"".join(str(randint(0, 9)) for _ in range(4))}'
        rand_ip = f'{str(randint(0, 256))}.{str(randint(0, 256))}.{str(randint(0, 256))}.{str(randint(0, 256))}'

        msgs = [
            f'Scanning system for vulnerabilities.',
            f'Vulnerability found: `{rand_cve}`.',
            f'Exploiting system using `{rand_cve}`.',
            f'Malware installed on system.',
            f'`hack.js` injected into Discord.',
            f'Brute forcing account',
            f'Brute force success.\nEmail: `{user_name}@{choice(self.emails)}`\nPassword: `{choice(passwords)}`',
            f'Logging in.',
            f'Changing bio to `Hacked by {self.client.user}`.',
            f'Changing locale to russian.'
            f'Grabbing IP address.',
            f'IP found: {rand_ip}',
            f'DDoS\'ing IP using LOIC.',
            f'IP is offline.',
            f'Logging out of account.',
            f'Clearing traces.',
            f'Logs removed, device cleaned.',
        ]

        await ctx.message.edit(content=f'**[**0%**]** Hack on {user} started.')

        # this looks like a horrible mess
        # so basically what this does is, it generates a list of random numbers and appends the % to it
        # his provides us with pseudo-random list of percents
        percents = [
            f'{y}%'
            for y in sorted([f'{prefix}{choice(["", "." + str(randint(1, 9))])}'
            for prefix in [str(randint(i, i+1))[0] + str(randint(i, 9+i))[0]
            for i in range(0, len(msgs))]])
        ]
        
        for i, percent in enumerate(percents):
            await asyncio.sleep(uniform(2, 4))
            await ctx.message.edit(content=f'**[**{percent}**]** {msgs[i]}')

        await asyncio.sleep(uniform(2, 3))
        await ctx.message.edit(content=f'**[**100%**]** Successfully hacked {user_name}.')        

async def setup(client):
    await client.add_cog(Fun(client))