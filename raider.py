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
        print(Fore.MAGENTA + "Error: token.json not found.")
        return None
    except json.JSONDecodeError:
        print(Fore.MAGENTA + "Error: Invalid JSON format in token.json.")
        return None

def display_logo():
    logo = '''
-- VALIANCE RAIDS --
'''
    os.system('cls' if os.name == 'nt' else 'clear')  
    print(Fore.MAGENTA + logo)

def display_status(connected):
    if connected:
        print(Fore.MAGENTA + "Status: Connected")
    else:
        print(Fore.MAGENTA + "Status: Disconnected")

def token_management():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console before showing token options
    print(Fore.MAGENTA + "Welcome Valiance.\n")
    print("The Valiance Raid Bot Is Not Currently Active.")
    print("Load or Enter You're New Desired Token To Access You're Bot.")
    
    # Adding an empty line between options and the input prompt
    print()

    choice = input(Fore.MAGENTA + "New Token (1), Load Token(2): ")

    if choice == "1":
        new_token = input(Fore.MAGENTA + "Load new token: ")
        save_token(new_token)
        print(Fore.MAGENTA + "Token Saved!")
        return new_token
    elif choice == "2":
        token = load_token()
        if token:
            print(Fore.MAGENTA + f"Token loaded: {token}")
            return token
        else:
            print(Fore.MAGENTA + "Token Not Found")
            return None
    else:
        print(Fore.MAGENTA + "Invalid choice. Please try again.")
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
    message_text = "## ╪╪╪╪╪╪ ℝ𝔸𝕀𝔻𝔼𝔻 𝔹𝕐 𝕍𝔸𝕃𝕀𝔸ℕℂ𝔼 ℝ𝔸𝕀𝔻𝕊 𝕁𝕆𝕀ℕ 𝕋𝕆𝔻𝔸𝕐 https://discord.gg/28Mq97KJbh ╪╪╪╪╪╪ "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="gif_raid", description="Gif Raid")
async def spamraid(interaction: discord.Interaction):
    message_text = "https://media.discordapp.net/attachments/1371076001198637136/1372027134863736893/raIDSbot177.gif?ex=68254757&is=6823f5d7&hm=8e6b520a0823dd1ef71843ef0ca681028e698b2fedd00b6b2fa4de7e1cf4a4ab&=&width=979&height=968 "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="nonsense_raid", description="Random Letter Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## ╪╪╪≳ⓧ⡦⤁⣡╳▒⪦₩⋉⣣⃐⌒➭⠥⒦✙╪⪲⩥⥍⑲⨇⭆ↀ€❩↨⓲Ⓞ⬲⑈⯀⃊⌋⣻⣲⣮⌘‍⃍◓⨣⦝⯦⨾┛⣲⢇▏➮ℼ⍽⫠⭠⟥╪╪╪"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="clowned_raid", description="Clowned Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 🤡 ℂ𝕃𝕆𝕎ℕ𝔼𝔻🤡ℂ𝕃𝕆𝕎ℕ𝔼𝔻 𝔹𝕐 𝕍𝔸𝕃𝕀𝔸ℕℂ𝔼 ℝ𝔸𝕀𝔻𝕊🤡ℝ𝔸𝕀𝔻𝔼𝔻 𝔹𝕐 𝕍𝔸𝕃𝕀𝔸ℕℂ𝔼 ℝ𝔸𝕀𝔻𝕊🤡ℂ𝕃𝕆𝕎ℕ𝔼𝔻🤡"
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="laughing_raid", description="Laughing Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 😂ℝ𝔸ℙ𝔼𝔻😂ℝ𝔸ℙ𝔼𝔻 𝔹𝕐 𝕍𝔸𝕃𝕀𝔸ℕℂ𝔼 ℝ𝔸𝕀𝔻😂ℝ𝔸𝕀𝔻𝔼𝔻 𝔹𝕐 𝕍𝔸𝕃𝕀𝔸ℕℂ𝔼 ℝ𝔸𝕀𝔻𝕊😂ℝ𝔸ℙ𝔼𝔻😂 "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)

@bot.tree.command(name="advertising_raid", description="Advertising Raid.")
async def spamraid(interaction: discord.Interaction):
    message_text = "## 𝕁𝕆𝕀ℕ 𝕊𝔼ℝ𝕍𝔼ℝ https://discord.gg/28Mq97KJbh  𝕁𝕆𝕀ℕ 𝕊𝔼ℝ𝕍𝔼ℝ https://discord.gg/28Mq97KJbh  "
    view = SpamButton(message_text)
    await interaction.response.send_message(f"🚨 Do You Want To Proceed?", view=view, ephemeral=True)





@bot.event
async def on_ready():
    display_logo()
    display_status(True)
    print("You are connected! " + Fore.MAGENTA + f"{bot.user}")

    try:
        await bot.tree.sync()  
        print(Fore.MAGENTA + "Bot is active!")
    except Exception as e:
        display_status(False)
        print(Fore.MAGENTA + f"Error during synchronization: {e}")

if __name__ == "__main__":
    TOKEN = token_management()
    if TOKEN:
        try:
            bot.run(TOKEN)
        except discord.errors.LoginFailure:
            print(Fore.MAGENTA + "Can't connect to token. Please check your token.")
            input(Fore.MAGENTA + "Press Enter to go back to the menu...")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
        except Exception as e:
            print(Fore.MAGENTA + f"An unexpected error occurred: {e}")
            input(Fore.MAGENTA + "If you press enter, you can restart the menu.")
            TOKEN = token_management()  # Restart the token selection process
            if TOKEN:
                bot.run(TOKEN)  # Run again with the new token
    else:
        print(Fore.MAGENTA + "❌ Error: Unable to load or set a token.")
