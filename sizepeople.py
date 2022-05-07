def sizePeople():
    customerNum = 0

    while True:
        customerNum = int(input("How many people will stay in the room:"))
        if (customerNum <= 5):
            insertCustomerData(customerNum)
            break
        else:
            print("Maximum Capacity per room is 5, please try again") 