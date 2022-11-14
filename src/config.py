import json, os, sys

from setup import setup
from base64 import b64decode

class config:
    token = ''
    prefix = ''
    nitrosniper_toggle = False
    nitrosniper_stealth = True
    giveawaysniper_toggle = False
    giveawaysniper_stealth = True
    slotbotsniper_toggle = False
    slotbotsniper_stealth = True
    apikeys = {}

def save_config():
    with open('config.json', 'w+', buffering=512) as fd:
        fd.write(json.dumps({
            'token': config.token,
            'prefix': config.prefix,
            'nitro_sniper': config.nitrosniper_toggle,
            'nitro_sniper_stealth': config.nitrosniper_stealth,
            'giveaway_sniper': config.giveawaysniper_toggle,
            'giveaway_sniper_stealth': config.giveawaysniper_stealth,
            'slotbot_sniper': config.slotbotsniper_toggle,
            'slotbot_sniper_stealth': config.slotbotsniper_stealth,
            'apikeys': config.apikeys
        },
        indent=4
    ))

def load_config():

    if not os.path.exists('config.json'):
        print('Config not found, running setup')
        setup()
    
    with open(
        'config.json',
        buffering=512
        ) as fd:
        cfg = json.loads(fd.read())
    
    try:
        tk_format, tk_str = cfg['token'].split(':')

        # can help with regex based token loggers
        if tk_format == 'base64' \
        or tk_format == 'b64':
            tk_str = b64decode(tk_str.encode()).decode()

    except Exception:
        tk_str = cfg['token']
    
    if tk_str == 'your token here!':
        sys.exit('\nIt seems like you\'ve forget to edit your token. \nPlease do that first before continuing!')

    try:
        config.token = tk_str
        config.prefix = cfg['prefix']
        config.nitrosniper_toggle = cfg['nitro_sniper']
        config.nitrosniper_stealth = cfg['nitro_sniper_stealth']
        config.giveawaysniper_toggle = cfg['giveaway_sniper']
        config.giveawaysniper_stealth = cfg['giveaway_sniper_stealth']
        config.slotbotsniper_toggle = cfg['slotbot_sniper']
        config.slotbotsniper_stealth = cfg['slotbot_sniper_stealth']
        config.apikeys = cfg['apikeys']
    except Exception as e:
        sys.exit(f'\nError while reading from config file: {str(e).rstrip()}')