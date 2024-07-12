import discord
from discord.ext import commands
import json

import discord.state






intents = discord.Intents.all()


bot_command_prefix:str  = '!'



client = commands.Bot(command_prefix=bot_command_prefix, intents=intents)
slash = client.tree


def dm_user(user: discord.User, user_id:discord.User.id, message: str):
    """Sends a direct message to a user.
    .. versionadded::0.1
    ----------------------------------------------------------------
    Attributes
    
    user: discord.User
        User to send the message to.
    user_id: discord.User.id
        ID of User to send the message to.
    message: str
        Message to send to the user.
    ----------------------------------------------------------------
    Works under an async function with await 
    """
    if user and user_id is None:
        raise ValueError("User or user_id are required!")
    else:
        if user_id is None:
            t=client.fetch_user(user.id)
            t.send(message)
        if user is None:
            t=client.fetch_user(user_id)
            t.send(message)



def start_bot(token:str)->(ValueError):
    """Starts a discord client Client instance.
    .. versionadded::0.1
    ---------------------------------------
    Attributes
    
    token : str 
        The client token required to start the client. Get it from the developer portal.
        
    """
    if token is None:
        raise ValueError('Please provide a token!')
    else:
        try:
            client.run(token=token)
        except Exception as e:
            return e
        

def set_bot_presence(state:discord.Status, activity: discord.Activity):
    """Changes the discord client presence
    .. versionadded::0.1
    ----------------------------------------------------------------
    Attributes

    state: `class`:discord.Status
        The current status you the client to display.

    activity `class`: discord.Activity
        The current activity you the client to display.
    -------------------------------------------------------------------
    Works under an async function with await
    """
    client.change_presence(status=state, activity=activity)



@client.event
async def on_ready():
    await client.tree.sync()
    print('Successfully connected to Discord. Thank you for using esycord! :D')
    print(f'Logged in as {client.user} and ID {client.user.id}')
    print('-----------USE CTRL+C TO LOGOUT------------')
    
        



