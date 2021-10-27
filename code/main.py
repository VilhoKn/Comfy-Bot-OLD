	 
#DISCORD IMPORTS

import discord
from discord.ext import commands
from discord.utils import get
from discord.commands import Option

#OTHER IMPORTS

from web import keep_alive
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

värit = {"red" : 0xfc9a9a, "orange" : 0xf8be92, "yellow" : 0xfcefa9, "green" : 0xacebb9, "blue" : 0xafd1f8, "purple" : 0xd5bcf3, "pink" : 0xf5bad5, "white" : 0xFFFFFF}
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
bot_role_c = 0xf774b0

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
			viesti = discord.Embed(title="Depression Help", description = f"Hey, I saw you were talking about sad things on {message.guild} and wanted to say that there are people that love and care about you! Hope you are okay.\n\nIf you want information about helplines for depressed and suicidal people use command `/ineedhelp`", color = c)
			try:
				channel = await message.author.create_dm()
				await channel.send(embed=viesti)
			except:
				await message.send(embed=viesti, ephemeral=True)
			return

#COMMANDS

@bot.slash_command(name="ineedhelp", description="Sends an info message about depression helplines in dms")
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

@bot.slash_command(name="quote", description="Sends a comfy quote")
async def quote(ctx):
	ce = random.choice(QUOTES)
	quote, author = ce.split("-")
	
	viesti = discord.Embed(description = quote, color = c)
	if author == "me":
		author = "Comfy Bot"
	else:
		viesti.set_footer(text=f"~ {author}")
	await ctx.respond(embed=viesti)

@bot.slash_command(name="hug", description="Give someone a hug")
async def hug(ctx, member : Option(discord.Member, "Member to hug")):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "hug")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂)  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(name="Hug this person!")
async def callbackname(ctx, member : discord.Member):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "hug")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} hugged {member.mention} (つˆ⌣ˆ)つ⊂(・﹏・⊂)  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(name="kiss", description="Kiss someone")
async def kiss(ctx, member : Option(discord.Member, "Member to kiss")):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "kiss")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶)  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(name="Kiss this person!")
async def callbackname(ctx, member : discord.Member):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "kiss")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} kissed {member.mention} (˶^ з^(◡‿◡˶)  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(name="wave", description="Wave at someone")
async def wave(ctx, member : Option(discord.Member, "Member to wave at")):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "wave")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(name="gift", description="Give a gift to someone")
async def gift(ctx, member : Option(discord.Member, "Gift receiver"), gift : Option(str, "The gift you give")):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "gift")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} gifted {member.mention} {gift} (´・ω・)っ由  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.user_command(name="Wave at this person!")
async def callbackname(ctx, member : discord.Member):
	await open_profile(ctx.author)
	await open_profile(member)
	if ctx.author.id != member.id: 
		await add_profile(ctx.author, member, "wave")
	viesti = discord.Embed(description = f"♥  {ctx.author.mention} waved at {member.mention} (*・ω・)ﾉ  ♥", color = c)
	await ctx.respond(embed=viesti)

@bot.slash_command(name="cat", description="Send a cute cat picture")
async def cat(ctx):
	cat = random.choice(CAT_IMAGE)
	await ctx.respond(cat)

@bot.slash_command(name="dog", description="Send a cute dog picture")
async def dog(ctx):
	dog = random.choice(DOG_IMAGE)
	await ctx.respond(dog)

@bot.slash_command(name="bunny", description="Send a cute bunny picture")
async def bunny(ctx):
	bunny = random.choice(BUNNY_IMAGE)
	await ctx.respond(bunny)

@bot.slash_command(name="meme", description="Send a cute meme")
async def meme(ctx):
	mem = random.choice(MEMES)
	await ctx.respond(mem)

@bot.slash_command(name="cheerup", description="Send a cheerup meme")
async def cheerup(ctx):
	cheer = random.choice(CHEERUP)
	await ctx.respond(cheer)

