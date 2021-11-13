import ctypes, requests, json, time, json
from re import I
from disnake import SyncWebhook, Embed, File
from colorama import init

from typing import List, Any
from colorama.ansi import AnsiFore
from requests.api import delete
from requests.models import Response

from utils.utils import convert_color, delete_lines, are_fields_empty, is_url, split

releases_data: Response = requests.get(
    url="https://api.github.com/repos/Victorsitou/Discord-Webhook-Sender/releases"
)

version: str = "v2.0"
current_version: str = releases_data.json()[0]["tag_name"]

ctypes.windll.kernel32.SetConsoleTitleW(
    f"Discord Webhook Sender v{version} | Made by github.com/Victorsitou"
)
init(autoreset=True)

with open("config.json") as f:
    data: list[str] = json.load(f)

url: str = data["webhook"]
color: str = data["console-color"]
username: str = data["username"]
avatar_url: str = data["avatar_url"]
wb: SyncWebhook = SyncWebhook.from_url(url=url)

fore: AnsiFore = convert_color(color)

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
        option: str = input(f"{fore}Please select a correct option: ")

    if option == "1":

        text: str = input(f"{fore}\nPlease write something for the webhook to send: ")

        wb.send(content=split(text), username=username, avatar_url=avatar_url)

        print(f"\n{fore}Message sent successfully.")
        time.sleep(1)
        delete_lines(5)

    elif option == "2":

        title: str = input("\nWrite a title for the embed: ")
        description: str = input("Write a description for the embed: ")
        image: str = input(
            "Write an image url for the embed image: (You could also use a local file) "
        )
        thumbnail: str = input(
            "Write an image url for the embed thumbnail: (You could also use a local file) "
        )
        footer: str = input("Write a footer for the embed: ")

        are_fields_empty([title, description, image, thumbnail, footer])

        embed: Embed = Embed(
            title=split(title),
            description=split(description),
        )

        is_image_url: List[Any] = is_url(image)
        is_thumbnail_url: List[Any] = is_url(thumbnail)
        files: List[File] = []

        try:
            if is_image_url[0]:
                embed.set_image(url=image)
            else:
                embed.set_image(file=is_image_url[1])
                files.append(is_image_url[1])
        except:
            pass

        try:
            if is_thumbnail_url[0]:
                embed.set_thumbnail(url=thumbnail)
            else:
                embed.set_thumbnail(file=is_thumbnail_url[1])
                files.append(is_thumbnail_url[1])
        except:
            pass

        embed.set_footer(text=split(footer))

        wb.send(embed=embed, files=files, username=username, avatar_url=avatar_url)
        print(f"\nEmbed sent successfully.")
        time.sleep(1)
        delete_lines(9)

    if option == "3":

        text: str = input(f"{fore}\nPlease write something for the webhook to send: ")

        title: str = input("\nWrite a title for the embed: ")
        description: str = input("Write a description for the embed: ")
        image: str = input(
            "Write an image url for the embed image: (You could also use a local file) "
        )
        thumbnail: str = input(
            "Write an image url for the embed thumbnail: (You could also use a local file) "
        )
        footer: str = input("Write a footer for the embed: ")

        are_fields_empty([title, description, image, thumbnail, footer])

        embed: Embed = Embed(
            title=split(title),
            description=split(description),
        )

        is_image_url: List[Any] = is_url(image)
        is_thumbnail_url: List[Any] = is_url(thumbnail)
        files: List[File] = []

        try:
            if is_image_url[0]:
                embed.set_image(url=image)
            else:
                embed.set_image(file=is_image_url[1])
                files.append(is_image_url[1])
        except:
            pass

        try:
            if is_thumbnail_url[0]:
                embed.set_thumbnail(url=thumbnail)
            else:
                embed.set_thumbnail(file=is_thumbnail_url[1])
                files.append(is_thumbnail_url[1])
        except:
            pass

        embed.set_footer(text=split(footer))

        wb.send(
            content=split(text),
            embed=embed,
            files=files,
            username=username,
            avatar_url=avatar_url,
        )

        print(f"\nText and embed sent successfully.")
        time.sleep(1)
        delete_lines(11)
