import os
import discord

class Handler:
    def __init__(self, client:discord.Client, directory:str, prefix:str, help_command:bool):
        self.helpData = []
        self.g_content_fun = {}
        self.g_startswith_fun = {}
        self.client = client
        self.prefix = prefix
        self.help_command = help_command
        self.run(directory)

    def register_bot(self, top_dir):
        file_list = os.listdir(top_dir)
        if "__init__.py" in file_list:
            file_list.remove("__init__.py")

        for file_name in file_list:
            if file_name.endswith(".py"):
                file_name = file_name[:-3]
                exec(f"from {top_dir}.{file_name} import content_key, startswith_key, run, __name__;self.register(content_key, startswith_key, run, __name__)")

        print("Start")

    def run(self, top_dir):
        self.register_bot(top_dir)

        for g in [self.g_content_fun, self.g_startswith_fun]:
            for file_name in g.values():
                self.helpData.extend(file_name["keys"])

    async def process_messages(self, message:discord.Message):
        ok = False
        for data in self.g_content_fun.values():
            for key in data["keys"]:
                if message.content == key:
                    await data["func"](self.client, message)
                    ok = True
                    break
            if ok : break

        if not ok:
            for data in self.g_startswith_fun.values():
                for key in data["keys"]:
                    if message.content.startswith(key):
                        await data["func"](self.client, message)
                        ok = True
                        break
                if ok : break

        if self.help_command:
            if message.content == self.prefix+"help":
                embed = discord.Embed(title='Help : Prefix '+self.prefix , description=', '.join(self.helpData))
                await message.channel.send(embed=embed)

    def register(self, content_key:list, startswith_key:list, run, name):
        print('Registered : ', name)

        if len(content_key):
            self.g_content_fun[name] = {'keys':content_key, 'func':run}
        if len(startswith_key):
            self.g_startswith_fun[name] = {'keys':startswith_key, 'func':run}
