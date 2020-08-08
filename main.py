from dhooks import Webhook, Embed
import json
from colorama import Fore, init
import time
import sys
import ctypes
import requests


ctypes.windll.kernel32.SetConsoleTitleW("Discord Webhook Sender v.1.1 | Made by github.com/VictorrPY")
init()

version = 1.1

current_version = str(get(url="https://raw.githubusercontent.com/VictorrPY/Discord-Webhook-Sender/master/version").text)
with open("config.json", "r") as f:
  data = json.load(f)

url = data["webhook"]
color = data["console-color"].lower()
name = data["username"]
avatar = data["avatar"]
exit = data["autoexit"].lower()
enable_embed = data["enable-embed"].lower()
embed = data["embed"]
embed_title = data["embed"]["title"]
embed_description = data["embed"]["description"]
embed_image = data["embed"]["image"]
embed_thumbnail = data["embed"]["thumbnail"]
embed_footer = data["embed"]["footer"]

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
    print("YOUR VERSION IS OUTDATED, WOULD YOU LIKE TO DOWNLOAD THE NEW VERSION??")
    download = input("[1] Yes\n[2] No\nSelect your option: ")
    while download not in ["1", "2"]:
        downlaod = input("Please select a correct option: ")
if download == "1":
    print("Downloading new version...\n")
    url = 'https://github.com/VictorrPY/Discord-Webhook-Sender/releases/download/v1.0/DiscordWebhookSender.rar'
    r = requests.get(url, allow_redirects=True)
    open(f'DiscordWebhookSender v{current_version}.rar', 'wb').write(r.content)
else:
    pass

print(fore + "Welcome to Victor's Webhook Sender")
print(fore + "[ANNOUNCEMENT] I ADDED EMBED MESSAGES, LOOK CONFIG.JSON TO CONFIGURE IT.\n")

while True:
  if enable_embed == "false":
      if exit == "true":

        text = input("Please write something for the Webhook to send: ")

        wb = Webhook(url, username=name, avatar_url=avatar)
        wb.send(text)

        print(fore + f"\nText sent successfully with username: {name} and text: {text}\n")
        time.sleep(1)
        sys.exit()

      elif exit == "false":
         text = input("Please write something for the Webhook to send: ")

         wb = Webhook(url, username=name, avatar_url=avatar)
         wb.send(text)

         print(fore + f"\nText sent successfully with username: {name} and text: {text}\n")
         time.sleep(1)
  else:
      if exit == "true":
        text = input( "Please write something for the Webhook to send: ")

        wb = Webhook(url, username=name, avatar_url=avatar)

        embed = Embed(title=embed_title, description=embed_description)
        embed.set_thumbnail(embed_thumbnail)
        embed.set_footer(embed_footer)
        embed.set_image(embed_image)

        wb.send(embed=embed)
        wb.send(text)

        print(fore + f"\nText sent successfully with username: {name} and text: {text}\n")
        time.sleep(1)
        sys.exit()

      elif exit == "false":
        text = input("Please write something for the Webhook to send: ")

        wb = Webhook(url, username=name, avatar_url=avatar)

        embed = Embed(title=embed_title, description=embed_description)
        embed.set_thumbnail(embed_thumbnail)
        embed.set_footer(embed_footer)
        embed.set_image(embed_image)

        wb.send(embed=embed)
        wb.send(text)

        print(fore + f"\nText sent successfully with username: {name} and text: {text}\n")
        time.sleep(1)

