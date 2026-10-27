
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main

init(autoreset=True)


def twitch_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Streamer Profile")
        print(Fore.CYAN + "[2] Live Stream Search")
        print(Fore.YELLOW + "[3] Game / Category Research")
        print(Fore.MAGENTA + "[4] Public Clips Search")
        print(Fore.BLUE + "[5] Keyword Research")
        print(Fore.RED + "[6] Twitch Safety Resources")
        print(Fore.WHITE + "[7] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter public Twitch username: "
            ).strip().lstrip("@")

            if username:
                url = "https://www.twitch.tv/" + quote_plus(username)
                print(Fore.GREEN + "\nOpening streamer profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            keyword = input(
                "Enter streamer name or live-stream topic: "
            ).strip()

            if keyword:
                url = (
                    "https://www.twitch.tv/search?term="
                    + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening Twitch search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a search term.")

        elif choice == "3":
            game = input(
                "Enter game or category name: "
            ).strip()

            if game:
                url = (
                    "https://www.twitch.tv/directory"
                    "?term=" + quote_plus(game)
                )
                print(Fore.GREEN + "\nOpening game/category research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a game or category.")

        elif choice == "4":
            keyword = input(
                "Enter clip topic or streamer name: "
            ).strip()

            if keyword:
                query = quote_plus("site:twitch.tv " + keyword + " clips")
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public clips search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a search term.")

        elif choice == "5":
            keyword = input(
                "Enter OSINT research keyword: "
            ).strip()

            if keyword:
                query = quote_plus("site:twitch.tv " + keyword)
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public keyword results...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "6":
            print(Fore.YELLOW + "\nOpening Twitch Safety Center...")
            webbrowser.open("https://safety.twitch.tv/")
            print(Fore.CYAN + "Safety resources opened.")

        elif choice == "7":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 7.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    twitch_menu()
