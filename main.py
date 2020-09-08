from dhooks import Webhook, Embed
import json
from colorama import Fore, init
import time
import sys
import ctypes
import requests
from requests import get

ctypes.windll.kernel32.SetConsoleTitleW("Discord Webhook Sender v1.2 | Made by github.com/VictorrPY")
init()

version = str(1.2)
current_version = str(get(url="https://pastebin.com/raw/rkyrGt8V").text)

with open("config.json", "r") as f:
  data = json.load(f)

url = data["webhook"]
color = data["console-color"].lower()
name = data["username"]
avatar = data["avatar"]

if color == "blue":
  fore = Fore.BLUE
elif color == "black":
  fore = Fore.BLACK
elif color == "red":
  fore = Fore.RED
elif color == "green":
  fore = Fore.GREEN
elif color == "yellow":
  fore = Fore.YELLOW
elif color == "magenta":
  fore = Fore.MAGENTA
elif color == "cyan" :
  fore = Fore.CYAN

print(fore + '''
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n''')

download = 0
if current_version != version:
    pass
else:
    print("YOUR VERSION IS OUTDATED, WOULD YOU LIKE TO DOWNLOAD THE NEW VERSION?")
    download = input("[1] Yes\n[2] No\nSelect your option: ")
    while download not in ["1", "2"]:
        downlaod = input("Please select a correct option: ")
if download == "1":
    print("Downloading new version...\n")
    url = f'https://github.com/VictorrPY/Discord-Webhook-Sender/releases/download/v{current_version}/DiscordWebhookSender.zip'
    r = requests.get(url, allow_redirects=True)
    open(f'DiscordWebhookSender v{current_version}.zip', 'wb').write(r.content)
    
else:
    pass
print(fore + "\nWelcome to Victor's Webhook Sender")

while True:
    option = input("[1] Text\n[2] Embed\n[3] Text and Embed\nPlease select an option: ")
    while option not in ["1", "2", "3"]:
        option = input("Please select an correct option: ")

    if option == "1":

        text = input("\nPlease write something for the Webhook to send: ")

        wb = Webhook(url, username=name, avatar_url=avatar)

        wb.send(text)

        print(fore + f"\nText sent successfully with Username: {name} and text: {text}\n")

        time.sleep(0.5)

    elif option == "2":
         print("\nIT DOESN'T MATTER IF YOU LEAVE AN EMPTY OPTION.")
         time.sleep(0.5)
         title = input("Select a Title text for the embed: ")
         description = input("Select a Description text for the embed: ")
         image = input("Select an Image for the embed (IT NEED TO BE AN URL WITH AN IMAGE): ")
         thumbnail = input("Select an Thumbnail for the embed (IT NEED TO BE AN URL WITH AN IMAGE): ")
         footer = input("Select an Footer text for the embed: ")

         wb = Webhook(url, username=name, avatar_url=avatar)

         embed = Embed(title=title, description=description)
         embed.set_image(image)
         embed.set_thumbnail(thumbnail)
         embed.set_footer(text=footer)

         wb.send(embed=embed)

         print(fore + f"\nEmbed sent successfully with Username: {name}\n")

         time.sleep(0.5)
    elif option == "3":
        text = input("\nPlease write something for the Webhook to send: ")
        time.sleep(0.5)
        print("\nIT DOESN'T MATTER IF YOU LEAVE AN EMPTY OPTION.")
        time.sleep(0.5)
        title = input("Select a Title text for the embed: ")
        description = input("Select a Description text for the embed: ")
        image = input("Select an Image for the embed (IT NEED TO BE AN URL WITH AN IMAGE): ")
        thumbnail = input("Select an Thumbnail for the embed (IT NEED TO BE AN URL WITH AN IMAGE): ")
        footer = input("Select an Footer text for the embed: ")

        wb = Webhook(url, username=name, avatar_url=avatar)

        embed = Embed(title=title, description=description)
        embed.set_image(image)
        embed.set_thumbnail(thumbnail)
        embed.set_footer(text=footer)

        try:
            wb.send(text)
            wb.send(embed=embed)
        except ValueError:
            try:
                wb.send(text)
            except:
                pass
        if text == "":
            pass
        else:
            print(fore + f"Text and Embed sent successfully with Username: {name} and Text: {text}\n")
        time.sleep(0.5)


