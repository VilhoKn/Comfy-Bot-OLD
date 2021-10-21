
#DISCORD IMPORTS

import discord
from discord.ext import commands
from discord.utils import get
from discord.commands import Option

#OTHER IMPORTS

import datetime
import json
import asyncio
import random

#SETUP

with open("files/on_message_trigger_words.txt", "r") as f:
	f_lines = f.readlines()
	ON_MESSAGE_TRIGGER_WORDS = []
	for i in f_lines:
		ON_MESSAGE_TRIGGER_WORDS.append(i.strip("\n"))

with open("files/quotes.txt", "r") as f:
	f_lines = f.readlines()
	QUOTES = []
	for i in f_lines:
		QUOTES.append(i.strip("\n"))

with open("files/cat_image_links.txt", "r") as f:
	f_lines = f.readlines()
	CAT_IMAGE = []
	for i in f_lines:
		CAT_IMAGE.append(i.strip("\n"))

with open("files/dog_image_links.txt", "r") as f:
	f_lines = f.readlines()
	DOG_IMAGE = []
	for i in f_lines:
		DOG_IMAGE.append(i.strip("\n"))

with open("files/bunny_image_links.txt", "r") as f:
	f_lines = f.readlines()
	BUNNY_IMAGE = []
	for i in f_lines:
		BUNNY_IMAGE.append(i.strip("\n"))

#OTHER VARIABLES

c = 0xefd8d0

#EMBED VARIABLES



#BOT VARIABLES

bot = discord.Bot()

#EVENTS

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.listening,name='Comfy Vibes'))
	print(f"Comfy Bot logged in as: {bot.user}", end="\n\n")

@bot.event
async def on_message(message):
	if message.author.bot:
		return
	temp_msg = message.content.lower().split(" ")
	for i in temp_msg:
		if i in ON_MESSAGE_TRIGGER_WORDS:
			viesti = discord.Embed(title="Depression Help", description = f"Hey, I saw you were talking about depressing things on {message.guild} and wanted to say that there are people that love and care about you!\n\nIf you want information about helplines for depressed and suicidal people use command `/ineedhelp`", color = c)
			try:
				channel = await message.author.create_dm()
				await channel.send(embed=viesti)
			except:
				await message.send(embed=viesti, ephemeral=True)
			return

#COMMANDS

@bot.slash_command(guild_ids=[900712260937322526], name="ineedhelp", description="Sends an info message about depression helplines in dms")
async def ineedhelp(ctx):
	viesti = discord.Embed(title="I Need Help Helplines", description = f"Here is information about helplines for depressed and suicidal people", color = c)
	viesti.add_field(name="Child Helplines (EU)", value="""
Telephone: 116 111

This number is free of charge.

The number 116 111 is specifically for children who seek assistance and need someone to talk to. The service helps children in need of care and protection and links them to the appropriate services and resources; it provides children with an opportunity to express their concerns and talk about issues directly affecting them.

Here's an alphabetical list of member states which have access to 116 111: Bulgaria, Cyprus, Czech Republic, Germany, Denmark, Estonia, Greece, Spain, Finland, Croatia, Hungary, Ireland, Lithuania, Luxembourg, Latvia, Poland, Portugal, Romania, Sweden, Slovenia, Slovakia, United Kingdom, Malta.
	""")
	viesti.add_field(name="Emotional Support Helpline (EU)", value="""
Telephone: 116 123

This number is free of charge.

116 123 is a phone number for people suffering from loneliness or who are in a state of psychological crisis or thinking about committing suicide.

Here's an alphabetical list of member states which have access to 116 123: Austria, Czech Republic, Germany, Greece, Hungary, Ireland, Lithuania, Malta, Netherlands, Poland, Slovenia, Sweden, United Kingdom.
	""")
	viesti.add_field(name="National Suicide Prevention Lifeline (US)", value="""
Telephone: 1-800-273-8255 (1-800-273-TALK)
Text: Text "START" (without quotes) to 741-741.
	""")
	try:
		channel = await ctx.author.create_dm()
		await channel.send(embed=viesti)
		viesti2 = discord.Embed(title="I Need Help Helplines", description = "I sent you a dm about helplines for depressed and suicidal people", color = c)
		await ctx.respond(embed=viesti2, ephemeral=True)
	except:
		await ctx.respond(embed=viesti, ephemeral=True)
	return

@bot.slash_command(guild_ids=[900712260937322526], name="quote", description="Sends a comfy quote")
async def quote(ctx):
	ce = random.choice(QUOTES)
	quote, author = ce.split("-")
	if author == "me":
		author = "Comfy Bot"
	viesti = discord.Embed(description = quote, color = c)
	viesti.set_footer(text=author, icon_url=bot.user.avatar.url)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="hug", description="Give someone a hug")
async def hug(ctx, member : Option(discord.Member, "Member to hug")):
	viesti = discord.Embed(description = f"{ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂)", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Hug this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"{ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂)", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="kiss", description="Kiss someone")
async def kiss(ctx, member : Option(discord.Member, "Member to kiss")):
	viesti = discord.Embed(description = f"{ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶)", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Kiss this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"{ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶)", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="wave", description="Wave at someone")
async def wave(ctx, member : Option(discord.Member, "Member to wave at")):
	viesti = discord.Embed(description = f"{ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Wave at this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"{ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="cat", description="Send a cute cat picture")
async def cat(ctx):
	cat = random.choice(CAT_IMAGE)
	await ctx.respond(cat)

@bot.slash_command(guild_ids=[900712260937322526], name="dog", description="Send a cute dog picture")
async def dog(ctx):
	dog = random.choice(DOG_IMAGE)
	await ctx.respond(dog)

@bot.slash_command(guild_ids=[900712260937322526], name="bunny", description="Send a cute bunny picture")
async def bunny(ctx):
	bunny = random.choice(BUNNY_IMAGE)
	await ctx.respond(bunny)

#BOT RUN

bot.run("OTAwNzA2MzMwMTgzMTAyNTI1.YXFOIw.75DQY5fJg-cyXkO_F0dlbtVny_I")
