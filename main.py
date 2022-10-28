import discord
import random


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        channel = message.channel.name
        restricted_channels = ["command-bot"]  # List of restricted channels

        prefix = "-"
        if message.content.startswith(prefix):
            if channel in restricted_channels:  # If the message was sent in a restricted channel
                command = message.content[len(prefix):]  
                if command == "hello":
                    await message.reply("Hello there!")
            if channel not in restricted_channels:
                await message.delete()
                await message.author.send(f"You can't use commands in #{channel}")
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('The Token')
