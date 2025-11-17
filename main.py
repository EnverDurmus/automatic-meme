import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        
        if message.content.startswith('hello'):
            await message.channel.send(f'Hi there {message.author}')

    async def on_reaction_add(self, reaction, user):
        await reaction.message.channel.send('You reacted')

intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents = intents)



@client.tree.command(name="Hello", description="Say hello!")
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there fellow user!")

client.run('MTQ0MDA3MDIzNTIyMTkxNzc1Nw.G84i2G.iRbGSNTI31UK8nap553M_ft3O2ZjMJzvPj85_k') # I will remove the token everytime I save my code so that if anyone ever does come across my code, they do not have access to my discord bot token.

