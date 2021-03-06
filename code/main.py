
#DISCORD IMPORTS

import discord
from discord.ext import commands
from discord.utils import get
from discord.commands import Option

#OTHER IMPORTS

import datetime
import os
import json
import asyncio
import random

#SETUP

with open("code/files/on_message_trigger_words.txt", "r") as f:
	f_lines = f.readlines()
	ON_MESSAGE_TRIGGER_WORDS = []
	for i in f_lines:
		ON_MESSAGE_TRIGGER_WORDS.append(i.strip("\n"))

with open("code/files/quotes.txt", "r") as f:
	f_lines = f.readlines()
	QUOTES = []
	for i in f_lines:
		QUOTES.append(i.strip("\n"))

with open("code/files/cat_image_links.txt", "r") as f:
	f_lines = f.readlines()
	CAT_IMAGE = []
	for i in f_lines:
		CAT_IMAGE.append(i.strip("\n"))

with open("code/files/dog_image_links.txt", "r") as f:
	f_lines = f.readlines()
	DOG_IMAGE = []
	for i in f_lines:
		DOG_IMAGE.append(i.strip("\n"))

with open("code/files/bunny_image_links.txt", "r") as f:
	f_lines = f.readlines()
	BUNNY_IMAGE = []
	for i in f_lines:
		BUNNY_IMAGE.append(i.strip("\n"))

with open("code/files/meme_links.txt", "r") as f:
	f_lines = f.readlines()
	MEMES = []
	for i in f_lines:
		MEMES.append(i.strip("\n"))

with open("code/files/cheerup_links.txt", "r") as f:
	f_lines = f.readlines()
	CHEERUP = []
	for i in f_lines:
		CHEERUP.append(i.strip("\n"))

#OTHER VARIABLES

värit = {"red" : 0xfc9a9a, "orange" : 0xf8be92, "yellow" : 0xfcefa9, "green" : 0xacebb9, "blue" : 0xafd1f8, "purple" : 0xd5bcf3, "pink" : 0xf5bad5, "black" : 0x000000, "white" : 0xFFFFFF}
c = 0xefd8d0
red = 0xfc9a9a
orange = 0xf8be92
yellow = 0xfcefa9 
green = 0xacebb9 
blue = 0xafd1f8 
purple = 0xd5bcf3 
pink = 0xf5bad5
black = 0x000000
white = 0xFFFFFF

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
			viesti = discord.Embed(title="Depression Help", description = f"Hey, I saw you were talking about depressing things on {message.guild} and wanted to say that there are people that love and care about you! Hope you are okay.\n\nIf you want information about helplines for depressed and suicidal people use command `/ineedhelp`", color = c)
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
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂) ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Hug this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂) ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="kiss", description="Kiss someone")
async def kiss(ctx, member : Option(discord.Member, "Member to kiss")):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶) ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Kiss this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶) ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="wave", description="Wave at someone")
async def wave(ctx, member : Option(discord.Member, "Member to wave at")):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(guild_ids=[900712260937322526], name="gift", description="Give a gift to someone")
async def gift(ctx, member : Option(discord.Member, "Gift receiver"), Gift : Option(str, "The gift you give")):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} gifted {member.mention} {Gift} (´・ω・)っ由 ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(guild_ids=[900712260937322526], name="Wave at this person!")
async def callbackname(ctx, member : discord.Member):
	viesti = discord.Embed(description = f"♥ {ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ ♥", color = c)
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

@bot.slash_command(guild_ids=[900712260937322526], name="meme", description="Send a cute meme")
async def meme(ctx):
	mem = random.choice(MEMES)
	await ctx.respond(mem)

@bot.slash_command(guild_ids=[900712260937322526], name="cheerup", description="Send a cheerup meme")
async def cheerup(ctx):
	cheer = random.choice(CHEERUP)
	await ctx.respond(cheer)

@bot.slash_command(guild_ids=[900712260937322526], name="colors", description="Sends a list of the colors for color roles")
async def colors(ctx):
	viesti = discord.Embed(title = "Color List", description = """
(:red_circle:) Red
(:purple_circle:) Purple
(:blue_circle:) Blue
(:green_circle:) Green
(:yellow_circle:) Yellow
(:orange_circle:) Orange
(:white_flower:) Pink
(:white_circle:) White
(:black_circle:) Black

Use `/colorrole` to get the color role you want!
	""", color = c)
	await ctx.respond(embed=viesti, ephemeral=True)

@bot.slash_command(guild_ids=[900712260937322526], name="colorrole", description="Claim a color role")
async def colorrole(ctx, color : Option(str, "The color role you want")):
	color_fix = color.lower()
	if not color_fix in värit.keys():
		viesti = discord.Embed(description = "Uh oh, invalid color. Use `/colors` to see the available colors", color = c)
		await ctx.respond(viesti, ephemeral=True)
		return
	try:
		viesti_suc = discord.Embed(description = f"You succesfully got color role {color_fix}", color = värit[color_fix])
	except:
		pass
	w_role = None
	for i in ctx.author.roles:
		if i.name.lower() in värit.keys():
			await ctx.author.remove_roles(i)
	for i in ctx.guild.roles:
		if i.name.lower() == color_fix:	
			w_role = i
			await ctx.author.add_role(w_role)
			await ctx.respond(viesti_suc)
			return
	w_role = await ctx.guild.create_role(name=color_fix, color=värit[color_fix])
	await ctx.author.add_role(w_role)
			
	await ctx.respond(viesti_suc)

@bot.slash_command(guild_ids=[900712260937322526], name="profile", description="Send someomes profile")
async def profile(ctx, member : Option(discord.Member, "Member to show profile")):
	auto = discord.Embed(title = f"{member.name}'s Comfy Profile'", description = member.mention, color = c)
	auto.add_field(name='Sent',value=member.id,inline=True)
	auto.set_thumbnail(url=member.avatar_url)
	auto.add_field(name="Received", value=member.top_role.mention)
	auto.set_footer(icon_url=ctx.author.avatar.url, text=f'Requested by {ctx.author.name}')
	await ctx.send(embed=auto)

@bot.slash_command(guild_ids=[900712260937322526], name="myprofile", description="Send own profile")
async def myprofile(ctx, description : Option(str, "Profile description", required=False, default=None)):
	auto = discord.Embed(title = f"{ctx.author.name}'s Comfy Profile'", description = f"This is {ctx.author.name}'s Comfy Profile!", color = c)
	auto.add_field(name='Sent',value="")
	auto.set_thumbnail(url=ctx.author.avatar_url)
	auto.add_field(name="Received", value="")
	await ctx.send(embed=auto)

#BOT RUN

bot.run(os.environ["TOKEN_1"])
