from colorama import Fore, Style
import time

def Mass_report(username, reason):
    username = username.strip().lstrip("@")

    if not username:
        print(Fore.RED + "Username cannot be empty.")
        return

    print(Fore.MAGENTA + f"\nProfile: @{username}")
    time.sleep(0.5)

    print(Fore.YELLOW + f"Reason selected: {reason}")
    time.sleep(0.5)

    print(Fore.CYAN + "\nReporting information")
    print(Fore.WHITE + "Sirf genuine policy violations report karein.")
    print(Fore.GREEN + "Instagram Help Center:")
    print("https://help.instagram.com/")

    input(Fore.YELLOW + "\nPress Enter to continue...")

    