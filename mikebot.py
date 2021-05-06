# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:37:54 2021
@author: Benes
"""
import discord
import nest_asyncio
import random


client = discord.Client()
guild = discord.Guild

token = os.getenv('DISCORD_TOKEN')

mikeQuotes = ["_decisions have consequences_","_i've killed more men with words_","poop","beep boop","oh hi mark","you've been blinded, fool","why the fuck are they nerfing bard","oh hell no","https://www.youtube.com/watch?v=uH0hikcwjIA",":0 yes that's me","math is pretty cool","teemo is the best champion in the game","that was not very cash money of you","that's a money move right there",":eyes: what's up gamers","jugilae????", "we must dance to shame dog planet","dude i feel that","dude that reminds me of when i was in popreka, ucsc's finest kpop dance group","cki is pain", "when will jeff carry me", "your honor, that's cap", "im a macro player","schnucki", "please look at this german content \nhttps://www.youtube.com/watch?v=39UDZMgPg5k"]

mike8ball = ["oh heck yeah","oh hell no","yis","no lmao",":0 sure",":eyes: maybe","yes swear on me mum","nO","oui oui","NOPE","i mean i guess so","no that sounds spooky","??? i don't know","yes as long as there's no xerath involved","unfortunately no, gamer", "i mean okay yeah","no your honor","im gonna go with a yes your honor",":regional_indicator_n::regional_indicator_o:","yes but only with teemo","lmao","yikes","yes i believe","no :'0"]

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
nest_asyncio.apply()    

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #math rule
    if "math" in message.content and "i hate math" not in message.content and "!mike8" not in message.content:
           await message.channel.send('did someone say math')
           
    #teemo rule
    if "teemo" in message.content and "!mike8" not in message.content:
           await message.channel.send(':0 teemo')     
           
    #!mikehelp       
    if (message.content=="!mikehelp"):
        await message.channel.send("hey what's up gamers i'm mikebot. i'm a discord bot that's automated to sound like mike so that mike can go play animal crossing or something\n-----\nthese are my commands:\n -!mikehelp - lists commands\n -!mike - random message from mike\n -!mike8 {your question}- 8-ball command. ask mike a question and i will answer for him\n -math - i like math and if you ever mention math _i will know_" )
    
    #!mike
    if (message.content=="!mike"):
           await message.channel.send(random.choice(mikeQuotes))
    
    #!mike8
    if message.content.startswith("!mike8"):
        await message.channel.send(random.choice(mike8ball))
    
    #i hate math rule
    if "i hate math" in message.content:
        await message.channel.send(">:0 how dare you hate math")

# message.channel.send
client.run(token)
nest_asyncio.apply()        
