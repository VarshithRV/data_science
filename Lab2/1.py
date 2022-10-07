# Creating a menu driven program for implement student details in a dictionary

mydictionary={}

while True:
    print("Hello!, Here are your choices : ")
    print("Enter 1 to insert")
    print("Enter 2 to delete")
    print("Enter 3 to search")
    print("Enter 4 to exit")

    mychoice = int(input("Please Enter your choice : " ))
    # print(mychoice)

    if mychoice == 1:
        rollnumber = input("Enter the rollnumber : ")
        name = input("Enter the name : ")
        cgpa = input("Enter the CGPA : ")
        phone = input("Enter the Phone number : ")
        mydictionary[rollnumber] = [name,cgpa,phone]
        # print(mydictionary)

    elif mychoice == 2:
        rollnumber = input("Enter the rollnumber: ")
        mydictionary.pop(rollnumber)
        # print(mydictionary)

    elif mychoice == 3:
        rollnumber = input("Enter the rollnumber: ")
        print(rollnumber, ":" ,mydictionary.get(rollnumber))
        
    elif mychoice == 4:
        break

    else :
        print("")
        print("ENTER A VALID OPTION!!")
        print("\n")
