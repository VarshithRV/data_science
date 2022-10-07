### Menu driven program for set operations in py

set1 = {1,2,3,4}
set2 = {4,3,5,6}
#set1.discard(4)
#print("Set1 : ",set1)
#print("Set2 : ",set2)
# print(type(set1),type(set2))

#set1 = set({})
#set2 = set({})
resultset = set({})

while True:
    print("Hello!, here are your choices : ")
    print("Enter 1 to create a new empty set.")
    print("Enter 2 to insert a new element in a given set.")
    print("Enter 3 to delete an element in a set.")
    print("Enter 4 to search for an element in a set.")
    print("Enter 5 to print a set.")
    print("Enter 6 to get the union of two sets.")
    print("Enter 7 to get the intersection of two sets.")
    print("Enter 8 to get the set difference of two sets.")
    print("Enter 9 to get the symmetric difference of two sets.")
    print("Enter 0 to EXIT.")

    mychoice = int(input("Enter your choice : "))
    
    # Initialize empty set
    if mychoice == 1:
        set1.clear()
        set2.clear()
        print("\nBoth set1 and set2 are cleared.\n")
    
    # Insert operation
    if mychoice == 2:
        sentinel = input("Enter 1 to insert elements into set1, enter 2 to insert elements into set2 : ")
        if sentinel == '1':
            myelement = int(input("Enter the element to be inserted into set1 : "))
            set1.add(myelement)
        elif sentinel == '2':
            myelement = int(input("Enter the element to be inserted into set2 : "))
            set2.add(myelement)
        else:
            print("Enter a valid sentinel.")
    

    #delete operation
    if mychoice == 3:
        sentinel = input("Enter 1 to delete elements from set1, enter 2 to delete elements from set2 : ")
        if sentinel == '1':
            myelement = int(input("Enter the element to be deleted from set1 : "))
            set1.discard(myelement)
        elif sentinel == '2':
            myelement = int(input("Enter the element to be deleted from set2 : "))
            set2.discard(myelement)
        else:
            print("Enter a valid sentinel.")        

    # Search operation
    if mychoice == 4:
        sentinel = input("Enter 1 to search from set 1, 2 to search from set 2")
        if sentinel == '1':
            myelement = int(input("Enter the element to search from set1"))
            if myelement in set1:
                print("\n",myelement, " is present in set1\n")
        elif sentinel == '2':
            myelement = int(input("Enter the element to search from set2"))
            if myelement in set2:
                print("\n",myelement, " is present in set2\n")
        else:
            print("Enter a valid sentinel.")

    # Print operation
    if mychoice == 5:
        print("\nSet1 : ",set1)
        print("Set2 : ",set2,"\n")

    # Union operation
    elif mychoice == 6:
        resultset = set1 | set2
        print("\nUnion of the two set : ",resultset,"\n")

    # Intersection operation
    elif mychoice == 7:
        resultset = set1 & set2
        print("\nIntersection of the two sets : ",resultset,"\n")

    # Set Difference
    elif mychoice == 8:
        sentinel = input("Enter 1 if set1 - set2 or 2 if set2-set1 : ")
        if sentinel == '1':
            resultset = set1 - set2
            print("\nSet1 - set2 : ",resultset,"\n")
        elif sentinel == '2':
            resultset = set2 - set1
            print("\nSet2 - set1 : ",resultset,"\n")
        else :
            print("Enter a valid opition.")

    # Symmetric Difference
    elif mychoice == 9:
        resultset = set1 ^ set2
        print("\nThe symmetric difference : ",resultset,"\n")

    # Exit operation
    elif mychoice == 0:
        break


