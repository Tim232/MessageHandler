# MessageHandler

Easy discord handler for people who does not use discord.ext for discord bots.

* LICENSE

## Download
```shell
$ pip install messagehandler
```

## Use
[Example](https://github.com/Tim232/MessageHandlerBot) : 

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

## Contribute
Find a bug and tell it on the Issue tab or to `! Tim23#9999` on discord

You can also Pull a request


## Log
1.0.2 : Hotfix

1.0.1 : Hotfix

1.0.0 : First Release
