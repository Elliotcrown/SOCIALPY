
from colorama import Fore, Style, init
import os
import time
import webbrowser
import main
from urllib.parse import quote_plus

init(autoreset=True)


def snapchat_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        main.banner()
        
        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Spotlight Search")
        print(Fore.YELLOW + "[3] Public Story Information")
        print(Fore.MAGENTA + "[4] Public Topic Research")
        print(Fore.BLUE + "[5] Snapchat Safety Resources")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter public Snapchat username: "
            ).strip().lstrip("@")

            if username:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "site:snapchat.com/add/ " + username
                    )
                )
                print(Fore.GREEN + "\nOpening public profile search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username.")

        elif choice == "2":
            keyword = input("Enter Spotlight topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus(
                        "Snapchat Spotlight " + keyword
                    )
                )
                print(Fore.GREEN + "\nOpening Spotlight search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "3":
            print(Fore.YELLOW + "\nPublic Story Information")
            print("Only stories made publicly available by their")
            print("creators can be researched.")
            print("Private or friends-only stories are not accessed.")

        elif choice == "4":
            keyword = input("Enter public research topic: ").strip()

            if keyword:
                url = (
                    "https://www.google.com/search?q="
                    + quote_plus("Snapchat " + keyword)
                )
                print(Fore.GREEN + "\nOpening topic search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "5":
            print(Fore.CYAN + "\nOpening Snapchat Safety Resources...")
            webbrowser.open("https://values.snap.com/safety/safety-center")
            print("Official safety resources opened.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    snapchat_menu()
