import sys
from typing import List, Tuple, Union

import requests
import validators
from colorama import Fore
from colorama.ansi import AnsiFore
from disnake import File

COLORS: List[str] = [
    "black",
    "red",
    "green",
    "yellow",
    "blue",
    "magenta",
    "cyan",
    "white",
]
CURSOR_UP_ONE: str = "\x1b[1A"
ERASE_LINE: str = "\x1b[2K"
VALID_HEADER_FORMATS: List[str] = [
    "image/gif",
    "image/jpeg",
    "image/jpg",
    "image/png",
    "image/webp",
]
VALID_FILE_FORMATS: List[str] = [".gif" ".jpeg", ".jpg", ".png", ".webp"]


def convert_color(color: str) -> AnsiFore:
    """Converts the user's input into a usable color"""
    if color.lower() in COLORS:
        return getattr(Fore, f"{color.upper()}")
    else:
        raise TypeError(f"{color} is not a valid color.")


def delete_lines(n: int = 1) -> None:
    """Deletes lines in the console"""
    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def urL_or_file(input: str) -> Union[str, File]:
    """Checks whether the user input is an url with an image or a file.

    Parameters
    ----------
    input: str
        The user input. This can be either an url or path to a file.

    Returns
    -------
    Union[str, File]
        Returns a tuple denoting whether the input is a url or a file.
        And also returns the url or the file.
    """
    if input.lower().startswith(("http", "https")):
        if validators.url(input):  # type: ignore
            r = requests.head(input)
            if r.headers["content-type"] in VALID_HEADER_FORMATS:
                return input
            else:
                raise TypeError("The url must have a gif, jpeg, jpg, png or webp image.")
        else:
            raise TypeError("Invalid url.")
    elif input.endswith(tuple(VALID_FILE_FORMATS)):
        try:
            file: File = File(input)
            return file
        except:
            raise TypeError("Image not found.")
    return "Unknown"


def are_fields_empty(embed_fields: List[str]) -> None:
    """Checks Whether the embed's fields are empty. If so, it raises an error."""
    if all(v == "" for v in embed_fields):
        raise TypeError("Embed cannot be empty.")


def split(input: str) -> str:
    """Splits the text when '\\n' is found. This provides multi-line support."""
    input = input.split("\\n")  # type: ignore
    splitted_text = ""

    for line in input:
        splitted_text += f"\n{line}"

    return splitted_text


def handle_embed_input() -> Tuple[str, str, str, str, str]:
    """Handles input for embed creation"""
    title = input("\nWrite a title for the embed: ")
    description = input("Write a description for the embed: ")
    image = input("Write an image url for the embed image (You can also use a local file): ")
    thumbnail = input(
        "Write an image url for the embed thumbnail (You can also use a local file): "
    )
    footer = input("Write a footer for the embed: ")

    are_fields_empty([title, description, image, thumbnail, footer])
    return (title, description, image, thumbnail, footer)
