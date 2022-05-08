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