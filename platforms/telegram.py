
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main


init(autoreset=True)


def telegram_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Channel Research")
        print(Fore.CYAN + "[2] Public Group Search")
        print(Fore.YELLOW + "[3] Public Username Research")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Telegram API Documentation")
        print(Fore.RED + "[6] Telegram Safety Resources")
        print(Fore.WHITE + "[7] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            channel = input(
                "Enter public channel name or keyword: "
            ).strip().lstrip("@")

            if channel:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:t.me/" + channel
                    )
                )
                print(Fore.GREEN + "\nOpening public channel search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a channel name.")

        elif choice == "2":
            keyword = input("Enter public group topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("Telegram public group " + keyword)
                )
                print(Fore.GREEN + "\nOpening public group search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "3":
            username = input(
                "Enter public Telegram username: "
            ).strip().lstrip("@")

            if username:
                url = "https://t.me/" + quote_plus(username)
                print(Fore.GREEN + "\nOpening Telegram public username...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "4":
            keyword = input("Enter research keyword: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("site:t.me " + keyword)
                )
                print(Fore.GREEN + "\nOpening keyword research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            print(Fore.CYAN + "\nOpening Telegram API documentation...")
            webbrowser.open("https://core.telegram.org/")
            print("Official documentation opened.")

        elif choice == "6":
            print(Fore.YELLOW + "\nOpening Telegram FAQ...")
            webbrowser.open("https://telegram.org/faq")
            print("Official Telegram FAQ opened.")

        elif choice == "7":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 7.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    telegram_menu()
