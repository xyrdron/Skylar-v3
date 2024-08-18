import logging
import os
import sys

import discord
from colorama import Fore
from loader import loader
from discord.ext import commands

# DO NOT EDIT THIS FILE
# Or your PR will be rejected

# Enviroment Settings
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='*@#RH@(*U$YH*&HF@U#H', intents=intents)
logging.basicConfig(level=logging.INFO,
  format='\033[1m %(asctime)s %(levelname)s \033[0m    %(message)s', 
  datefmt=Fore.LIGHTBLACK_EX+'%Y-%m-%d %H:%M:%S'+Fore.RESET)  
logging.info(Fore.BLUE + f"Xyrdron Pty Ltd\nMikuBOT")

# Bot Startup
@bot.event
async def on_ready():
    logging.info(Fore.GREEN+'Connected to Discord')

    # Cogs
    cogcount = len([f for f in os.listdir('cogs') if os.path.isfile(os.path.join('cogs', f))])
    logging.info(Fore.BLUE+f'Loading cogs [{cogcount} to load]')
    cog_success = 0
    cog_skipped = 0
    cog_failed = 0
    for filename in os.listdir('cogs'):
        if filename.endswith(".py"):
            cog_name = filename[:-3]
            result = await loader(bot,'load',cog_name)
            if result == 0:
                cog_success = cog_success + 1
            elif result == 1:
                cog_skipped = cog_skipped + 1
            else:
                cog_failed = cog_failed + 1
            
    logging.info(Fore.GREEN+f'Loaded cogs [{cog_success} loaded, {cog_skipped} skipped, {cog_failed} failed]')


    # Syncing
    try:
        logging.info(Fore.BLUE+'Syncing command tree')
        await bot.wait_until_ready()
        await bot.tree.sync()
        logging.info(Fore.GREEN+'Commands synced')
    except Exception as e:
        logging.critical(Fore.RED+f'Failed to sync command tree {e}')
        logging.critical(Fore.RED+'Failed to complete boot sequence due to exception')
        sys.exit('Failed to complete boot sequence due to exception')

    # Presence
    try:
        logging.info(Fore.BLUE+'Setting presence')
        await bot.change_presence(activity=discord.Game(name="hehe~"))
        logging.info(Fore.GREEN+'Presence set')
    except Exception as e:
        logging.critical(Fore.RED+f'Failed to set presence {e}')
        logging.critical(Fore.RED+'Failed to complete boot sequence due to exception')
        sys.exit('Failed to complete boot sequence due to exception')

    # Miku is booted!1!1!1
    logging.info(Fore.GREEN+f'Boot successful, Logged in as {bot.user}')

def run():
    # IMPORTANT
    # TO ALL CONTRIBUTORS, PLEASE USE YOUR OWN BOT TOKEN FOR STAGING
    # CREATE A VSCODE LAUNCH CONFIGURATION AND ADD YOUR TOKEN AS AN ENV
    # .vscode is gitignored so you do not need to remove it (however just to be safe you should remove it on commit)
    logging.info(Fore.BLUE+'Connecting to Discord')
    bot.run(os.environ['RELEASE_BOT_SECRET'])

if __name__ == '__main__':
    run()