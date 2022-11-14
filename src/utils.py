import asyncio, glob, aiohttp, io, selfcord, os, threading, math, re

from random import choice, uniform, randint
from selfcord.ext import commands
from os.path import join
from datetime import datetime
from collections.abc import AsyncGenerator, Generator
from concurrent.futures import ThreadPoolExecutor

with open(
    join('src', 'files', 'facts.txt'), 
    buffering=512
    ) as fd:
    facts = fd.read().splitlines()

with open(
    join('src', 'files', 'dictionary.txt'), 
    buffering=512
    ) as fd:
    dictionary = fd.read().splitlines()

class Regex:
    uppercase = re.compile(r'[A-Z]')
    lowercase = re.compile(r'[a-z]')
    numbers = re.compile(r'[0-9]')

async def get_entropy(
    string: str
    ) -> float:
    """
    await get_entropy(string) -> entropy

    Gets the entropy of the given string

    :param string str: String to compute entropy of
    :returns float: Entropy
    """

    ent = 0.0
    if len(string) < 2:
        return ent

    poolchar = 0
    if len(Regex.uppercase.findall(string)) > 0:
        poolchar += 26
    
    if len(Regex.lowercase.findall(string)) > 0:
        poolchar += 26
    
    if len(Regex.numbers.findall(string)) > 0:
        poolchar += 10
    
    specialc = 0
    for char in string:
        if not char.isalpha() and not char.isdigit():
            specialc += 1
    
    if specialc > 0:
        poolchar += 21 # special characters
    
    ent = math.log2(poolchar) * len(string)
    return ent

async def async_run(
    func, 
    *args, 
    **kwargs
    ) -> asyncio.Future:
    """
    await async_run(synchronous function, args, keyword args) -> asyncio future object

    Runs a synchronous function asynchronous

    :param func function: Synchronous function to run
    :param args str: Arguments
    :param kwargs str: Keyword arguments
    :returns asyncio.Future: Response from the asynchronously ran function
    """

    loop = asyncio.get_event_loop()

    return await loop.run_in_executor(
        ThreadPoolExecutor(),
        lambda: func(*args, **kwargs)
    )

def async_wrap_iter(
    it: Generator
    ) -> AsyncGenerator:
    """
    async_wrap_iter(iterable) -> async generator

    Turns a synchronous iterable into an asynchronous generator

    :param it Generator: Generator
    :returns AsyncGenerator: Asynchronous generator
    """

    loop = asyncio.get_event_loop()
    q = asyncio.Queue(1)

    exception = None
    _END = object()

    async def yield_queue_items() -> AsyncGenerator:
        """
        await yield_queue_items() -> async generator

        Yields all the items from the queue

        :returns AsyncGenerator: Asynchronous generator
        """

        while 1:
            next_item = await q.get()

            if next_item is _END:
                break

            yield next_item

        if exception is not None:
            # the iterator has raised, propagate the exception
            raise exception

    def iter_to_queue() -> None:
        """
        iter_to_queue() -> nothing

        Moves all the items from the iterable into the queue

        :returns None: Nothing
        """

        nonlocal exception

        try:
            for item in it:

                # This runs outside the event loop thread, so we
                # must use thread-safe API to talk to the queue.
                asyncio.run_coroutine_threadsafe(
                    q.put(item), 
                    loop
                ).result()

        except Exception as e:
            exception = e

        finally:
            asyncio.run_coroutine_threadsafe(
                q.put(_END), 
                loop
            ).result()

    threading.Thread(
        target=iter_to_queue
    ) .start()

    return yield_queue_items()

def get_size(
    _bytes: int | float, 
    suffix = "B"
    ) -> str:
    """
    get_size(bytes, suffix) -> proper unit

    Gets the proper unit for the bytes

    :param bytes int or float: Bytes
    :param suffix str: Suffix to prepend
    :returns str: String with proper unit and suffix prepended
    """

    factor = 1024
    for unit in ["", "Ki", "Mi", "Gi", "Te", "Pe"]:
        
        if _bytes < factor:
            return f'{_bytes:.2f} {unit}{suffix}'

        _bytes /= factor
    
    return ''

