import os
import random
from dotenv import load_dotenv

from discord.ext import commands

from mtgsdk import Card

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
#cardimage=""

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='lookup', help='Simulates rolling dice.')
async def lookup(ctx, *args):
    cardname=""
    print(args)
    for arg in args:
        print(arg)
        cardname = cardname + arg + " "
    cardname = cardname.strip()
    print(cardname)
    cards = Card.where(name=cardname).all()

    print(cards)
    for card in cards:
        if card.image_url:
            #cardimage = card.image_url
            print(card.image_url)
            await ctx.send(card.image_url)
            break
    
    #return value to client
    



bot.run(TOKEN)

"""
Calling a function
Error handling
Case senitivity problem?
Cloud
Catagorizing the input into the right place. like name into name.
card of the day
show me a random card
suggest a card
"""