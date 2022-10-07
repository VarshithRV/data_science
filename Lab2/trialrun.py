mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
mylist.append(4)
mylist.append("Hellloworld")
mylist[3] = "change"
print(mylist)
# string formatting
print("Hello %s!"%("johon"))
print("My list is %s"%(mylist))
print(type(mylist[3]),type(mylist[2]))

# mynum= input("Enter your number : ")
#print(mynum)

# sets and set operation functions
myset = {1,3}
# sets are unordered :
myset.add(2)
print(myset)
myset.add(2)
print(myset)
myset.update([4,5,2,3])
print(myset)
myset.discard(4)
print(myset)
#myset.clear

## SET OPERATIONS:
myset2 = {1,2,3,4,5,6,7,8,9,0}
# union
newset = myset | myset2
print(newset)
