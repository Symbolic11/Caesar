import psutil, platform, cpuinfo, distro

from selfcord.ext import commands

from src.utils import *
from src.core import *

class System(commands.Cog):
    """
    System information, memory and cpu viewing and more
    """

    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command(aliases=['mem', 'memory-usage'])
    async def memory(self, ctx) -> None:
        """
        Shows the memory usage
        """

        """
        await memory(context) -> nothing

        Returns the memory usage

        :param ctx object: Context
        :returns None: Nothing
        """

        mem = psutil.virtual_memory()
        await sendmsg(
            ctx,
            (
                '__**Memory usage**__\n'
                f'**Used**: `{get_size(mem.used)} ({mem.percent}%)`\n'
                f'**Aviable**: `{get_size(mem.available)}`\n'
                f'**Total**: `{get_size(mem.total)}`'
            )
        )
    
    @commands.command(aliases=['cpu-usage'])
    async def cpu(self, ctx) -> None:
        """
        Shows the CPU usage
        """

        """
        await cpu(context) -> nothing

        Returns the CPU usage

        :param ctx object: Context
        :returns None: Nothing
        """

        await sendmsg(
            ctx,
            f'**CPU usage**: `{psutil.cpu_percent(0.1)}%`'
        )

    @commands.command()
    async def neofetch(self, ctx) -> None:
        """
        Shows your system information in a very fancy way
        """

        """
        await neofetch(context) -> nothing

        Returns the devices system information in a fancy way

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        memory = psutil.virtual_memory()
        battery = psutil.sensors_battery()
        cpu = cpuinfo.get_cpu_info()

        msg = f'''```ansi
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿   {self.client.user.name} 
⣿⡟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⢹⣿   {'-'*len(self.client.user.name)}
⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿   OS: {platform.platform()} ({distro.name(pretty=True) if os.name == 'posix' else 'Windows'})
⣿⡇⠄⠄⠄⢠⣴⣾⣵⣶⣶⣾⣿⣦⡄⠄⠄⠄⢸⣿   Boot time: {datetime.fromtimestamp(psutil.boot_time()).strftime('%d/%m/%y %S:%M:%H')}
⣿⡇⠄⠄⢀⣾⣿⣿⢿⣿⣿⣿⣿⣿⣿⡄⠄⠄⢸⣿   CPU: {cpu['brand_raw']}, {cpu["arch_string_raw"]} ({psutil.cpu_percent(0.1)}%)
⣿⡇⠄⠄⢸⣿⣿⣧⣀⣼⣿⣄⣠⣿⣿⣿⠄⠄⢸⣿   Memory: {get_size(memory.used)} / {get_size(memory.total)} ({memory.percent}%)
⣿⡇⠄⠄⠘⠻⢷⡯⠛⠛⠛⠛⢫⣿⠟⠛⠄⠄⢸⣿   Battery: {str(int(battery.percent))+"%" if battery else "No battery installed"} {"[Discharging]" if not battery.power_plugged else "[Charging]" if battery.power_plugged else "[Unbound]"}
⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿
⣿⣧⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢡⣀⠄⠄⢸⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣆⣸⣿```'''

        await asyncio.sleep(uniform(2, 4))    
        await ctx.message.edit(content=msg)
    
    @commands.command()
    async def htop(self, ctx, max=5) -> None:
        """
        Shows CPU usage, memory usage and the top max most cpu consuming processes (5 by default)
        """

        """
        await htop(context, message, max amount of procs) -> nothing

        Shows CPU usage, memory usage and the top x most cpu consuming processes (where x is the max)

        :param ctx object: Context
        :param max int: Max amount of processes to return, max 21
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        if max > 21:
            max = 5

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content=f'**Hold on, this might take a while.**')

        procs = [(
            proc.name(),
            proc.cpu_percent(0.1) / psutil.cpu_count()
        ) for proc in psutil.process_iter()]

        procs_sorted = sorted(
            procs, 
            key=lambda procObj: procObj[1], 
            reverse=True
        )

        msg = [
            f'**CPU usage**: `{psutil.cpu_percent(0.1)}%`',
            f'**Memory usage**: `{str(psutil.virtual_memory().percent)}%`',
            f'**Top {str(max)} most CPU eating processes**:'
        ]

        for i, proc in enumerate(procs_sorted):
            if i > max:
                break

            msg.append(f'__{str(i)}__ - {proc[0]}: {str(proc[1])}')

        await asyncio.sleep(uniform(1, 2))
        await ctx.message.edit(content="\n".join(msg))

        await asyncio.sleep(uniform(15, 20))
        await ctx.message.delete()

async def setup(client):
    await client.add_cog(System(client))