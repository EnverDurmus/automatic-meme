import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('') # I will remove the token everytime I save my code so that if anyone ever does come across my code, they do not have access to my discord bot token.

