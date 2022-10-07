var1=2

print("1" ,var1==3) #prints out false
print(var1!=3) #prints true

mylist=[1,2,3]
print(var1 in mylist) #prints true

print(var1 is var1) #prints true # compares if true or false

statement= True
another_statement = False
print(statement==another_statement)
print(not (statement is another_statement))

print("using if statements")
myname="John"
namelist = ["John", "Doe"]
if myname in namelist:
    print("Your name is %s or %s"% (namelist[0],namelist[1]))