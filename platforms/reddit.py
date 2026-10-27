
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main

init(autoreset=True)


def reddit_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public User Research")
        print(Fore.CYAN + "[2] Subreddit Research")
        print(Fore.YELLOW + "[3] Public Post Search")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Reddit Safety Resources")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input("Enter Reddit username: ").strip().lstrip("u/")

            if username:
                url = (
                    "https://www.reddit.com/user/"
                    + quote_plus(username)
                    + "/"
                )
                print(Fore.GREEN + "\nOpening Reddit profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            subreddit = input(
                "Enter subreddit name (without r/): "
            ).strip().lstrip("r/")

            if subreddit:
                url = (
                    "https://www.reddit.com/r/"
                    + quote_plus(subreddit)
                    + "/"
                )
                print(Fore.GREEN + "\nOpening subreddit...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a subreddit name.")

        elif choice == "3":
            keyword = input("Enter post search keyword: ").strip()

            if keyword:
                url = (
                    "https://www.reddit.com/search/?q="
                    + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening Reddit post search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "4":
            keyword = input("Enter research keyword: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("site:reddit.com " + keyword)
                )
                print(Fore.GREEN + "\nOpening public keyword research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            print(Fore.CYAN + "\nOpening Reddit Help...")
            webbrowser.open("https://support.reddithelp.com/")
            print("Reddit Help opened in browser.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    reddit_menu()
