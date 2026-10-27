
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main


init(autoreset=True)


def discord_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Server Research")
        print(Fore.CYAN + "[2] Public Community Search")
        print(Fore.YELLOW + "[3] Discord Bot Documentation")
        print(Fore.MAGENTA + "[4] Public Topic Research")
        print(Fore.RED + "[5] Trust & Safety Resources")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            keyword = input("Enter server or community topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "Discord public server " + keyword
                    )
                )
                print(Fore.GREEN + "\nOpening public server search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "2":
            keyword = input("Enter community keyword: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:discord.com/servers " + keyword
                    )
                )
                print(Fore.GREEN + "\nOpening community search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            print(Fore.CYAN + "\nDiscord Developer Documentation")
            webbrowser.open("https://discord.com/developers/docs")
            print("Official documentation opened in browser.")

        elif choice == "4":
            keyword = input("Enter public research topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("Discord " + keyword)
                )
                print(Fore.GREEN + "\nOpening topic search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "5":
            print(Fore.MAGENTA + "\nDiscord Safety Resources")
            webbrowser.open("https://discord.com/safety")
            print("Official Discord Safety page opened.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    discord_menu()
