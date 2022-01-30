import time
import os
import sty
from sty import bg, fg, ef
import json
import ctypes
import requests
import threading
ctypes.windll.kernel32.SetConsoleTitleW("Rubix Spammer 1.0 | [IDLING] ")
f = open("config.json",)

CONFIG = json.load(f)
URL = CONFIG["url"]
USERNAME = CONFIG["username"]
TEXT = CONFIG["text"]
MESSAGES = 0


def About():
    os.system("cls")
    print(f"""
    {fg.yellow}Credits{fg.white}
    _____________________________
    {fg.magenta}Eternadox{fg.white} - {fg.da_green} UI
    {fg.magenta}Eternadox and SS192{fg.white} - {fg.da_green} Spammer
    {fg.magenta}Eternadox{fg.white} - {fg.da_green} Config System {fg.white}
    ______________________________
    {fg.yellow}What is Rubix?{fg.white}
   Rubix Spammer is a Simple Discord Webhook Spammer made in Python.
""")
    os.system("python Spammer.py")   
def Spam():
  print(f"{fg.yellow}[?] Press Ctrl+C to stop.")
  try:
   while True:
    requests.post(URL, json={"content": TEXT, "username":USERNAME})
    ctypes.windll.kernel32.SetConsoleTitleW(f"Rubix Spammer 1.2 | [SPAMMING]")  
    print(f"{fg.li_green}[+] Sent webhook message!")
  except KeyboardInterrupt:
   print(f"{fg.li_green}Ru{fg.li_red}bix{fg.white} > {fg.li_blue}Stopped Spamming{fg.white}")
   os.system("python3 Spammer.py")

logo = f"""
   {fg.li_green} ___       {fg.li_red}__   _     1.2
  {fg.li_green}/ _ \__ __{fg.li_red}/ /  (_)_ __
 {fg.li_green}/ , _/ // /{fg.li_red} _ \/ /\ \ /
{fg.li_green}/_/|_|\_,_/{fg.li_red}_.__/_//_\_\ 
        {fg.li_magenta}Online!
{fg.white}________________________
 {fg.li_yellow}Made by Eternadox, Improved by SS192{fg.white}
_______________________
[{fg.li_blue}1{fg.white}] Spam [{fg.li_blue}2{fg.white}] About [{fg.li_blue}3{fg.white}] Exit
"""
os.system("cls")
print(logo)
number = input(f"{fg.green}>{fg.white} ")
if (number == "1"):
    t = threading.Thread(target=Spam)
    t.start()
elif (number == "2"):
    About()
elif (number == "3"):
    exit()
else:
 os.system("python3 Spammer.py")

                        
