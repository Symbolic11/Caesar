import sys

from selfcord.ext import commands
from datetime import datetime
from colorama import Fore, init

# initialize colorama
init(autoreset=True)

from src.utils import *
from src.config import *
from src.cogs import *
from src.core import *

load_config()

client = commands.Bot(
    command_prefix=config.prefix, 
    caseinsensitive=True,
    self_bot=True
)

@client.event
async def on_connect() -> None:
    """
    on_connect() -> nothing

    Runs when Ceasar connects to the Discord gateway

    :returns None: Nothing
    """

    Core.connect_time = datetime.now()

@client.event
async def on_command_error(ctx, error) -> None:
    """
    on_command_error(context, error) -> nothing

    Error handler

    :param ctx object: Context
    :param error object: Exception
    :returns None: Nothing
    """

    orig_error = getattr(
        error,
        'original',
        error
    )

    error = str(error).rstrip()

    print(f'\n{Fore.RED}>{Fore.RESET} ', end='')
    if isinstance(orig_error, commands.CommandNotFound):
        print(f'Command not recognized: {error}')
        await sendmsg(ctx, f'**Command not recognized**: `{error}`')
    
    elif isinstance(orig_error, (commands.MissingRole, commands.MissingAnyRole)):
        print(f'Missing role(s): {error}')
        await sendmsg(ctx, f'**Missing role(s)**: `{error}`')
    
    elif isinstance(orig_error, commands.CommandOnCooldown):
        print(f'Command is on cooldown>:{error}')
        await sendmsg(
            ctx, 
            (
                f'**Command is on cooldown**: `{error}`\n'
                f'**Seconds until cooldown is finished**: `{round(orig_error.retry_after, 2)}`'
            )
        )
    
    else:
        print(f'Error appeared: {str(error)}')
        await sendmsg(ctx, f'**Error**: `{str(error)}`')

    await asyncio.sleep(uniform(1, 2))

    # sometimes the message already gets deleted by the user, so we wrap this up
    # incase it does happen (else code will error out)
    try:
        await ctx.message.delete()
    except Exception:
        pass

@client.event
async def on_ready() -> None:
    """
    on_ready() -> nothing

    Runs when Ceasar is fully ready

    :returns None: Nothing
    """

    clear()

    if not client.user:
        sys.exit(f'{Fore.RED}User not logged in!{Fore.RESET}')

    print(f'''{Fore.LIGHTBLUE_EX}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⢿⡶⠆⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⡿⠻⠋⣠⠀⢀⣶⠇⢠⣾⡿⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣼⠟⠋⠻⢁⣴⠀⣾⣿⠀⠾⠟⠀⠈⣉⣠⣦⡤⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠃⣠⡆⠀⣿⡟⠀⠛⠃⠀⠀⣶⣶⣦⣄⠉⢁⡄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣰⡀⢰⣿⠇⠀⢉⣀⣀⠛⠿⠿⠦⠀⢀⣠⣤⣴⣾⡇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⠃⠀⠠⣴⣦⡈⠙⠛⠓⠀⢰⣶⣶⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀
⠀⠀⢀⣤⠦⡀⠰⢷⣦⠈⠉⠉⠀⣰⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀
⠀⠀⠈⠁⠀⠘⣶⣤⣄⣀⣨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣯⡈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣷⣤⣈⡉⠛⠛⠛⠛⠻⠟⠛⠛⠛⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉''')

    latency = round(client.latency * 1000)

    if latency > 100: latency_color = Fore.LIGHTYELLOW_EX
    elif latency > 200: latency_color = Fore.RED
    else: latency_color = Fore.LIGHTGREEN_EX

    print(f'Logged in as "{Fore.LIGHTBLUE_EX}{client.user}{Fore.RESET}" (id: {Fore.LIGHTBLUE_EX}{client.user.id}{Fore.RESET})')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Extensions loaded: {str(len(client.extensions))}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Commands: {str(len(client.commands))}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Guilds: {str(len(client.guilds))}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Friends: {str(len(client.user.friends))}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Started at: {str(Core.start_time)}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Connected at: {str(Core.connect_time)}')
    print(f'{Fore.LIGHTBLUE_EX}>{Fore.RESET} Latency: {latency_color}{str(latency)}{Fore.RESET} ms\n')

if __name__ == '__main__':
    clear()

    Core.start_time = datetime.now()

    try:
        asyncio.run(load_cogs(client))
        client.run(config.token)
    
    except KeyboardInterrupt:
        pass

    except Exception as e:
        asyncio.run(client.close())

        print(f'Exception while connecting: {str(e).rstrip()}')
    
    save_config()
    sys.exit('\nClosing.')