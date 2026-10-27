
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main

init(autoreset=True)


def twitter_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Post Search")
        print(Fore.YELLOW + "[3] Hashtag Research")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Public Topic Search")
        print(Fore.RED + "[6] X Safety Resources")
        print(Fore.WHITE + "[7] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter public X username: "
            ).strip().lstrip("@")

            if username:
                url = "https://x.com/" + quote_plus(username)
                print(Fore.GREEN + "\nOpening public profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            keyword = input(
                "Enter post search keyword: "
            ).strip()

            if keyword:
                url = (
                    "https://x.com/search?q="
                    + quote_plus(keyword)
                    + "&src=typed_query"
                )
                print(Fore.GREEN + "\nOpening X post search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            hashtag = input(
                "Enter hashtag (with or without #): "
            ).strip().lstrip("#")

            if hashtag:
                query = quote_plus("#" + hashtag)
                url = "https://x.com/search?q=" + query
                print(Fore.GREEN + "\nOpening hashtag research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a hashtag.")

        elif choice == "4":
            keyword = input(
                "Enter OSINT research keyword: "
            ).strip()

            if keyword:
                query = quote_plus("site:x.com " + keyword)
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public keyword results...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            topic = input(
                "Enter a topic, event, or public organization: "
            ).strip()

            if topic:
                query = quote_plus(topic)
                url = "https://x.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public topic search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "6":
            print(Fore.YELLOW + "\nOpening X Help Center...")
            webbrowser.open("https://help.x.com/")
            print(Fore.CYAN + "Safety and help resources opened.")

        elif choice == "7":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 7.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    twitter_menu()
