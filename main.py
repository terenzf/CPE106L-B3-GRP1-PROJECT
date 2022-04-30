import re
import os

def intro():
    print("Do you wish to enter SAGA")
    print("Enter [1|0]")
    print("Enter '1' to add or book a room")
    print("Enter '0' to exit")

def continueasking():
    print("Do you wish to book another room")
    print("Enter [1|0]")
    print("Enter '1' to add or book another room")
    print("Enter '0' to exit")

def main():
    global intRoomNumber
    intRoomNumber = [0 for _ in range(100)] # Main Array
    choice = -1
    logged_in = False
    option = ""
    email = ""

    intro()   
    while True:        
        choice = int(input("Enter your choice:"))
        if choice == 0:
            print("* Thank you for visiting SAGA! *")
            print("* Please come again soon! ******")
            break 
        elif choice == 1:
            if not logged_in:
                print("Do you wish to login")        
                print("Enter [1|0]")
                print("Enter '1' to Login")
                print("Enter '0' to exit")
                l_choice = int(input("Enter your choice:"))
                if l_choice == 1:
                    loginSystem()
                    logged_in = True 
                    os.system("CLS")
                    sizePeople()
                    continueasking()
                else:
                    print("* Thank you for visiting SAGA! *")
                    print("* Please come again soon! ******")
                    break 
            else:
                os.system("CLS")
                sizePeople()
                continueasking()

            
            
        else:
            print("PLEASE TRY AGAIN")

main()