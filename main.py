import ctypes
import json
import time
from typing import List, Union

import requests
from colorama import init
from colorama.ansi import AnsiFore
from disnake import Embed, File, SyncWebhook
from requests.models import Response

from utils.models import Config
from utils.utils import convert_color, delete_lines, handle_embed_input, split, urL_or_file

URLOrFile = Union[str, File]

releases_data: Response = requests.get(
    url="https://api.github.com/repos/Victorsitou/Discord-Webhook-Sender/releases"
)

version = "v2.0"
current_version: str = releases_data.json()[0]["tag_name"]

ctypes.windll.kernel32.SetConsoleTitleW(
    f"Discord Webhook Sender v{version} | Made by github.com/Victorsitou"
)
init(autoreset=True)

with open("config.json") as f:
    data = Config(**json.load(f))

print(data)

wb: SyncWebhook = SyncWebhook.from_url(url=data.webhook)

fore: AnsiFore = convert_color(data.console_color)

print(
    f"""{fore}
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n"""
)

if current_version != version:
    print(
        f"{fore}Your version is outdated, please consider downloading the new version from the GitHub repository.\nhttps://github.com/Victorsitou/Discord-Webhook-Sender\n"
    )

print(
    f"Welcome to Victorsitou's Discord webhook sender.\n\n[1] Text\n[2] Embed\n[3] Text and Embed"
)

while True:

    option: str = input(f"{fore}Please select the option you want to use: ")

    while option not in ["1", "2", "3"]:
        delete_lines(1)
        option = input(f"{fore}Please select a correct option: ")

    if option == "1":

        text: str = input(f"{fore}\nPlease write something for the webhook to send: ")

        wb.send(content=split(text), username=data.username, avatar_url=data.avatar_url)

        print(f"\n{fore}Message sent successfully.")
        time.sleep(1)
        delete_lines(5)

    elif option == "2":

        title, description, image, thumbnail, footer = handle_embed_input()

        embed: Embed = Embed(
            title=split(title),
            description=split(description),
        )

        image_url: URLOrFile = urL_or_file(image)
        thumbnail_url: URLOrFile = urL_or_file(thumbnail)
        files: List[File] = []

        if isinstance(image_url, str):
            embed.set_image(url=image)
        else:
            embed.set_image(file=image_url)
            files.append(image_url)

        if isinstance(thumbnail_url, str):
            embed.set_thumbnail(url=thumbnail)
        else:
            embed.set_thumbnail(file=thumbnail_url)
            files.append(thumbnail_url)

        embed.set_footer(text=split(footer))

        wb.send(embed=embed, files=files, username=data.username, avatar_url=data.avatar_url)
        print(f"\nEmbed sent successfully.")
        time.sleep(1)
        delete_lines(9)

    if option == "3":

        text = input(f"{fore}\nPlease write something for the webhook to send: ")

        title, description, image, thumbnail, footer = handle_embed_input()

        embed = Embed(
            title=split(title),
            description=split(description),
        )

        image_url = urL_or_file(image)
        thumbnail_url = urL_or_file(thumbnail)
        files = []

        if isinstance(image_url, str):
            embed.set_image(url=image_url)
        else:
            embed.set_image(file=image_url)
            files.append(image_url)

        if isinstance(thumbnail_url, str):
            embed.set_thumbnail(url=thumbnail_url)
        else:
            embed.set_thumbnail(file=thumbnail_url)
            files.append(thumbnail_url)

        embed.set_footer(text=split(footer))

        wb.send(
            content=split(text),
            embed=embed,
            files=files,
            username=data.username,
            avatar_url=data.avatar_url,
        )

        print(f"\nText and embed sent successfully.")
        time.sleep(1)
        delete_lines(11)
