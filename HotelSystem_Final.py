import re
import os

class Room:
    def __init__(self):
        self.array_age = []
        self.array_contact = []
        self.array_customerName = []

    def addAge(self, age):
        self.array_age.append(age)

    def addContact(self, contact):
        self.array_contact.append(contact)

    def addCustomerName(self, customerName):
        self.array_customerName.append(customerName)

    def getAge(self): return self.array_age
    def getContact(self): return self.array_contact
    def getCustomerName(self): return self.array_customerName

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
            
def sizePeople():
    customerNum = 0

    while True:
        customerNum = int(input("How many people will stay in the room:"))
        if (customerNum <= 5):
            insertCustomerData(customerNum)
            break
        else:
            print("Maximum Capacity per room is 5, please try again") 

def insertCustomerData(customerNum):
    global intRoomNumber

    newRoom = Room()

    for i in range(customerNum):
        print(f"For Customer {i+1}")
        name = input("Please enter your name:")
        contact_number = input("Please enter your contact number:")
        age = input("Please enter your age:")

        newRoom.addAge(age)
        newRoom.addContact(contact_number)
        newRoom.addCustomerName(name)

    roomNumber = FloorRoomNumber()

    intRoomNumber[roomNumber] = newRoom

    name_arr = newRoom.getCustomerName()
    contact_arr = newRoom.getContact()
    age_arr = newRoom.getAge()

    for i in range(customerNum):
        print(f"Name: {name_arr[i]}")
        print(f"Contact Number: {contact_arr[i]}")
        print(f"Age {age_arr[i]}")
    

def FloorRoomNumber():
    global intRoomNumber
    floorNum = 0
    roomNum = 0
    totalRoom = 100
    totalfloors = 5
    roomperfloor = totalRoom / totalfloors

    while True:
        print("First Floor: Room 1 - Room 20 [Enter 1]")
        print("Second Floor: Room 21 - Room 40 [Enter 2]")
        print("Third Floor: Room 41 - Room 60 [Enter 3]")
        print("Fourth Floor: Room 61 - Room 80 [Enter 4]")
        print("Fifth Floor: Room 81 - Room 100 [Enter 5]")
        choice = int(input("Choose a Floor to stay:"))
        if choice <= 5:
            floorNum = choice
            break 
        else:
            print("Please select a valid floor")

    while True:
        choice = int(input("Choose a Room to stay:"))
        if ((choice // roomperfloor) + (1 * (choice % roomperfloor != 0))) == floorNum:
            if (intRoomNumber[choice - 1] == 0):
                roomNum = choice
                break
            else:
                #print(intRoomNumber[choice - 1].getCustomerName())
                print("Room is occupied, pick another room")
             
        else:
            print("Invalid Room Number, Please Try Again")

    return roomNum - 1
    


def loginSystem():
    while True:
        email = input("Enter your email:")
        if (email_validation(email)):
            print("Your Email Address is valid")
            break
        else:
            print("Your email address is invalid please try again!")

    while True:
        password = input("Enter your password:")
        if (len(password) >= 8 and len(password) <= 16):
            print("Your Password is valid")
            break
        else:
            print("Your Password is invalid! Please try again!")


def email_validation(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.fullmatch(pattern, email)


def test():
    email = input("Enter email:")


main()