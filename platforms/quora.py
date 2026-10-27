
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main


init(autoreset=True)


def quora_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Question Search")
        print(Fore.YELLOW + "[3] Public Answer Search")
        print(Fore.MAGENTA + "[4] Topic / Keyword Research")
        print(Fore.BLUE + "[5] Public Space Research")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter Quora profile name or keyword: "
            ).strip()

            if username:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:quora.com/profile " + username
                    )
                )
                print(Fore.GREEN + "\nOpening public profile search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a name.")

        elif choice == "2":
            question = input("Enter question or keyword: ").strip()

            if question:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:quora.com " + question
                    )
                )
                print(Fore.GREEN + "\nOpening public question search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a question.")

        elif choice == "3":
            keyword = input("Enter answer topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:quora.com " + keyword + " answer"
                    )
                )
                print(Fore.GREEN + "\nOpening public answer search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "4":
            keyword = input("Enter research keyword: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("site:quora.com " + keyword)
                )
                print(Fore.GREEN + "\nOpening topic research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            topic = input("Enter public Space topic: ").strip()

            if topic:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:quora.com " + topic + " space"
                    )
                )
                print(Fore.GREEN + "\nOpening public Space search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    quora_menu()
