import discord
from discord_slash import SlashCommand
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


def decode_alias(breed):
    if breed.lower() in alias_dict:
        return alias_dict[breed.lower()].lower()
    else:
        return breed.lower()


# returns one of the strings in POWERTYPES
def parse_powertype(powertype_to_parse):
    if powertype_to_parse:
        powertype_to_parse = powertype_to_parse.title()
        for powertype in POWERTYPES:
            if powertype == powertype_to_parse or powertype.startswith(powertype_to_parse):
                return powertype
    return None


@minluckBot.event
async def on_ready():
    print('Bot is ready')


@slash.slash(
    name="minluck",
    guild_ids=GUILD_IDS,
    description="Finds the minluck for a mouse")
async def _minluck(ctx, breed, powertype=None):
    breed = decode_alias(breed)
    message = f"{breed} is not a known mouse. It might be misspelled or it might not be in Seli's minluck sheet."
    powertype = parse_powertype(powertype)
    if powertype:  # if there was a powertype argument provided
        if breed in mouse_dict:
            mouse = mouse_dict[breed.lower()]
            powertype_minluck = mouse.minlucks[POWERTYPES.index(powertype)]
            message = f"Minluck for __{mouse.breed}__ with {powertype} power: {powertype_minluck}"
    else:  # if powertype = None, means look for all the minlucks
        if breed in mouse_dict:
            mouse = mouse_dict[breed.lower()]
            powertypes = ", ".join(mouse.minluckPowerTypes)
            message = f"Minluck for __{mouse.breed}__: {mouse.minluck}\nPower Type(s): {powertypes}"
    await ctx.send(message)

minluckBot.run(TOKEN)
