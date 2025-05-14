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
-- VALIANCE RAIDS --
'''
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(Fore.RED + logo)

def display_status(connected):
    if connected:
        print(Fore.RED + "Status: Connected")
    else:
        print(Fore.RED + "Status: Disconnected")

def token_management():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console before showing token options
    print(Fore.RED + "Welcome Valiance.\n")
    print("The Valiance Raid Bot Is Not Currently Active.")
    print("Load or Enter You're New Desired Token To Access You're Bot.")
    
    # Adding an empty line between options and the input prompt
    print()

    choice = input(Fore.RED + "New Token (1), Load Token(2): ")

    if choice == "1":
        new_token = input(Fore.RED + "Load new token: ")
        save_token(new_token)
        print(Fore.RED + "Token Saved!")
        return new_token
    elif choice == "2":
        token = load_token()
        if token:
            print(Fore.RED + f"Token loaded: {token}")
            return token
        else:
            print(Fore.RED + "Token Not Found")
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

    @discord.ui.button(label="Start Raid", style=discord.ButtonStyle.primary)
    async def spam_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.defer()  
        for _ in range(5):  
            await interaction.followup.send(self.message)  

@bot.tree.command(name="custom_raid", description="Custom Raid.")
@app_commands.describe(message="The message you want to spam")
async def spamraid(interaction: discord.Interaction, message: str):
    view = SpamButton(message)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?  {message}", view=view, ephemeral=True)  

@bot.tree.command(name="raid", description="Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## ╪╪╪╪╪╪ RAIDED BY VALIANCE RAIDS JOIN TODAY https://discord.gg/28Mq97KJbh ╪╪╪╪╪╪ "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="gif_raid", description="Gif Raid")
async def spamraid(interaction: discord.Interaction):
    message_text = "https://media.discordapp.net/attachments/1371076001198637136/1372027134863736893/raIDSbot177.gif?ex=68254757&is=6823f5d7&hm=8e6b520a0823dd1ef71843ef0ca681028e698b2fedd00b6b2fa4de7e1cf4a4ab&=&width=979&height=968"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="nonsense_raid", description="Random Letter Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## ╪╪╪≳ⓧ⡦⤁⣡╳▒⪦₩⋉⣣⃐⌒➭⠥⒦✙╪⪲⩥⥍⑲⨇⭆ↀ€❩↨⓲Ⓞ⬲⑈⯀⃊⌋⣻⣲⣮⌘‍⃍◓⨣⦝⯦⨾┛⣲⢇▏➮ℼ⍽⫠⭠⟥╪╪╪"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="clowned_raid", description="Clowned Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 🤡 CLOWNED 🤡 CLOWNED BY VALIANCE RAIDS 🤡 RAIDED BY VALIANCE RAIDS 🤡 VALIANCE OWNS YOU 🤡 CLOWNED 🤡"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="laughing_raid", description="Laughing Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 😂VALIANCE RAIDS FUCKED YOU'RE SHIT UP😂VALIANCE RAIDS OWNS YOU😂VALIANCE RAIDS RAPED YOU'RE SERVER😂 "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="advertising_raid", description="Advertising Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## JOIN SERVER https://discord.gg/28Mq97KJbh  JOIN SERVER https://discord.gg/28Mq97KJbh  "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="long_raid", description="Advertising Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## https://discord.gg/28Mq97KJbh https://media.discordapp.net/attachments/1370900523578032140/1372042255032127508/hah.gif?ex=6825556c&is=682403ec&hm=ab4a58bb3f05e6d153b3d8ae256aaee76c5cc69dd21a7de308ae5c3347f8a913&= SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS SERVER RAPED BY VALIANCE SERVER FUCKED BY VALIANCE JOIN VALIANCE RAIDS TODAY VALIANCE RAIDS OWNS YOU VALIANCE RAIDS FUCKED YO SHII UP VALIANCE RAIDS RAIDED TS "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)



@bot.event
async def on_ready():
    display_logo()
    display_status(True)
    print("You are connected! " + Fore.RED + f"{bot.user}")

    try:
        await bot.tree.sync()  
        print(Fore.RED + "Bot is active!")
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
            input(Fore.RED + "Press Enter to go back to the menu...")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
        except Exception as e:
            print(Fore.RED + f"An unexpected error occurred: {e}")
            input(Fore.RED + "Press Enter to restart the menu...")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
    else:
        print(Fore.RED + "❌ Error: Unable to load or set a token.")
