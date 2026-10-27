
from colorama import Fore, Style, init
import os
import time
import main

init(autoreset=True)


def facebook_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        main.banner()
        

        print(Fore.GREEN + Style.BRIGHT + "[1] Public Profile Research")
        print(Fore.CYAN + Style.BRIGHT + "[2] Increase Likes")
        print(Fore.YELLOW + Style.BRIGHT + "[3] Increase Followers")
        print(Fore.RED + Style.BRIGHT + "[4] Mass Reporting")
        print(Fore.MAGENTA + Style.BRIGHT + "[5] Back")
        

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            print(Fore.GREEN + "\nPublic Profile Research selected.")
            profile = input("Enter public profile URL: ").strip()

            if profile:
                print(Fore.CYAN + "\nProfile URL:", profile)
                print("Next step: connect an authorized public-data source.")
            else:
                print(Fore.RED + "Profile URL cannot be empty.")

        elif choice == "2":
            print(Fore.CYAN + "\nPublic Page Research selected.")
            page = input("Enter public Facebook Page URL: ").strip()

            if page:
                print(Fore.GREEN + "\nPage URL:", page)
                print("Next step: retrieve permitted public Page information.")
            else:
                print(Fore.RED + "Page URL cannot be empty.")

        elif choice == "3":
            print(Fore.YELLOW + "\nPublic Post Research selected.")
            post = input("Enter public post URL: ").strip()

            if post:
                print(Fore.CYAN + "\nPost URL:", post)
                print("Next step: analyze available public post information.")
            else:
                print(Fore.RED + "Post URL cannot be empty.")

        elif choice == "4":
            print(Fore.RED + "\nFacebook Safety / Reporting")
            print("Use Facebook's official reporting tools")
            print("for genuine policy violations.")

        elif choice == "5":
              print(Fore.BLUE + "\nReturning to previous menu...")
              time.sleep(1)
              break
        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    facebook_menu()
