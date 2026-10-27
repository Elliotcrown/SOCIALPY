
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main

init(autoreset=True)


def tumblr_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()

        print(Fore.GREEN + "[1] Public Blog Research")
        print(Fore.CYAN + "[2] Public Post Search")
        print(Fore.YELLOW + "[3] Tag Research")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Tumblr Safety Resources")
        print(Fore.WHITE + "[6] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            blog = input(
                "Enter public Tumblr blog name or URL: "
            ).strip()

            if blog:
                if blog.startswith(("https://", "http://")):
                    url = blog
                else:
                    blog = blog.removesuffix(".tumblr.com").strip("/")
                    url = "https://" + quote_plus(blog) + ".tumblr.com/"

                print(Fore.GREEN + "\nOpening public Tumblr blog...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a blog name or URL.")

        elif choice == "2":
            keyword = input("Enter post search keyword: ").strip()

            if keyword:
                query = quote_plus(keyword)
                url = f"https://www.tumblr.com/search/{query}"
                print(Fore.GREEN + "\nOpening Tumblr post search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            tag = input(
                "Enter tag (with or without #): "
            ).strip().lstrip("#")

            if tag:
                url = "https://www.tumblr.com/tagged/" + quote_plus(tag)
                print(Fore.GREEN + "\nOpening Tumblr tag research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a tag.")

        elif choice == "4":
            keyword = input("Enter OSINT research keyword: ").strip()

            if keyword:
                query = quote_plus("site:tumblr.com " + keyword)
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public keyword results...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            print(Fore.YELLOW + "\nOpening Tumblr Help Center...")
            webbrowser.open("https://help.tumblr.com/")
            print(Fore.CYAN + "Tumblr help resources opened.")

        elif choice == "6":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 6.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    tumblr_menu()
