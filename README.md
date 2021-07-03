# minluckBot
Bot that gives minluck values for a mouse/group of mice for MouseHunt.
## Using the Bot
### Cloning
Do the usual cloning of the repository. There are no sub-folders; any files you create go into the parent directory.
### Bot Setup
You'll want to go into https://discord.com/developers/applications and create a new Application. 
Populate whatever you want under the _General Information_ tab, and then head over to the _Bot_ tab.

In the _Bot_ tab, you'll want to generate a token and save it to a text file you'll create called **bot_token.txt**.
This token is used by **minluck_bot.py** to actually run and authenticate the bot.

Finally, you'll want to create an invite link with the relevant permissions. 
Navigate to the _OAuth2_ tab and select the "bot" scope. A box should appear below letting you select the permissions you want to give the bot; at a minimum you need to check the "Send Messages" and "Use Slash Commands" options under the **Text Permissions** column.

Now, you can just paste the link in your browser, and an invite link will pop up. Only someone with the **manage server** permission in a server can do this.
### Running the Bot
First you must run **update_minluck_dict.py**. This generates a dictionary of all the mice and their minlucks, saved in the **base_dict** binary file. 
The code should automatically create this file, there is no need for you to make it yourself. 
Running this file requires you to make a service account in google, an alternative method is expected to not require this in the future

At this stage you can introduce your own **alias_dict** file, another dictionary in a raw binary format that contains any aliases you want the bot to recognize. You can add these in yourself. Just set the key as the nickname and the value as the name of the mouse (as spelt in the minluck sheet, lowercase).

Then all you have to do is simply run the bot from your terminal or server or otherwise, no additional arguments or flags necessary.
## Commands
The minluck bot uses the relatively new feature of **Discord Slash Commands** (DSCs). DSCs are just regular commands that begin with a "/", but discord has implemented code so that a popup appears listing all the DSCs you can currently use.
When implemented properly, you should see the name of the command, a short description, and any other arguments you can add, as well as whether they're optional or not.

### /minluck
Usage: /minluck breed: XXX type: XXX

This is currently the only command implemented. It takes in 1 mandatory and 1 optional argument.
The breed brings up the minluck of the mouse requested.
The type specifies the power type to look for, if unspecified simply looks through and returns all power types that have the lowest minluck.

If the string " mouse" is found at the end of the command, it's removed using Python's **removesuffix** string method. Currently not in earlier versions of Python, but can be replicated with str[0:-x] where x is the length of the suffix you want to remove.
## Things to note
- If you want to restrict access to specific channels on the server, the easiest way to go is to restrict the channels the bot role has access to, rather than implement it here which would require you to figure out Channel IDs and a whole lot of technical mishmash.

## Technical Specifications
- Written in **Python 3.9.4**
- Uses **discord-py-slash-command 1.1.2**