def clear() -> None:
    """
    clear() -> nothing

    Clears the screen, thats it

    :returns None: Nothing
    """

    print('\033c', end='')

def get_time(
    source: datetime,
    raw: bool = False
    ) -> str | dict:
    """
    get_time(source, raw dictionary) -> string or dictionary

    Parses the difference between now, and the given source

    :param source datetime: Datetime object
    :param raw bool: Wether to return a raw dictionary
    :returns str or dict: Dictionary if raw, else a string
    """

    hours, remainder = divmod(int((datetime.now() - source).total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)

    if raw:
        return {
            'weeks': weeks, 
            'days': days, 
            'hours': hours, 
            'minutes': minutes, 
            'seconds': seconds, 
            'remainder': remainder
        }
        
    else:
        final = f'{str(seconds)} second{"s"if seconds!=1 else""}'
        if minutes != 0: final = f'{str(minutes)} minute{"s"if minutes!=1 else""}, {final}'
        if hours != 0: final = f'{str(hours)} hour{"s"if hours!=1 else""}, {final}'
        if days != 0: final = f'{str(days)} day{"s"if days!=1 else""}, {final}'
        if weeks != 0: final = f'{str(weeks)} week{"s"if weeks!=1 else""}, {final}'

        return final

async def load_cogs(
    client: commands.Bot
    ) -> None:
    """
    await load_cogs(client) -> nothing

    Loads all cogs in the "src/cogs" directory

    :param client commands.Bot: The connected discord bot/client
    :returns None: Nothing
    """


    for file in glob.glob(join('src', 'cogs', '*')):
        if file.endswith('.py') and not '__' in file and not file.endswith('.disabled.py'):
            file = file.replace(os.sep, '.')[:-3]

            try:
                await client.load_extension(file)

            except commands.errors.ExtensionAlreadyLoaded:
                await client.unload_extension(file)
                await client.load_extension(file)

            except Exception as e:
                print(f'Exception while loading cog "{file}"> {str(e).rstrip()}\n')
                continue

async def unload_cog(
    client: commands.Bot,
    cog: str
    ) -> bool | None | Exception:
    """
    await unload_cog(client, cog name) -> status

    Unloads the given cog

    :param client commands.Bot: The connected discord bot/client
    :param cog str: Cog name
    :returns bool or Exception: True if the cog was unloaded, False if not found and an Exception if any errors where raised
    """

    for file in glob.glob(join('src', 'cogs', '*')):
        if cog in file:
            file = file.replace(os.sep, '.')[:-3]

            try:
                await client.unload_extension(file)

                return True
            except Exception as e:
                return e
    
    return False

async def randomstr(
    length: int, 
    chars: str | list = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789"
    ) -> str:
    """
    await randomstr(length, allowed characters) -> created string

    Builds a random string

    :param length int: Length of the string
    :param chars str or list: Characters to pick from
    """

    return ''.join([choice(chars) for _ in range(length)])

async def didyouknow() -> str:
    """
    await didyouknow() -> random fact

    Generates a random fact

    :returns str: the fact
    """

    return choice(facts).rstrip()

async def sendmsg(
    ctx, 
    message: str,
    delete_after: bool = True,
    img: str | None = None
    ) -> None:
    """
    await sendmsg(context, message, delete afterwards) -> nothing

    Sends a message, and adds some randomization to the delays

    :param ctx object: Context
    :param message str: Message to send
    :param img str or None: Image to send from url, leave empty for no image
    :param delete_after bool: Deletes the message afterwards
    :returns None: Nothing
    """

    attachments = []
    if img:
        async with aiohttp.ClientSession() as session:
            async with session.get(img) as resp:
                
                if resp.status != 200:
                    return print(f'Error, could not download image! Response code: {str(resp.status)}')
                
                else:
                    data = io.BytesIO(await resp.read())
                    attachments = [
                        selfcord.File(
                            data, 
                            f'{await randomstr(randint(1, 9))}.png'
                        )
                    ]

    await asyncio.sleep(uniform(1, 5))

    # overwrite the trigger message with our own message
    await ctx.message.edit(
        content=message, 
        attachments=attachments
    )

    if delete_after:
        await asyncio.sleep(uniform(10, 20))

        # after that, delete the message
        await ctx.message.delete()