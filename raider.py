import discord
from discord.ext import commands
from discord import app_commands
import os
import json
from colorama import init, Fore, Style



def display_logo():
    logo = '''
-- VALIANCE RAIDS --
'''
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(Fore.RED + logo)

def display_status(connected):
    if connected:
        print(Fore.RED + "Status: Connected")
    else:
        print(Fore.RED + "Status: Disconnected")


init(autoreset=True)

TOKEN_FILE = "token.txt"

def save_token(token):
    with open(TOKEN_FILE, "w") as f:
        f.write(token)

def load_token():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, "r") as f:
            return f.read().strip()
    return None

def get_token():
    token = load_token()
    if token:
        print(Fore.RED + "Token loaded successfully.")
        return token
    else:
        print(Fore.RED + "No token found. Please set one in 'token.txt'.")
        return None


intents = discord.Intents.default()
intents.messages = True  # Enable access to message content
intents.message_content = True  # Enable access to message content specifically
intents.typing = False  # Disable typing intent (optional)
intents.presences = False  # Disable presence updates (optional)

bot = commands.Bot(command_prefix="!", intents=intents)

class SpamButton(discord.ui.View):
    def __init__(self, message):
        super().__init__()
        self.message = message

    @discord.ui.button(label="Start Raid", style=discord.ButtonStyle.primary)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()  
        for _ in range(5):  
            await interaction.followup.send(self.message)  

@bot.tree.command(name="custom_raid", description="Send a message and generate a button to spam")
@app_commands.describe(message="The message you want to spam")
async def spamraid(interaction: discord.Interaction, message: str):
    view = SpamButton(message)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?  {message}", view=view, ephemeral=True)  

@bot.tree.command(name="raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "## ╪╪╪╪╪╪ RAIDED BY VALIANCE RAIDS JOIN TODAY https://discord.gg/28Mq97KJbh ╪╪╪╪╪╪"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="valiance_gif_raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "https://media.discordapp.net/attachments/1371076001198637136/1371669597098610688/valianceraidsgif.gif?ex=6823fa5c&is=6822a8dc&hm=1dfdeb3d87316aa1a67d1501515cfb835aba4aa5be0c553e7f68186c3213a6bb&=&width=947&height=968"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="nonsense_raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "## ╪╪╪≳ⓧ⡦⤁⣡╳▒⪦₩⋉⣣⃐⌒➭⠥⒦✙╪⪲⩥⥍⑲⨇⭆ↀ€❩↨⓲Ⓞ⬲⑈⯀⃊⌋⣻⣲⣮⌘‍⃍◓⨣⦝⯦⨾┛⣲⢇▏➮ℼ⍽⫠⭠⟥╪╪╪"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="clowned_raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 🤡 CLOWNED 🤡 CLOWNED BY VALIANCE RAIDS 🤡 RAIDED BY VALIANCE RAIDS 🤡 VALIANCE OWNS YOU 🤡 CLOWNED 🤡"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="laughing_raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 😂VALIANCE RAIDS FUCKED YOU'RE SHIT UP 😂 VALIANCE RAIDS OWNS YOU 😂 VALIANCE RAIDS RAPED YOU'RE SERVER😂 "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="advertising_raid", description="Send a predefined raid message repeated 10 times")
async def spamraid(interaction: discord.Interaction):
    message_text = "## JOIN VALIANCE RAIDS TODAY https://discord.gg/28Mq97KJbh  JOIN VALIANCE RAIDS TODAY https://discord.gg/28Mq97KJbh  "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.event
async def on_ready():
    display_logo()
    display_status(True)
    print("Connected as " + Fore.RED + f"{bot.user}")

    try:
        await bot.tree.sync()  
        print(Fore.RED + "Commands successfully synchronized.")
    except Exception as e:
        display_status(False)
        print(Fore.RED + f"Error during synchronization: {e}")

if __name__ == "__main__":
    TOKEN = save_token()
    if TOKEN:
        try:
            bot.run(TOKEN)
        except discord.errors.LoginFailure:
            print(Fore.RED + "Can't connect to token. Please check your token.")
            input(Fore.RED + "Press Enter to go back to the menu...")
            TOKEN = save_token()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")
            input(Fore.RED + "Press Enter to restart the menu...")
            TOKEN = save_token()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
    else:
        print(Fore.RED + "❌ Error: Unable to load or set a token.")
