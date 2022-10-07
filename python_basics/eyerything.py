from xml.dom.minidom import TypeInfo


print("Helloworld")

a, b = 3, 4
myfloat = 7.0
print("These are my vars",a,b,int(myfloat),myfloat)

# lists

mylist=[1,2,3,4]
mylist.append(1)
print(mylist,mylist[3])

# Input
myvar=input("Prompt : ")
print(myvar,type(myvar))