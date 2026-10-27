
import os
from colorama import Fore, Style, init

from platforms.instagram import instagram_menu
from platforms.facebook import facebook_menu

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def social_media():
    platforms = {
        "1": ("Instagram", instagram_menu),
        "2": ("Facebook", facebook_menu),
    }

    while True:
        clear_screen()

        print(Fore.MAGENTA + Style.BRIGHT +
              "\n===== RUDRAPRATAP SOCIAL MENU =====")

        for number, (name, _) in platforms.items():
            print(Fore.GREEN + f"[{number}] {name}")

        print(Fore.RED + "[0] Exit")

        choice = input(
            Fore.CYAN + "\nSelect platform: "
        ).strip()

        if choice == "0":
            break

        selected = platforms.get(choice)

        if selected:
            selected[1]()
        else:
            print(Fore.RED + "Invalid choice!")
            input("Press Enter to continue...")


if __name__ == "__main__":
    social_media()
