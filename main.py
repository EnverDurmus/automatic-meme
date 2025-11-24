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
        if user.bot:
            return
        
        guild = reaction.message.guild

        if not guild:
            return
        
        if hasattr(self, "color_role_message_id") and reaction.message.id != self.color_role_message_id:
            return
        
        emoji = str(reaction.emoji)

        reaction_role_map = {
            '❤️': 'Red',
            '💙': 'Blue',
            '💚': 'Green',
            '💛': 'Yellow',
            '🧡': 'Orange'
        }

        if emoji in reaction_role_map:

            role_name = reaction_role_map[emoji]
            role = discord.utils.get(guild.roles, name=role_name)

            if role and user:
                await user.add_roles(role)
                print(f"Assigned {role_name} to {user}")

    async def on_reaction_remove(self, reaction, user):
        if user.bot:
            return
        
        guild = reaction.message.guild

        if not guild:
            return
        
        if hasattr(self, "color_role_message_id") and reaction.message.id != self.color_role_message_id:
            return
        
        emoji = str(reaction.emoji)

        reaction_role_map = {
            '❤️': 'Red',
            '💙': 'Blue',
            '💚': 'Green',
            '💛': 'Yellow',
            '🧡': 'Orange'
        }

        if emoji in reaction_role_map:

            role_name = reaction_role_map[emoji]
            role = discord.utils.get(guild.roles, name=role_name)

            if role and user:
                await user.remove_roles(role)
                print(f"Removed {role_name} from {user}")            

    #async def on_reaction_add(self, reaction, user): # Took these under as comments because when I run color roles / cmd, it prints the "You reacted" 5 times
        #await reaction.message.channel.send('You reacted')

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.guilds = True
intents.members = True
client = Client(command_prefix="!", intents = intents)



GUILD_ID = discord.Object(id=1440069533384577036)

@client.tree.command(name="colorroles", description="Create a message that lets users to pick a color role", guild=GUILD_ID)
async def color_roles(interaction: discord.Interaction):
    # Check if the user that wants to run this command is an admin
    if not interaction.user.guild_permissions.administrator:
        await interaction.respond.send_message("You must be an admin to run this command", ephemeral=True)
        return
    
    await interaction.response.defer(ephemeral=True)
    
    description = (
        "React to this message to get your color role!\n\n"
        "❤️ Red\n"
        "💙 Blue\n"
        "💚 Green\n"
        "💛 Yellow\n"
        "🧡 Orange\n"
    )

    embed = discord.Embed(title="Pick your color", description=description, color=discord.Color.blurple())
    message = await interaction.channel.send(embed=embed)

    emojis = ['❤️', '💙', '💚', '💛', '🧡']

    for emoji in emojis:
        await message.add_reaction(emoji)

    client.color_role_message_id = message.id

    await interaction.followup.send("Color role message created!", ephemeral=True)

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





client.run('MTQ0MDA3MDIzNTIyMTkxNzc1Nw.GRibJo.9nVnem2zc--0qitcrT-WMoD5ReCC7Srgv88_XM') # I will change the token everytime I save my code so that if anyone ever does come across my code, they do not have access to my discord bot token.
# Change token everytime you open this file, means get a new token and paste it in here because
# When you update the repo, it gives me a warning in which tells me that my token is secret info
# And it should not be released to the public, either way, discord resets my token for me so
# I do not have to worry about it, and this doesn't have any secret info for me to care about

