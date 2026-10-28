
import os
import time
import getpass

from colorama import Fore, Style, init


init(autoreset=True)

# Demo credentials — real projects should use secure authentication
USERNAME = "rudrapratap"
PASSWORD = "Rudra@123"


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def banner():

 print(Fore.MAGENTA + Style.BRIGHT + r"""
   ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     
   ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     
   ███████╗██║   ██║██║     ██║███████║██║     
   ╚════██║██║   ██║██║     ██║██╔══██║██║     
   ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗
   ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝

          >>> DEVELOPED BY ELLIOT <<<
""")
print(Fore.CYAN + Style.BRIGHT + "=" * 52)


    


def login():
    attempts = 3

    while attempts > 0:
        clear_screen()
        banner()

        username = input(
            Fore.GREEN + Style.BRIGHT + "\n  Username: "
        ).strip()

        password = getpass.getpass(
            Fore.GREEN + Style.BRIGHT + "  Password: "
        )

        if username == USERNAME and password == PASSWORD:
            print(Fore.GREEN + Style.BRIGHT +
                  "\n  Login successful!")
            time.sleep(1)
            import social
            social.social_media()
            return

        attempts -= 1
        print(Fore.RED + Style.BRIGHT +
              f"\n  Invalid credentials! Attempts left: {attempts}")

        if attempts > 0:
            time.sleep(1)

    print(Fore.RED + Style.BRIGHT +
          "\n  Access denied. Exiting...")
    time.sleep(2)


def main():
    try:
        login()
    except KeyboardInterrupt:
        print(Fore.YELLOW + "\n\n  Program interrupted. Goodbye!")


if __name__ == "__main__":
    main()
