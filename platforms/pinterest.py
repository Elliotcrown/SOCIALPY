
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main
import social

init(autoreset=True)


def pinterest_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()
        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Pins Search")
        print(Fore.YELLOW + "[3] Public Boards Search")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Image Topic Research")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter Pinterest username: "
            ).strip().lstrip("@")

            if username:
                url = "https://www.pinterest.com/" + quote_plus(username) + "/"
                print(Fore.GREEN + "\nOpening Pinterest profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            keyword = input("Enter pin search keyword: ").strip()

            if keyword:
                url = (
                    "https://www.pinterest.com/search/pins/?q="
                    + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening public Pins search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            keyword = input("Enter board topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:pinterest.com " + keyword + " boards"
                    )
                )
                print(Fore.GREEN + "\nOpening board search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a board topic.")

        elif choice == "4":
            keyword = input("Enter research keyword: ").strip()

            if keyword:
                url = (
                    "https://www.pinterest.com/search/"
                    "?q=" + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening keyword research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            topic = input("Enter image topic: ").strip()

            if topic:
                url = (
                    "https://www.google.com/search?tbm=isch&q="
                    + quote_plus(
                        "site:pinterest.com " + topic
                    )
                )
                print(Fore.GREEN + "\nOpening image topic search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter an image topic.")

        elif choice == "6":
            print(Fore.CYAN + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    pinterest_menu()
