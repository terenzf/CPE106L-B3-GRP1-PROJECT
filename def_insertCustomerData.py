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