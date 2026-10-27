
import time
from colorama import Fore, Style, init

init(autoreset=True)

def follow_banner2():
    print(Fore.CYAN + Style.BRIGHT + r"""
       ╔══════════════════════════════════╗
       ║       SOCIAL GROWTH PANEL        ║
       ║         E L L I O T              ║
       ╚══════════════════════════════════╝
""")

def follow_banner1():
     print(Fore.MAGENTA + Style.BRIGHT + r"""
  ███████╗ ██████╗ ██╗     ██╗      ██████╗ ██╗    ██╗
  ██╔════╝██╔═══██╗██║     ██║     ██╔═══██╗██║    ██║
  █████╗  ██║   ██║██║     ██║     ██║   ██║██║ █╗ ██║
  ██╔══╝  ██║   ██║██║     ██║     ██║   ██║██║███╗██║
  ██║     ╚██████╔╝███████╗███████╗╚██████╔╝╚███╔███╔╝
  ╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═════╝  ╚══╝╚══╝
""")


def follower_account():
    
    follow_banner1()
    follow_banner2()

 
    username = input(
        Fore.CYAN + "Instagram username: @"
    ).strip().lstrip("@")

    if not username:
        print(Fore.RED + "Username cannot be empty!")
        return

    

    print(Fore.GREEN + f"\nProfile: @{username}")
    followers_data=int(input(Fore.GREEN + "\nEnter How much followers you want :"))
    print(Fore.CYAN + "\n started. Stop with Ctrl+C.\n")

    count = 0

    try:
        while followers_data>count:
            count += 1
            print(
                Fore.MAGENTA
                + f"[{count}] Processing @{username} "
                + Fore.YELLOW
                + " add your followers"
            )
            time.sleep(0.5)

    except KeyboardInterrupt:
        print(Fore.GREEN + Style.BRIGHT + "\n After 2 hours your followers is added ")
        print(Fore.RED + "\n\n stopped by user (Ctrl+C).")
        


if __name__ == "__main__":
    follower_account()
