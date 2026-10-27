
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main

init(autoreset=True)


def vk_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Profile Research")
        print(Fore.CYAN + "[2] Public Post Search")
        print(Fore.YELLOW + "[3] Public Community Research")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] VK Official Resources")
        print(Fore.RED + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            username = input(
                "Enter public VK username or profile ID: "
            ).strip().lstrip("@")

            if username:
                url = "https://vk.com/" + quote_plus(username)
                print(Fore.GREEN + "\nOpening public VK profile...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a username or profile ID.")

        elif choice == "2":
            keyword = input("Enter public post search keyword: ").strip()

            if keyword:
                query = quote_plus(keyword)
                url = f"https://www.google.com/search?q={quote_plus('site:vk.com ' + keyword)}"
                print(Fore.GREEN + "\nOpening public post search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            community = input(
                "Enter public VK community name or ID: "
            ).strip().lstrip("@")

            if community:
                url = "https://vk.com/" + quote_plus(community)
                print(Fore.GREEN + "\nOpening VK community...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a community name or ID.")

        elif choice == "4":
            keyword = input("Enter OSINT research keyword: ").strip()

            if keyword:
                query = quote_plus("site:vk.com " + keyword)
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public keyword results...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            print(Fore.YELLOW + "\nOpening VK website...")
            webbrowser.open("https://vk.com/")
            print(Fore.CYAN + "VK official website opened.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    vk_menu()
