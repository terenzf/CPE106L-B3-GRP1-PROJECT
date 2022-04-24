print ("** Please log in your email and password **")

emailAdd = input ("Email Address: ")
print (emailAdd)
ctr = True

print ("(Enter 8-16 characters for your password)")
while ctr == True:
    password = input ("Password: ")
    if len(password) >= 8 and len(password) <= 16:
        print ("* Your password is valid. \n")
        ctr = not ctr
    else:
        print (" Your Password is invalid! Please try again! *")
