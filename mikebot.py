# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:37:54 2021
@author: Benes
"""
import discord
#import nest_asyncio
import random
import os
import re
from mike_quotes import mikeQ, mike8ball
from spec_quotes import franky8ball, creator8ball, megan8ball, jacky8ball, dillon8ball, britney8ball, kev8ball, kiett8ball, kyle8ball, ariel8ball, nathan8ball, kelly8ball, lexie8ball, alvi8ball, hannah8ball, mikey8ball, brandon8ball, mathieu8ball

client = discord.Client()
guild = discord.Guild

token = os.getenv('DISCORD_TOKEN')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
# nest_asyncio.apply()    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #math rule
    if re.search(r"\b[Mm][Aa][Tt][Hh]\b", message.content) and "i hate math" not in message.content and "!mike8" not in message.content:
           await message.channel.send('did someone say math')
           
    #teemo rule
    if re.search(r"\b[Tt][Ee][Ee][Mm][Oo]\b", message.content) and "!mike8" not in message.content:
           await message.channel.send(':0 teemo')     
           
    #!mikehelp       
    if (message.content=="!mikehelp"):
        await message.channel.send("hey what's up gamers i'm mikebot. i'm a discord bot that's automated to sound like mike so that mike can go play animal crossing or something\n-----\nthese are my commands:\n !mikehelp - lists commands\n !mike - random message from mike\n !mike8 {your question}- 8-ball command. ask mike a yes/no question and i will answer for him\n math - i like math and if you ever mention math _i will know_" )
    
    #!mike
    if (message.content=="!mike"):
           await message.channel.send(random.choice(mikeQ))
    
    #!mike8
    if message.content.startswith("!mike8"):
        #franky
        if (str(message.author)=="Ray1500#8011"):
            await message.channel.send(random.choice(franky8ball))
        #megan
        elif (str(message.author)=="meg#5937"):
            await message.channel.send(random.choice(megan8ball+mike8ball))
        #mike
        elif (str(message.author)=="beneschan#9845"):
            await message.channel.send(random.choice(creator8ball+mike8ball))
        #britney
        elif (str(message.author)=="brit#7538"):
            await message.channel.send(random.choice(britney8ball+mike8ball))
        #kev
        elif (str(message.author)=="kev#3104"):
            await message.channel.send(random.choice(kev8ball+mike8ball))
        #ariel
        elif (str(message.author)=="ariii#3082"):
            await message.channel.send(random.choice(ariel8ball+mike8ball))
        #kyle
        elif (str(message.author)=="FLUFFYzOMG#8290"):
            await message.channel.send(random.choice(kyle8ball+mike8ball))
        #kiett
        elif (str(message.author)=="Kiett#9385"):
            await message.channel.send(random.choice(kiett8ball+mike8ball))
        #jacky
        elif (str(message.author)=="jacky#3616"):
            await message.channel.send(random.choice(jacky8ball+mike8ball))
        #dillon
        elif (str(message.author)=="Diyllliaon#8346"):
            await message.channel.send(random.choice(dillon8ball+mike8ball))            
        #nathan
        elif (str(message.author)=="soul#8497"):
            await message.channel.send(random.choice(nathan8ball+mike8ball))          
        #kelly    
        elif (str(message.author)=="kellyellow#5482"):
            await message.channel.send(random.choice(kelly8ball+mike8ball))          
        #alvi
        elif (str(message.author)=="ItsLV#7146"):
            await message.channel.send(random.choice(alvi8ball+mike8ball))          
        #lexie
        elif (str(message.author)=="ScarletHeart#4514"):
            await message.channel.send(random.choice(lexie8ball+mike8ball))          
        #hannah
        elif (str(message.author)=="yue#5715"):
            await message.channel.send(random.choice(hannah8ball+mike8ball))          
        #mikey
        elif (str(message.author)=="mikey#4269"):
            await message.channel.send(random.choice(mikey8ball+mike8ball))          
        #brandon
        elif (str(message.author)=="yoroba#5636"):
            await message.channel.send(random.choice(brandon8ball+mike8ball))          
        #mathieu
        elif (str(message.author)=="mathieu1111#2963"):
            await message.channel.send(random.choice(mathieu8ball+mike8ball))
        else:
            await message.channel.send(random.choice(mike8ball))
    
    #i hate math rule
    if "i hate math" in message.content:
        await message.channel.send(">:0 how dare you hate math")

client.run(token)
# nest_asyncio.apply()        
