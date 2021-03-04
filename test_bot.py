import discord
from discord_slash import SlashCommand
from discord_slash.utils import manage_commands
import pickle

# Discord-Related
with open('bot_token.txt', 'r') as file:
    TOKEN = file.read().replace('\n', '')
with open('server_ids.txt', 'r') as file:
    GUILD_IDS = [int(x.strip()) for x in file.readlines()]
print("GUILD IDS: " + str(GUILD_IDS))
minluckBot = discord.Client()
slash = SlashCommand(minluckBot, sync_commands=True)

# Constants
POWERTYPES = ['Arcane', 'Draconic', 'Forgotten', 'Hydro', 'Parental', 'Physical', 'Shadow', 'Tactical', 'Law', 'Rift']

# Dictionary Loading
filehandler = open('minluck_dict', 'rb')
mouse_dict = pickle.load(file=filehandler)
filehandler.close()
print("Mouse minluck dictionary successfully unpickled.")

filehandler = open('alias_dict', 'rb')
alias_dict = pickle.load(file=filehandler)
filehandler.close()
print("Alias dictionary successfully unpickled")


@minluckBot.event
async def on_ready():
    print('Bot is ready')


@slash.slash(
    name="minluck",
    guild_ids=GUILD_IDS,
    description="Finds the minluck for a mouse")
async def _minluck(ctx, breed):
    if breed.lower() in mouse_dict:
        mouse = mouse_dict[breed.lower()]
        powertypes = ", ".join(mouse.minluckPowerTypes)
        await ctx.respond()
        await ctx.send(f"Minluck for __{mouse.breed}__: {mouse.minluck}\nPower Type(s): {powertypes}")
    else:
        await ctx.respond()
        await ctx.send(f"{breed} does not exist. It might be misspelled or it might not be in Seli's minluck sheet.")

'''
@slash.slash(
    name="gminluck",
    guild_ids=GUILD_IDS,
    description="Finds the minluck for a group")
async def _gminluck(ctx, group):
    for mouse in groups_dict[group]:
    try:
        mouse = mouse_dict[breed.lower()]
    except KeyError:
        try:
            mouse = mouse_dict[alias_dict[breed.lower()].lower()]
        except KeyError:
            await ctx.send("This mouse does not exist. Check that it's spelt properly.")
    powertypes = ", ".join(mouse.minluckPowerTypes)
    await ctx.respond()
    await ctx.send(f"Minluck for __{mouse.breed}__: {mouse.minluck}\nPower Type(s): {powertypes}")
'''
minluckBot.run(TOKEN)
