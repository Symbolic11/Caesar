<div align="center">
   <h1 style="font-size: 220%">Caesar</h1>

   <img alt="forks"        src="https://img.shields.io/github/forks/Symbolic11/Caesar"/>
   <img alt="last commit"  src="https://img.shields.io/github/last-commit/Symbolic11/Caesar/main"/>
   <img alt="stars"        src="https://img.shields.io/github/stars/Symbolic11/Caesar">
   <img alt="license"      src="https://img.shields.io/github/license/Symbolic11/Caesar">
   <img alt="issues"       src="https://img.shields.io/github/issues/Symbolic11/Caesar">
   <img alt="size"         src="https://img.shields.io/github/repo-size/Symbolic11/Caesar">
   <img alt="top language" src="https://img.shields.io/github/languages/top/Symbolic11/Caesar">
</div>

# !! READ ME FIRST !!
## I got banned from discord. lol. All work on this project will be stopped, and the repository will be archived. 
## ps: fuck you discord

# About
My own personal selfbot, free and opensource for ever. Lots of commands & weekly (if not daily) updates

# Disclaimer
```
Selfbots are against Discord's Terms of Service
Usage of this program can result in your account get locked and/or terminated! 
I, Symbolic,  can't be held responsible if anything happens to your account.
Use at your own risk.
```

# Features
- Working Dank-Memer farmer
- Tons of commands (AI, system info, memes, nsfw stuff, music player, ascii art and much more)
- Simple cog system
- Clean and documented code
- Fully open source, forever!

# Q&A
- Why is it so slow?
   - Caesar is not slow, it sends messages with delays to prevent detection. Sometimes it might take a while to send a message, or it can be near instant. Just be patient

- Is this against the TOS?
   - While technically selfbots are against the TOS, as long as you don't spam the API too much and keep the usage as stealthy as possible the chance to get banned will be extremely low
   - It's a grey zone, just be careful and don't start spamming commands in a big server

- I got my account banned thanks to you!
   - I put up a disclaimer, saying if you use this program you use it on your own risk. I can't be held responsible if anything happens to your account.

# Setup
<details>
<summary>Using the setup script</summary>

1. Run the script
```sh
python3 setup.py
```
2. Answer the questions
3. Profit
</details>

<details>
<summary>Without using the setup script</summary>

1. Install the depencies
```sh
pip install -r requirements.txt
pip install git+https://github.com/dolfies/discord.py-self@renamed#egg=selfcord.py
```

2. Get your token
 - This one-liner will copy your token to your clipboard, once run in the console: 
 ```js
   window.webpackChunkdiscord_app.push([[Math.random()], {}, (req) => {for (const m of Object.keys(req.c).map((x) => req.c[x].exports).filter((x) => x)) {if (m.default && m.default.getToken !== undefined) {return copy(m.default.getToken())}if (m.getToken !== undefined) {return copy(m.getToken())}}}]); console.log("%cWorked!", "font-size: 50px"); console.log(`%cYou now have your token in the clipboard!`, "font-size: 16px")
   ```

 - <a href="https://youtube.com/watch?v=YEgFvgg7ZPI">Here</a> is another way of getting your token

3. Open the config file, and replace `your token here!` with your token
 - If no config file is found, make one and name it `config.json`. Then save the following lines in there (after you've added your token):
```json
{
    "token": "your token here!",
    "prefix": ";",
    "nitro_sniper": false,
    "nitro_sniper_stealth": true,
    "giveaway_sniper": false,
    "giveaway_sniper_stealth": true,
    "slotbot_sniper": false,
    "slotbot_sniper_stealth": true,
    "apikeys": []
}
```

4. Save it, and launch the selfbot
```sh
python3 main.py
```
</details>

# Disabling a cog
## Before running the selfbot
You can disable certain cogs by
 - Removing them
 - Renaming them so the file suffix becomes `.disabled.py` instead of `.py`

## While running
You can unload a specific cog by using the `unload` command, the syntax is:
 - `<prefix>unload <cog name>`

For example:
 - `;unload crypto`

# License
```
This project is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, 
either version 3 of the License, or (at your option) any later version.

This project is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; 
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this code. 
If not, see <https://www.gnu.org/licenses/>. 
```