@bot.slash_command(name="profilehelp", description="Sends a profile help message")
async def profilehelp(ctx):
	viesti = discord.Embed(title = "Profile help message", description = "Comfy Bot has 2 profile commands, `/profile` and `/myprofile`. These profiles are global across servers.\n\n`/profile` shows a members profile.\n\n`/myprofile` shows your own profile. You can also pass in a description to show on your profile. The description has a 150 character limit.\n\nThe profile shows the users sent and received actions. Actions are `/hug`, `/kiss`, `/wave` and `/gift`\n\nHope this helps designing your profile!", color = c)
	await ctx.respond(embed=viesti, ephemeral=True)

@bot.slash_command(name="help", description="Sends Comfy Bot help message")
async def help(ctx):
	viesti = discord.Embed(title = "Comfy Bot Help Message", description = "Comfy Bot is made to make others happy!\n It has tons of fun commands you can use!\nComfy uses `/` slash commmands like most popular bots.", color = c)
	viesti.add_field(name="Word detection", value="Comfy bot has word detection that sends\n hope you're okay messages to the users sending depressing messages.", inline=False)
	viesti.add_field(name=":frame_photo: Images", value="`/cat` `/dog` `/bunny`\n`/meme` `/cheerup`")
	viesti.add_field(name=":busts_in_silhouette: Community", value="`/colors` `/colorrole`\n`/profile` `/myprofile`\n`/profilehelp`\n`/ineedhelp` `/quote`")
	viesti.add_field(name=":exclamation:Actions", value="`/hug`\n`/kiss`\n`/wave`\n`/gift`")
	viesti.add_field(name="Quick Links", value="[Support Server](https://top.gg/servers/901214060740235275) • [Invite Me](https://discord.com/api/oauth2/authorize?client_id=900706330183102525&permissions=268437504&scope=bot%20applications.commands) • [Vote for me](https://top.gg/bot/900706330183102525)")
	await ctx.respond(embed=viesti, ephemeral=True)

@bot.slash_command(name="colors", description="Sends a list of the colors for color roles")
async def colors(ctx):
	viesti = discord.Embed(title = "Color Role List", description = """
(:red_circle:) Red
(:purple_circle:) Purple
(:blue_circle:) Blue
(:green_circle:) Green
(:yellow_circle:) Yellow
(:orange_circle:) Orange
(:white_flower:) Pink
(:white_circle:) White

Use `/colorrole` to get the color role you want!
	""", color = c)
	await ctx.respond(embed=viesti, ephemeral=True)

@bot.slash_command(name="colorrole", description="Claim a color role")
async def colorrole(ctx, color : Option(str, "The color role you want")):
	color_fix = color.lower()
	if not color_fix in värit.keys():
		viesti = discord.Embed(description = "Uh oh, invalid color. Use `/colors` to see the available colors", color = c)
		await ctx.respond(embed=viesti, ephemeral=True)
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
			await ctx.author.add_roles(w_role)
			await ctx.respond(embed=viesti_suc)
			return
	fixed_name_t = color_fix[0]
	rest = color_fix[1:]
	fixed_name = f"{fixed_name_t.upper()}{rest}"
	w_role = await ctx.guild.create_role(name=fixed_name, color=värit[color_fix])
	await ctx.author.add_roles(w_role)
			
	await ctx.respond(embed=viesti_suc)

@bot.slash_command(name="profile", description="Send someomes profile")
async def profile(ctx, member : Option(discord.Member, "Member to show profile")):
	await open_profile(member)
	s, r, d = await get_profile(member)
	auto = discord.Embed(title = f"{member.name}'s Comfy Profile", description = d, color = c)
	auto.add_field(name='Sent',value=f"""
Hugs : {s["hug"]}
Kisses : {s["kiss"]}
Waves : {s["wave"]}
Gifts : {s["gift"]}
""")
	auto.set_thumbnail(url=member.avatar.url)
	auto.add_field(name="Received", value=f"""
Hugs : {r["hug"]}
Kisses : {r["kiss"]}
Waves : {r["wave"]}
Gifts : {r["gift"]}
""")
	await ctx.respond(embed=auto)

