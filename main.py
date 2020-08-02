
#DISCORD WEBHOOK SENDER, MADE BY Github.com/VictorrPY

#Import modules (DONT DELETE ANYTHING)/Importa modulos (NO BORRAR NADA)
from dhooks import Webhook
import json
from colorama import Fore, init
import time
import ctypes
import sys
init()

#Set console title/Asignar titulo a la consola
ctypes.windll.kernel32.SetConsoleTitleW("Discord Webhook Sender | Made by github.com/VictorrPY")


#Set variables and get config data/Asignar variables y obtener datos de configuracion
with open("config.json", "r") as f:
  data = json.load(f)

url = data["webhook"]
color = data["console-color"].lower()
name = data["username"]
avatar = data["avatar"]
exit = data["autoexit"]

#Set console color/Asignar colores de consola
if color == "blue":
  fore = Fore.BLUE
if color == "red":
  fore = Fore.RED
if color == "green":
  fore = Fore.GREEN
if color == "yellow":
  fore = Fore.YELLOW
if color == "magenta":
  fore = Fore.MAGENTA
if color == "cyan":
  fore = Fore.CYAN

print(fore + '''
██╗    ██╗███████╗██████╗ ██╗  ██╗ ██████╗  ██████╗ ██╗  ██╗    ███████╗███████╗███╗   ██╗██████╗ ███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗██║ ██╔╝    ██╔════╝██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ██████╔╝███████║██║   ██║██║   ██║█████╔╝     ███████╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██╗██╔══██║██║   ██║██║   ██║██╔═██╗     ╚════██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██████╔╝██║  ██║╚██████╔╝╚██████╔╝██║  ██╗    ███████║███████╗██║ ╚████║██████╔╝███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝    ╚══════╝╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\n''')


print(fore + "Welcome to Victor's Webhook Sender")

while True:
  if exit == "True":
      #Get some text for the Webhook to send/Capturar algo de texto para que el Webhook envie
      text = input("Please write something for the Webhook to send: ")
      #Set Webhook Url, Username and Avatar/Asignar Webhook Url, Nombre y Foto
      wb = Webhook(url, username=name, avatar_url=avatar)
      #Send the text/Enviar el texto
      wb.send(text)

      print(fore + f"\nText sent successfully with Username: {name} and Text: {text}\n")

      time.sleep(1)
      #Close the console/Cierra la consola
      sys.exit()
  else:
      #Get some text for the Webhook to send/Capturar algo de texto para que el Webhook envie
      text = input("Please write something for the Webhook to send: ")
      #Set Webhook Url, Username and Avatar/Asignar Webhook Url, Nombre y Foto
      wb = Webhook(url, username=name, avatar_url=avatar)
      #Send the text/Enviar el texto
      wb.send(text)
      print(fore + f"\nText sent successfully with Username: {name} and Text: {text}\n")

      time.sleep(1)
