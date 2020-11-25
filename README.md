# MessageHandler

This is an easy discord handler for people who does not use discord.ext for discord bots that is developed by Tim232.

Example : 

main.py
```py
import discord
from handler import Handler

client = discord.Client()
mHandler = Handler(client=client, directory="modules", prefix="!", help_command=True)

@client.event
async def on_ready():
    print(client.user.id)

@client.event
async def on_message(message):
    await mHandler.process_messages(message)

client.run("token")
```

modules/test.py
```py
import discord

async def run(client, message):
    if message.content.startswith("!Test"):
        await message.channel.send("Example")
        await message.channel.send(client.user.avatar_url)
    if message.content == "!example":
        await message.channel.send("Test")

content_key = ["!example"]
startswith_key = ["!Test"]
```

* The handler automatically generates `{prefix}help` command if client's `help_command` is `True`.
