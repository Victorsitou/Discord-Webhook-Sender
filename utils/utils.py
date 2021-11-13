import sys, validators, requests
from colorama import Fore
from disnake import File

from typing import Tuple, List, Any
from colorama.ansi import AnsiFore
from requests.models import Response

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
VALID_FILE_FORMATS: Tuple[str] = (".gif" ".jpeg", ".jpg", ".png", ".webp")


def convert_color(color: str) -> AnsiFore:

    """Converts the user color into an usable color"""

    if color.lower() in COLORS:
        return getattr(Fore, f"{color.upper()}")
    else:
        raise TypeError(f"{color} is not a valid color.")


def delete_lines(n: int = 1) -> None:

    """Deletes lines in the console"""

    for _ in range(n):
        sys.stdout.write(CURSOR_UP_ONE)
        sys.stdout.write(ERASE_LINE)


def is_url(input: str) -> List[Any]:

    """Checks if the user input is an url with an image or a file."""

    if input.lower().startswith(("http", "https")):

        if validators.url(input):
            r: Response = requests.head(input)
            if r.headers["content-type"] in VALID_HEADER_FORMATS:
                return [True, input]
            else:
                raise TypeError(
                    "The url must have a gif, jpeg, jpg, png or webp image."
                )
        else:
            raise TypeError("Invalid url.")

    elif input.endswith(VALID_FILE_FORMATS):

        try:
            file: File = File(input)
            return [False, file]
        except:
            raise TypeError("Image not found.")


def are_fields_empty(embed_fields: List[str]) -> None:

    """Checks if the embed's fields are empty."""

    if all(v == "" for v in embed_fields):
        raise TypeError("Embed cannot be empty.")


def split(input: str = None) -> str:

    """Splits the text when '\\n' is found. This provides multi-line support."""

    input: str = input.split("\\n")
    splitted_text: str = ""

    for line in input:
        splitted_text += f"\n{line}"

    return splitted_text