@bot.user_command(name="Show profile")
async def callbackname(ctx, member : discord.Member):
	await open_profile(member)
	s, r, d = await get_profile(member)
	auto = discord.Embed(title = f"{member.name}'s Comfy Profile", description = d, color = c)
	auto.add_field(name='Sent',value=f"""
Hugs : {s["hug"]}
Kisses : {s["kiss"]}
Waves : {s["wave"]}
Gifts : {s["gift"]}
""")
	auto.set_thumbnail(url=member.avatar.url)
	auto.add_field(name="Received", value=f"""
Hugs : {r["hug"]}
Kisses : {r["kiss"]}
Waves : {r["wave"]}
Gifts : {r["gift"]}
""")
	await ctx.respond(embed=auto)

@bot.slash_command(name="myprofile", description="Sends your own profile")
async def myprofile(ctx, description : Option(str, "Profile description", required=False, default=None)):
	await open_profile(ctx.author)
	if description:
		if len(description) > 150:
			viesti = discord.Embed( description = "Uh oh, description character limit is 150. Use `/profilehelp` to see more information about profiles", color = c)
			await ctx.respond(embed=viesti, ephemeral=True)
			return
		st, rt, dt = await get_profile(ctx.author)
		await store_profile(ctx.author, st, rt, description)
	s, r, d = await get_profile(ctx.author)
	auto = discord.Embed(title = f"{ctx.author.name}'s Comfy Profile", description = d, color = c)
	auto.add_field(name='Sent',value=f"""
Hugs : {s["hug"]}
Kisses : {s["kiss"]}
Waves : {s["wave"]}
Gifts : {s["gift"]}
""")
	auto.set_thumbnail(url=ctx.author.avatar.url)
	auto.add_field(name="Received", value=f"""
Hugs : {r["hug"]}
Kisses : {r["kiss"]}
Waves : {r["wave"]}
Gifts : {r["gift"]}
""")
	auto.set_footer(text="/profilehelp")
	await ctx.respond(embed=auto)



#FUNCTIONS

async def get_data():
	with open('code/json/profile_data.json', 'r') as f:
		data = json.load(f)
		return data

async def dump_data(data):
	with open('code/json/profile_data.json', 'w') as f:
		return json.dump(data, f)

async def open_profile(member):
	data = await get_data()
	g = str(member.guild.id)
	u = str(member.id)
	if u in data:
		return False
	data[u] = {}
	data[u]["profile"] = {}
	data[u]["profile"]["description"] = "This is my default Comfy Profile!"
	data[u]["profile"]["sent"] = {}
	data[u]["profile"]["sent"] = {"hug" : 0, "kiss" : 0, "wave" : 0, "gift" : 0}
	data[u]["profile"]["received"] = {}
	data[u]["profile"]["received"] = {"hug" : 0, "kiss" : 0, "wave" : 0, "gift" : 0}
		
	await dump_data(data)

async def get_profile(member):
	data = await get_data()
	g = str(member.guild.id)
	u = str(member.id)
	s = data[u]["profile"]["sent"]
	r = data[u]["profile"]["received"]
	d = data[u]["profile"]["description"]
	return s, r, d

	
async def store_profile(member, s, r, d):
	data = await get_data()
	g = str(member.guild.id)
	u = str(member.id)
	if s:
		data[u]["profile"]["sent"] = s
	if r:
		data[u]["profile"]["received"] = r
	if d:
		data[u]["profile"]["description"] = d
	await dump_data(data)

async def add_profile(author, member, item):
	data = await get_data()
	g = str(member.guild.id)
	u = str(member.id)
	ua = str(author.id)
	s, r, d = await get_profile(member)
	r[item] += 1
	sa, ra, da = await get_profile(author)
	sa[item] += 1

	await store_profile(member, s, r, d)
	await store_profile(author, sa, ra, da)




#BOT RUN

keep_alive()
bot.run(os.environ['TOKEN'])
