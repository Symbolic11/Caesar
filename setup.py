import sys, json
from os import system as run, name
from os.path import exists

def setup():
    token = input('> Enter your token: ')
    if len(token) <= 0:
        sys.exit('\nPlease enter a valid token.')
    
    prefix = input('> Bot prefix (default is ";"): ')
    if len(prefix) <= 0:
        prefix = ';'
    
    # could've done these in single lines,
    # but decided not to
    nitro_sniper = input('> Enable nitro sniper? (Y/n) ').lower().startswith('y')
    if nitro_sniper: nitro_sniper_stealth = input('> Enable stealth mode? (Y/n) ').lower().startswith('y')
    else: nitro_sniper_stealth = False

    giveaway_sniper = input('> Enable giveaway sniper? (Y/n) ').lower().startswith('y')
    if giveaway_sniper: giveaway_sniper_stealth = input('> Enable stealth mode? (Y/n) ').lower().startswith('y')
    else: giveaway_sniper_stealth = False

    slotbot_sniper = input('> Enable slotbot sniper? (Y/n) ').lower().startswith('y')
    if slotbot_sniper: slotbot_sniper_stealth = input('> Enable stealth mode? (Y/n) ').lower().startswith('y')
    else: slotbot_sniper_stealth = False

    # get api keys
    replicate_key = input('> Replicate API key: ')
    if len(replicate_key) <= 0:
        print('> No API key entered, AI related commands will be disabled!')
        replicate_key = None
    
    data = json.dumps(
        {
            'token': token,
            'prefix': prefix,
            'nitro_sniper': nitro_sniper,
            'nitro_sniper_stealth': nitro_sniper_stealth,
            'giveaway_sniper': giveaway_sniper,
            'giveaway_sniper_stealth': giveaway_sniper_stealth,
            'slotbot_sniper': slotbot_sniper,
            'slotbot_sniper_stealth': slotbot_sniper_stealth,
            'apikeys': {
                'replicate': replicate_key
            }
        },
        indent=4
    )

    # save (or overwrite) the config
    if exists('config.json'):
        overwrite = input('> Existing config found, overwrite? (Y/n) ').lower().startswith('y')
        if overwrite:
            with open('config.json', 'w+') as fd:
                fd.write(data)
        
        else:
            print('> Config saved to "config.json.1"')
            with open('config.json.1', 'w+') as fd:
                fd.write(data)
    
    else:
        with open('config.json', 'w') as fd:
            fd.write(data)

    # install depencies
    print('\n\n> Installing depencies')
    run('pip install -r requirements.txt')
    run('pip install git+https://github.com/dolfies/discord.py-self@renamed#egg=selfcord.py')

    print('> Creating launcher script')
    if name == 'nt':
        launcher = 'run.bat'
        body = 'py main.py'

    else:
        launcher = 'run.sh'
        body = 'python3 main.py'
    
    with open(launcher, 'w+') as fd: # "w+" overwrites any older launch scripts
        fd.write(body)

if __name__ == '__main__':
    print('''
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
    
    print('> Caesar setup')
    print('> You can always re-run this script if you want to.')

    setup()

    print(f'\n\n> Done')