## lists class :
'''
functions :
index : returns the int type index of the element
append : append the element
extend : to add the elements of another list to our list
sort : to sort the list
reverse : to reverse the list
insert : to insert an element
remove : to remove an element based on value
pop : to remove an element based on index
count : to count the elements
copy : copy the list to another list??
clear : clear the list
'''
mylist = ['1',2,3]
print(mylist,type(mylist[0]),len(mylist)) # type and len function

mylist.append(1) # append function
print(mylist,type(mylist[mylist.index(1)])) # index funtion

## traversing through the list:
for x in mylist:
    print(x)

## to get index of an element
print("The index of str type 1 : ",mylist.index('1'))

list2 = ['Hello','World','Bla']
mylist.extend(list2) # extend function
print("List after extending ",mylist)

mylist.insert(2,'Insert')# insert element list.insert(<index>,<element>)
print("List after inserting : ",mylist)

mylist.remove(1)
print("List after removing 1 : ",mylist)

print("Number of 1 in the list : ",mylist.count('1'))

mylist.pop(1) # remove an element based on index
print("modifiend list : ",mylist)

list1 = mylist.clear()
print(list1)
