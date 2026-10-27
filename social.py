
import os
import re
from colorama import Fore, Style, init

init(autoreset=True)


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
    ██████╗ ██╗   ██╗██████╗ ██████╗  █████╗
    ██╔══██╗██║   ██║██╔══██╗██╔══██╗██╔══██╗
    ██████╔╝██║   ██║██║  ██║██████╔╝███████║
    ██╔══██╗██║   ██║██║  ██║██╔══██╗██╔══██║
    ██║  ██║╚██████╔╝██████╔╝██║  ██║██║  ██║
    ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
    """)
    print(Fore.MAGENTA + Style.BRIGHT +
          "          R U D R A P R A T A P")
    print(Fore.YELLOW + Style.BRIGHT +
          "          P R I V A T E  L O G I N")
    print(Fore.CYAN + "    " + "=" * 42)


def visible_length(text):
    return len(re.sub(r"\x1b\[[0-9;]*m", "", text))


def pause():
    input(Fore.YELLOW + "\n  Press Enter to continue...")


def social_media():
    while True:
        clear_screen()
        banner()

        print(Fore.GREEN + Style.BRIGHT + "\n  [1] Increase Followers")
        print(Fore.CYAN + Style.BRIGHT + "\n  [2] Increase Likes")
        print(Fore.YELLOW + Style.BRIGHT + "\n  [3] Mass Reports")
        print(Fore.BLUE + Style.BRIGHT + "\n  [4] Contact Admin")
        print(Fore.RED + Style.BRIGHT + "\n  [5] Exit")
        print(Fore.CYAN + Style.BRIGHT + "\n" + "=" * 58)

        choice = input(
            Fore.YELLOW + Style.BRIGHT + "\n  Select option (1-5): "
        ).strip()

        if choice == "1":
            social_platforms()

        elif choice == "2":
            print(Fore.GREEN + "\n  Use official platform analytics")
            print("  and authorized APIs for data access.")
            pause()

        elif choice == "3":
            print(Fore.CYAN + "\n  Report only genuine policy violations")
            print("  through each platform's official process.")
            pause()

        elif choice == "4":
            print(Fore.BLUE + "\n  Add your official admin contact details here.")
            pause()

        elif choice == "5":
            print(Fore.RED + "\n  Thank you for using RUDRAPRATAP!")
            break

        else:
            print(Fore.RED + "\n  Invalid choice!")
            pause()


def social_platforms():
    left = [
        (Fore.GREEN, "[1] Instagram"),
        (Fore.CYAN, "[2] Facebook"),
        (Fore.YELLOW, "[3] Twitter / X"),
        (Fore.BLUE, "[4] TikTok"),
        (Fore.MAGENTA, "[5] YouTube"),
        (Fore.RED, "[6] Snapchat"),
        (Fore.WHITE, "[7] Discord"),
        (Fore.LIGHTCYAN_EX, "[8] LinkedIn"),
    ]

    right = [
        (Fore.LIGHTBLUE_EX, "[9] Pinterest"),
        (Fore.LIGHTMAGENTA_EX, "[10] Reddit"),
        (Fore.LIGHTYELLOW_EX, "[11] Tumblr"),
        (Fore.LIGHTGREEN_EX, "[12] Quora"),
        (Fore.LIGHTRED_EX, "[13] VK"),
        (Fore.LIGHTWHITE_EX, "[14] Twitch"),
        (Fore.LIGHTBLACK_EX, "[15] Telegram"),
        (Fore.LIGHTCYAN_EX, "[16] Back"),
    ]

    # Module and function names are strings; nothing is imported yet.
    platforms = {
        "1": ("Instagram", "instagram", "instagram_menu"),
        "2": ("Facebook", "facebook", "facebook_menu"),
        "3": ("Twitter / X", "twitter", "twitter_menu"),
        "4": ("TikTok", "tiktok", "tiktok_menu"),
        "5": ("YouTube", "youtube", "youtube_menu"),
        "6": ("Snapchat", "snapchat", "snapchat_menu"),
        "7": ("Discord", "discord", "discord_menu"),
        "8": ("LinkedIn", "linkedin", "linkedin_menu"),
        "9": ("Pinterest", "pinterest", "pinterest_menu"),
        "10": ("Reddit", "reddit", "reddit_menu"),
        "11": ("Tumblr", "tumblr", "tumblr_menu"),
        "12": ("Quora", "quora", "quora_menu"),
        "13": ("VK", "vk", "vk_menu"),
        "14": ("Twitch", "twitch", "twitch_menu"),
        "15": ("Telegram", "telegram", "telegram_menu"),
    }

    while True:
        clear_screen()
        banner()

        for i in range(8):
            left_text = Style.BRIGHT + left[i][0] + left[i][1]
            right_text = Style.BRIGHT + right[i][0] + right[i][1]
            padding = " " * max(1, 29 - visible_length(left_text))

            print("  " + left_text + padding + "  " + right_text)

        print(Fore.CYAN + Style.BRIGHT + "=" * 62)

        choice = input(
            Fore.YELLOW + Style.BRIGHT + "\n  Select platform (1-16): "
        ).strip()

        if choice == "16":
            break

        selected = platforms.get(choice)

        if selected is None:
            print(Fore.RED + "\n  Invalid choice!")
            pause()
            continue

        name, module_name, function_name = selected

        try:
            # Import only the selected platform.
            module = __import__(
                f"platforms.{module_name}",
                fromlist=[function_name]
            )
            menu_function = getattr(module, function_name)
            menu_function()

        except (ImportError, AttributeError) as error:
            print(Fore.RED + f"\n  Could not open {name}: {error}")
            pause()


if __name__ == "__main__":
    social_media()
