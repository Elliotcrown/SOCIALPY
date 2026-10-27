
from colorama import Fore, Style, init
import os
import time
import main

init(autoreset=True)


def linkedin_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + Style.BRIGHT + "[1] Public Profile Research")
        print(Fore.CYAN + Style.BRIGHT + "[2] Increase Connection")
        print(Fore.YELLOW + Style.BRIGHT + "[3] Increase Likes")
        print(Fore.MAGENTA + Style.BRIGHT + "[4] Mass Reports")
        print(Fore.RED + Style.BRIGHT + "[5] Back")
    

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            print(Fore.GREEN + "\nPublic Profile Research selected.")
            profile_url = input("Enter public LinkedIn profile URL: ").strip()

            if profile_url:
                print(Fore.CYAN + "\nProfile URL:", profile_url)
                print("Next step: connect an authorized public-data source.")
            else:
                print(Fore.RED + "Profile URL cannot be empty.")

        elif choice == "2":
            print(Fore.CYAN + "\nCompany Research selected.")
            company = input("Enter company name: ").strip()

            if company:
                print(Fore.GREEN + "\nCompany:", company)
                print("Next step: research publicly available company information.")
            else:
                print(Fore.RED + "Company name cannot be empty.")

        elif choice == "3":
            print(Fore.YELLOW + "\nJob Information selected.")
            job_title = input("Enter job title or keyword: ").strip()

            if job_title:
                print(Fore.CYAN + "\nSearch keyword:", job_title)
                print("Next step: connect an authorized job-data source.")
            else:
                print(Fore.RED + "Job title cannot be empty.")

        elif choice == "4":
            print(Fore.MAGENTA + "\nPublic Post Research selected.")
            post_url = input("Enter public post URL: ").strip()

            if post_url:
                print(Fore.GREEN + "\nPost URL:", post_url)
                print("Next step: analyze permitted public post information.")
            else:
                print(Fore.RED + "Post URL cannot be empty.")

        elif choice == "5":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    linkedin_menu()
