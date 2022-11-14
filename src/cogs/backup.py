import json

from selfcord.ext import commands
from datetime import datetime
from os.path import exists

from src.utils import *
from src.core import *

class Backup(commands.Cog):
    """
    Commands related to keeping your account safe
    """

    def __init__(self, client: commands.Bot):
        self.client = client
    
    async def mk_name(self, name) -> str:
        """
        await mk_name(name) -> name with timestamp

        Appends the current date and time to the given argument

        :param name str: Name to append timestamp to
        :returns str: Name with timestamp appened
        """

        now = datetime.now().strftime('%D_%m_%Y_%H_%M_%S')
        return f'{now}_{name}'
    
    @commands.command(aliases=['backup-all', 'all-backup'])
    async def backup(self, ctx) -> None:
        """
        Backups everything (servers, friends)
        """

        """
        await backup(context) -> Nothing

        Backups everything from the users account (guilds, friends

        :param ctx object: Context
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        for cmd in ['friends', 'guilds']:
            await ctx.invoke(self.client.get_command(f'backup_{cmd}'))
    
    @commands.command(aliases=['guilds-backup', 'backup-servers', 'backup-guilds'])
    async def backup_guilds(
        self,
        ctx,
        dest: str = 'servers.json'
        ) -> None:
        """
        Stores all of your servers
        """

        """
        await backup_guilds(context, destination file) -> nothing

        Saves all of the users guilds in a file

        :param context object: Context
        :param dest str: File to save the friends in
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return
        
        guilds = []
        for guild in self.client.guilds:
            if guild:

                # try grabbing the vanity invite
                invite = None
                try:
                    invite = await guild.vanity_invite()
                except Exception:
                    pass

                # try grabbing the first invite
                if not invite:
                    try:
                        invite = await guild.invites()
                        invite = invite[0].code
                    
                    except Exception:
                        pass
                
                # and as a last resort, try creating an invite
                if not invite:
                    try:
                        invite = await guild.text_channels[0].create_invite()
                        invite = invite.code
                    except Exception:
                        pass
                
                if type(invite) != str:
                    invite = None
                
                guilds.append((guild.name, invite))
        
        if dest.endswith('.json'):
            guilds = [
                {'name': guild[0], 'invite': guild[1]}
                for guild in guilds
            ]

            data = json.dumps(
                {'guilds': guilds},
                indent=4
            )
        
        else:
            data = "\n".join([
                f'{guild[0]}|{guild[1]}'
                for guild in guilds
            ])
        
        msg = None
        if exists(dest):
            msg = await ctx.send(f'**"{dest}" already exists, renaming.**')
            dest = await self.mk_name(dest)
        
        with open(dest, 'w+') as fd:
            fd.write(data)
        
        if not msg:
            await sendmsg(ctx, f'**Stored guilds in**: `{dest}`')
        else:
            await msg.edit(content=f'**Stored guilds in**: `{dest}`')
            await asyncio.sleep(uniform(3, 6))
            await msg.delete()
        
    @commands.command(aliases=['friends-backup', 'backup-friends'])
    async def backup_friends(
        self,
        ctx,
        dest: str = 'friends.json'
        ) -> None:
        """
        Stores all your friends in a file (friends.json by default)
        """

        """
        await backup_friends(context, destination file) -> nothing

        Saves all of the users friends into a file

        :param context object: Context
        :param dest str: File to save the friends in
        :returns None: Nothing
        """

        if ctx.message.author.id != self.client.user.id:
            return

        friends = [
            (f'{repr(friend.user.name)}#{friend.user.discriminator}', friend.user.id)
            for friend in self.client.user.friends
            if friend
        ][::-1]

        if dest.endswith('json'):
            friends = [
                {'name': friend[0], 'id': friend[1]}
                for friend in friends
            ]

            data = json.dumps(
                {'friends': friends},
                indent=4
            )

        else:
            data = "\n".join([
                friend[0]
                for friend in friends
            ])
        
        msg = None
        if exists(dest):
            msg = await ctx.send(f'**"{dest}" already exists, renaming.**')
            dest = await self.mk_name(dest)
        
        with open(dest, 'w+') as fd:
            fd.write(data)
        
        if not msg:
            await sendmsg(ctx, f'**Stored friends in**: `{dest}`')
        else:
            await msg.edit(content=f'**Stored friends in**: `{dest}`')
            await asyncio.sleep(uniform(3, 6))
            await msg.delete()

async def setup(client):
    await client.add_cog(Backup(client))