
from pathlib import Path
import getpass
import os
import sys
import time

from colorama import init, Fore, Style
from dotenv import set_key
from pymongo import MongoClient

init(autoreset=True)




def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
  ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗     ██████╗ ██╗   ██╗
  ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝
  ███████╗██║   ██║██║     ██║███████║██║     ██████╔╝ ╚████╔╝
  ╚════██║██║   ██║██║     ██║██╔══██║██║     ██╔═══╝   ╚██╔╝
  ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗██║        ██║
  ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝        ╚═╝
    """)
    print(Fore.GREEN + Style.BRIGHT + "          SOCIALPY | DATABASE SETUP")
    print(Fore.YELLOW + "-" * 58)


def main():
    banner()

    

    answer = input(
        Fore.CYAN + "Do you want to setup? [yes/no]: "
    ).strip().lower()

    if answer  in ("yes", "y"):
         url="mongodb://campusmanagement144_db_user:JmKFWQSKacNioZQf@ac-rtf7dnr-shard-00-00.0rvhswr.mongodb.net:27017,ac-rtf7dnr-shard-00-01.0rvhswr.mongodb.net:27017,ac-rtf7dnr-shard-00-02.0rvhswr.mongodb.net:27017/?ssl=true&replicaSet=atlas-ubeno4-shard-0&authSource=admin&compressors=zlib"
         print(f'URL={url}')
    else:
     print(Fore.BLUE+Style.BRIGHT+"\n Setup cancelled")
   
    
    


if __name__ == "__main__":
    main()
