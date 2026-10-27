
from colorama import Fore, Style, init
import os
import time
import webbrowser
import main
from urllib.parse import quote_plus

init(autoreset=True)


def tiktok_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()
        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Video Search")
        print(Fore.YELLOW + "[3] Hashtag Research")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] TikTok Safety Resources")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter public TikTok username: "
            ).strip().lstrip("@")

            if username:
                url = "https://www.tiktok.com/@" + quote_plus(username)
                print(Fore.GREEN + "\nOpening TikTok profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            keyword = input("Enter video search keyword: ").strip()

            if keyword:
                url = (
                    "https://www.tiktok.com/search?q="
                    + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening TikTok video search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            hashtag = input(
                "Enter hashtag (with or without #): "
            ).strip().lstrip("#")

            if hashtag:
                url = (
                    "https://www.tiktok.com/tag/"
                    + quote_plus(hashtag)
                )
                print(Fore.GREEN + "\nOpening hashtag research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a hashtag.")

        elif choice == "4":
            keyword = input("Enter research keyword: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("site:tiktok.com " + keyword)
                )
                print(Fore.GREEN + "\nOpening public keyword search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            print(Fore.YELLOW + "\nOpening TikTok Safety Center...")
            webbrowser.open("https://www.tiktok.com/safety")
            print("Official safety resources opened.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    tiktok_menu()
