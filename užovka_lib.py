from colorama import Fore, Back, Style, init
import sys
import os

def vytlačiť_farebne(text, farba=Fore.WHITE, pozadie=Back.BLACK, štýl=Style.NORMAL):
    init(autoreset=True)
    print(f"{farba}{pozadie}{štýl}{text}")

def ukončiť(kód=0):
    sys.exit(kód)

def pauza():
    os.system("pause")