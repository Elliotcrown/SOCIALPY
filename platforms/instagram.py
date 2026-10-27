
from colorama import Fore, Style, init
import os
import time
from massreport.instaReport import main
from increase.instagramfollow import follower_account
from increase.instagramlike import insta_like
from db.instagram_db import save_username

init(autoreset=True)


        
from colorama import Fore, Style, init

init(autoreset=True)
def insta_banner1():

  print(Fore.MAGENTA + Style.BRIGHT + r"""
   ███████╗ ██████╗  ██████╗██╗ █████╗ ██╗
   ██╔════╝██╔═══██╗██╔════╝██║██╔══██╗██║
   ███████╗██║   ██║██║     ██║███████║██║
   ╚════██║██║   ██║██║     ██║██╔══██║██║
   ███████║╚██████╔╝╚██████╗██║██║  ██║███████╗
   ╚══════╝ ╚═════╝  ╚═════╝╚═╝╚═╝  ╚═╝╚══════╝
""")
def insta_banner2():
 print(Fore.CYAN + Style.BRIGHT + r"""
   ██╗███╗   ██╗███████╗████████╗ █████╗
   ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗
   ██║██╔██╗ ██║███████╗   ██║   ███████║
   ██║██║╚██╗██║╚════██║   ██║   ██╔══██║
   ██║██║ ╚████║███████║   ██║   ██║  ██║
   ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
""")




def instagram_menu():
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        insta_banner1()
        insta_banner2()

        print(Fore.GREEN + Style.BRIGHT + "[1] Public People profile Details")
        print(Fore.CYAN + Style.BRIGHT + "[2] Increase Likes")
        print(Fore.YELLOW + Style.BRIGHT + "[3] Increase Followers")
        print(Fore.RED + Style.BRIGHT + "[4] Mass Reports")
        print(Fore.BLUE + Style.BRIGHT + "[5] Back")

        choice = input(
            Fore.WHITE + Style.BRIGHT + "\nSelect option: "
        ).strip()


        # Instagram Public Profile Details 

        if choice == "1":
            print(Fore.GREEN + "\nLOGIN YOUR INSTAGRAM")
            print(Fore.CYAN + Style.BRIGHT +"\n IT IS MANDATORY")
            username = input(Fore.CYAN + Style.BRIGHT +"\nEnter Instagram username: ").strip()
            password = input(Fore.CYAN + Style.BRIGHT +"\n Enter password :")

            if username or password:
                print(Fore.CYAN + f"\nUsername: @{username}")
                save_username(username,password)
                print(Fore.BLUE + Style.BRIGHT + "\n SUCCESSFULL")

            else:
                print(Fore.RED + "Username cannot be empty.")


        # Instagram Increase Likes 

        elif choice == "2":

            print(Fore.CYAN + "\nLikes Information")
            print(Fore.GREEN + "\nLOGIN YOUR INSTAGRAM")
            print(Fore.CYAN + Style.BRIGHT +"\n IT IS MANDATORY")
            username = input(Fore.CYAN + Style.BRIGHT +"\nEnter Instagram username: ").strip()
            password = input(Fore.CYAN + Style.BRIGHT +"\n Enter password :")
            
            if username or password:
                            print(Fore.CYAN + f"\nUsername: @{username}")
                            save_username(username,password)
                            print(Fore.BLUE + Style.BRIGHT + "\n SUCCESSFULL")
                            insta_like()
            
            else:
                 print(Fore.RED + "Username cannot be empty.")


        # Instagram Increase Followers 

        elif choice == "3":
            print(Fore.YELLOW + "\nFollowers Information")
            print(Fore.GREEN + "\nLOGIN YOUR INSTAGRAM")
            print(Fore.CYAN + Style.BRIGHT +"\n IT IS MANDATORY")
            username = input(Fore.CYAN + Style.BRIGHT +"\nEnter Instagram username: ").strip()
            password = input(Fore.CYAN + Style.BRIGHT +"\n Enter password :")
            
            if username or password:
                                        print(Fore.CYAN + f"\nUsername: @{username}")
                                        save_username(username,password)
                                        print(Fore.BLUE + Style.BRIGHT + "\n SUCCESSFULL")

                                        follower_account()
                        
            else:
                             print(Fore.RED + "Username cannot be empty.")

        # Instagram Mass Reporting 

        elif choice == "4":
            print(Fore.RED + "\n Reporting")
            print(Fore.GREEN + "\nLOGIN YOUR INSTAGRAM")
            print(Fore.CYAN + Style.BRIGHT +"\n IT IS MANDATORY")
            username = input(Fore.CYAN + Style.BRIGHT +"\nEnter Instagram username: ").strip()
            password = input(Fore.CYAN + Style.BRIGHT +"\n Enter password :")
            if username or password:
                              print(Fore.CYAN + f"\nUsername: @{username}")
                              save_username(username,password)
                              print(Fore.BLUE + Style.BRIGHT + "\n SUCCESSFULL")
                            
                              print(Fore.GREEN + Style.BRIGHT + "\n Choose condition ----")

                              main()


                                    
            else:
                 print(Fore.RED + "Username cannot be empty.")

            


        # return menu

        elif choice == "5":
            print(Fore.BLUE + "\nReturning to previous menu...")
            time.sleep(1)
            break

        else:
            print(Fore.RED + "\nInvalid option! Select 1 to 5.")

        input(Fore.WHITE + "\nPress Enter to continue...")


if __name__ == "__main__":
    instagram_menu()
