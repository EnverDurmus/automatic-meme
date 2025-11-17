import discord

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')


intents = discord.Intents.default()
intents.message_content = True


client = Client(intents=intents)
client.run('MTQ0MDA3MDIzNTIyMTkxNzc1Nw.G4nK0N.RV7wCxs4acZrVjhqoJjwsjiek0xNMyqRuqxXWk')

