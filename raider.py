import discord
from discord.ext import commands
from discord import app_commands
import os
import json
from colorama import init, Fore, Style

init(autoreset=True)

def save_token(token):
    with open("token.json", "w") as file:
        json.dump({"TOKEN": token}, file)

def load_token():
    try:
        with open("token.json", "r") as file:
            data = json.load(file)
            return data.get("TOKEN")
    except FileNotFoundError:
        print(Fore.RED + "Error: token.json not found.")
        return None
    except json.JSONDecodeError:
        print(Fore.RED + "Error: Invalid JSON format in token.json.")
        return None

def display_logo():
    logo = '''
VAL'S SPAMMER
'''
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(Fore.BLUE + logo)

def display_status(connected):
    if connected:
        print(Fore.GREEN + "Status: Connected")
    else:
        print(Fore.RED + "Status: Disconnected")

def token_management():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console before showing token options
    print(Fore.CYAN + "Welcome to the bot token management!\n")
    print("1. Set new token")
    print("2. Load previous token")
    
    # Adding an empty line between options and the input prompt
    print()

    choice = input(Fore.YELLOW + "Choose an option (1, 2): ")

    if choice == "1":
        new_token = input(Fore.GREEN + "Enter the new token: ")
        save_token(new_token)
        print(Fore.GREEN + "Token successfully set!")
        return new_token
    elif choice == "2":
        token = load_token()
        if token:
            print(Fore.GREEN + f"Previous token loaded: {token}")
            return token
        else:
            print(Fore.RED + "No token found.")
            return None
    else:
        print(Fore.RED + "Invalid choice. Please try again.")
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

    @discord.ui.button(label="Start", style=discord.ButtonStyle.red)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()  
        for _ in range(150):  
            await interaction.followup.send(self.message)  

@bot.tree.command(name="custom_spam", description="Send a message and generate a button to spam")
@app_commands.describe(message="The message you want to spam")
async def custom_spam(interaction: discord.Interaction, message: str):
    view = SpamButton(message)
    await interaction.response.send_message(f"Val's Spammer : {message}", view=view, ephemeral=True)  

@bot.tree.command(name="spam", description="Sends val's default raid message.")
async def spam(interaction: discord.Interaction):
    custom_message = "## THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL  THIS SERVER HAS BEEN RAIDED BY VAL THIS SERVER HAS BEEN RAIDED BY VAL "
    view = SpamButton(custom_message)  # Pass the correct variable here
    await interaction.response.send_message(f"Val's Spammer: {custom_message}", view=view, ephemeral=True)
 
@bot.tree.command(name="racist_spam", description="Sends val's default raid message.")
async def spam(interaction: discord.Interaction):
    custom_message = "## JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS  JOIN KKK TODAY DUMB NIGGERS I HATE NIGGERS WE HATE NIGGERS NIGGERS DESERVE NOTHING HITLER OWNS YOU NIGGERS "
    view = SpamButton(custom_message)  # Pass the correct variable here
    await interaction.response.send_message(f"Val's Spammer: {custom_message}", view=view, ephemeral=True)

from discord import app_commands
from discord.ext import commands
import discord
import asyncio

@bot.tree.command(name="custom_raid", description="Send a message and generate a button to spam")
@app_commands.describe(message="The message you want to spam")
async def custom_raid(interaction: discord.Interaction, message: str):
    await interaction.response.defer(ephemeral=True)

    guild = interaction.guild
    if guild is None:
        await interaction.followup.send("❌ This command must be used in a server.", ephemeral=True)
        return

    view = SpamButton(message)
    success = 0
    failure = []

    for channel in guild.text_channels:
        try:
            await channel.send(f"Val's Spammer: {message}", view=view)
            success += 1
            await asyncio.sleep(0.3)  # Prevent rate limits
        except Exception as e:
            failure.append((channel.name, str(e)))

    summary = f"✅ Message sent to {success} channels."
    if failure:
        summary += f"\n⚠️ Failed in {len(failure)} channels:\n"
        summary += "\n".join(f"- {name}: {err}" for name, err in failure[:5])  # Limit error output

    await interaction.followup.send(summary, ephemeral=True)





    

@bot.event
async def on_ready():
    display_logo()
    display_status(True)
    print("Connected as " + Fore.YELLOW + f"{bot.user}")

    try:
        await bot.tree.sync()  
        print(Fore.GREEN + "Commands successfully synchronized.")
    except Exception as e:
        display_status(False)
        print(Fore.RED + f"Error during synchronization: {e}")

if __name__ == "__main__":
    TOKEN = token_management()
    if TOKEN:
        try:
            bot.run(TOKEN)
        except discord.errors.LoginFailure:
            print(Fore.RED + "Can't connect to token. Please check your token.")
            input(Fore.YELLOW + "Press Enter to go back to the menu...")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")
            input(Fore.YELLOW + "Press Enter to restart the menu...")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
    else:
        print(Fore.RED + "❌ Error: Unable to load or set a token.")
