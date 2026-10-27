
import time
import requests
from urllib.parse import urlparse
from colorama import Fore, Style, init

init(autoreset=True)



def like_banner():
     print(Fore.MAGENTA + Style.BRIGHT + r"""
    ██╗     ██╗██╗  ██╗███████╗
    ██║     ██║██║ ██╔╝██╔════╝
    ██║     ██║█████╔╝ █████╗
    ██║     ██║██╔═██╗ ██╔══╝
    ███████╗██║██║  ██╗███████╗
    ╚══════╝╚═╝╚═╝  ╚═╝╚══════╝
  """)
def like_banner2():
 print(Fore.CYAN + Style.BRIGHT + r"""
       ⚡ SOCIAL ENGAGEMENT ⚡
       ━━━━━━━━━━━━━━━━━━━━━━
             ELLIOT
   """)

def verify_post_url(url):
    parsed = urlparse(url.strip())

    valid_host = parsed.hostname in (
        "instagram.com",
        "www.instagram.com",
    )
    valid_path = parsed.path.startswith(
        ("/p/", "/reel/", "/tv/")
    )

    return (
        parsed.scheme == "https"
        and valid_host
        and valid_path
    )


def insta_like():
    like_banner()
    like_banner2()

    post_url = input(
        Fore.CYAN + "Instagram post URL: "
    ).strip()

    like_count=int(input(Fore.CYAN + "\n Enter amount of like you want:"))

    if not verify_post_url(post_url):
        print(Fore.RED + "Invalid Instagram post URL!")
        return

    print(Fore.YELLOW + "\nChecking post URL...")

    try:
        response = requests.get(
            post_url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10,
            allow_redirects=True,
        )

        if response.status_code in (404, 410):
            print(Fore.RED + "Post may be unavailable or deleted.")
            return

        if response.status_code != 200:
            print(Fore.YELLOW +
                  "Post existence could not be confirmed.")
            return

    except requests.RequestException:
        print(Fore.YELLOW +
              "Instagram verification failed; access may be restricted.")
        return

    print(Fore.GREEN + "URL opened; existence is not guaranteed.")
    print(Fore.CYAN + "\nLike-processing  started.")
    print(Fore.RED + "Stop with Ctrl+C.\n")

    count = 0

    try:
        while like_count>count:
            count += 1
            print(
                Fore.MAGENTA
                + f"[{count}] "
                + Fore.YELLOW
                + "Simulating like processing..."
                
            )
            time.sleep(0.5)

    except KeyboardInterrupt:
        print(Fore.RED + "\n stopped by user.")


if __name__ == "__main__":
    insta_like()
