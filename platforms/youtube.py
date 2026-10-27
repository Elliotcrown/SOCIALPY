
from colorama import Fore, Style, init
import os
import time
import webbrowser
from urllib.parse import quote_plus
import main
import social

init(autoreset=True)


def youtube_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")

        main.banner()
        print(Fore.GREEN + "[1] Public Channel Research")
        print(Fore.CYAN + "[2] Video Search")
        print(Fore.YELLOW + "[3] YouTube Shorts Search")
        print(Fore.MAGENTA + "[4] Keyword Research")
        print(Fore.BLUE + "[5] Public Topic Research")
        print(Fore.RED + "[6] YouTube Safety Resources")
        print(Fore.WHITE + "[7] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()

        if choice == "1":
            channel = input(
                "Enter public channel name or @handle: "
            ).strip()

            if channel:
                if channel.startswith(("https://", "http://")):
                    url = channel
                elif channel.startswith("@"):
                    url = "https://www.youtube.com/" + quote_plus(channel)
                else:
                    url = (
                        "https://www.youtube.com/results?search_query="
                        + quote_plus(channel)
                    )

                print(Fore.GREEN + "\nOpening public channel search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a channel name or handle.")

        elif choice == "2":
            keyword = input("Enter video search keyword: ").strip()

            if keyword:
                url = (
                    "https://www.youtube.com/results?search_query="
                    + quote_plus(keyword)
                )
                print(Fore.GREEN + "\nOpening YouTube video search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "3":
            keyword = input("Enter Shorts topic or keyword: ").strip()

            if keyword:
                query = quote_plus(keyword + " shorts")
                url = (
                    "https://www.youtube.com/results?search_query="
                    + query
                )
                print(Fore.GREEN + "\nOpening Shorts search...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "4":
            keyword = input("Enter OSINT research keyword: ").strip()

            if keyword:
                query = quote_plus("site:youtube.com " + keyword)
                url = "https://www.google.com/search?q=" + query
                print(Fore.GREEN + "\nOpening public keyword results...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a keyword.")

        elif choice == "5":
            topic = input(
                "Enter a public topic, event, or organization: "
            ).strip()

            if topic:
                url = (
                    "https://www.youtube.com/results?search_query="
                    + quote_plus(topic)
                )
                print(Fore.GREEN + "\nOpening topic research...")
                webbrowser.open(url)
            else:
                print(Fore.RED + "Please enter a topic.")

        elif choice == "6":
            print(Fore.YELLOW + "\nOpening YouTube Help...")
            webbrowser.open("https://support.google.com/youtube/")
            print(Fore.CYAN + "YouTube help resources opened.")

        elif choice == "7":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 7.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    youtube_menu()
