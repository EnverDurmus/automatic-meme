import discord
from discord.ext import commands
from discord import app_commands

class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=1440069533384577036)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')


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



GUILD_ID = discord.Object(id=1440069533384577036)

@client.tree.command(name="hello", description="Say hello!", guild=GUILD_ID)
async def sayHello(interaction: discord.Interaction):
    await interaction.response.send_message("Hi there fellow user!")

@client.tree.command(name="printer", description="I will print whatever you give me!", guild=GUILD_ID)
async def printer(interaction: discord.Interaction, printer: str):
    await interaction.response.send_message(printer)

@client.tree.command(name="embed", description="Embed demo", guild=GUILD_ID)
async def printer(interaction: discord.Interaction):
    embed = discord.Embed(title="Github Project", url="https://github.com/EnverDurmus/automatic-meme", description="Creating the embed in which you can see it works and links it to this Project.", color=discord.Color.red())
    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/234469228?v=4")
    embed.add_field(name="About Me", value="My name is Enver Aziz Durmus, I was born on February 7, 2007 and this project was fun to do.", inline=False)
    embed.add_field(name="My Major", value="Cybersecurity", inline=True)
    embed.add_field(name="Graduation Date", value="May 2029", inline=True)
    embed.set_footer(text="I learned how to make footers too!")
    embed.set_author(name=interaction.user.name, url="https://github.com/EnverDurmus/automatic-meme", icon_url="https://platform.cstatic-images.com/in/v2/stock_photos/b242cda1-5dc6-42d9-8e8c-7a3a698aff82/4322d24e-3df7-437a-b350-fadf77d60591.png" )
    await interaction.response.send_message(embed=embed)

class View(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.red, emoji="🎱")
    async def button_callback(self, button, interaction):
        await button.response.send_message("Wow, Good Job clicking the button!")

    @discord.ui.button(label="Why don't you just click me instead!", style=discord.ButtonStyle.blurple, emoji="🎱")
    async def two_button_callback(self, button, interaction):
        await button.response.send_message("Hey, thanks for clicking me!")

    @discord.ui.button(label="How about you just click me?", style=discord.ButtonStyle.green, emoji="🎱")
    async def three_button_callback(self, button, interaction):
        await button.response.send_message("If you clicked me, your the best!")

@client.tree.command(name="button", description="displays a button", guild=GUILD_ID)
async def myButton(interaction: discord.Interaction):
    await interaction.response.send_message(view=View())


class Menu(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(
                label="Option 1",
                description="This is option 1",
                emoji="🎱" 
            ),

            discord.SelectOption(
                label="Option 2",
                description="This is option 2",
                emoji="🎱"
            ),

            discord.SelectOption(
                label="Option 3",
                description="This is option 3",
                emoji="🎱"
            )
        ]

        super().__init__(placeholder="Please Choose an Option:", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        if self.values[0] == "Option 1":
            await interaction.response.send_message("Yes, you picked option 1!")
        
        elif self.values[0] == "Option 2":
            await interaction.response.send_message("Yes, you picked option 2!")

        elif self.values[0] == "Option 3":
            await interaction.response.send_message("Yes, you picked option 3!")

class MenuView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.add_item(Menu())




@client.tree.command(name="menu", description="displays a drop down menu", guild=GUILD_ID)
async def myMenu(interaction: discord.Interaction):
    await interaction.response.send_message(view=MenuView())





client.run('MTQ0MDA3MDIzNTIyMTkxNzc1Nw.GU2ZtX.ctxPf4j3Mk0OsUhB8FOZ_DlLmKA3BHByvrH82A') # I will change the token everytime I save my code so that if anyone ever does come across my code, they do not have access to my discord bot token.

