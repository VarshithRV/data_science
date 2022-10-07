# Python Documentation:

### Hello World:
Use the `print("Hello World!")` function to print the message "Hello World!".

> To print variables in a string, use 
> ```py
> print("The second name on the names list is %s" % var_name)
> ```

### Variables and Datatypes:
We dont need to declare variables in pythone, it is completely object oriented.
Python supports *integers*, *floating*, *complex numbers*, *strings* as variables.

eg: of simples variable declarations and operations.
```python
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
```

To declare floating point numbers:
```python
floatnum = 7.0
# or use
floatnum = float(7)
```
single quotes can be used to declare variables but double are preferred as it permits the use of aphostrophes.

multiple declarations and executions can be performed as shown:

```python
num1, num2 = 1 , 3
print(num1,num2)
```

operations between datatypes will not work.

## Lists
Python lists are very similar to arrays.
We can add any number of elements to a list.
```python
mylist = []
append.mylist(1)
append.mylist(2)
append.mylist(3)
print(mylist[0], mylist[1], mylist[2], mylist[0])
```

append is used to add elements to the next position of the list.
To linearly traverse through the list, use
```python
mylist = [1,2,3]
for x in mylist:
    print(x)
# to print an entire list, use
print(mylist)
```

## Operators in python
### Mathematical operators:
- \+ add operator
- \- sub operator
- \* multiply operator
- \/ divide operator
- \** power operator
- \% modulus operator
- \// floor div operator
  
operators can be used to modify strings and lists too.
```py
print("hello" + " " + "world!") #concate
print("hello " *10)# multiply
print([1,2,3]+[4,5,6])
print([1,2,3]*10)
```
Python uses C-style string formatting to create new, formatted strings. The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list), together with a format string, which contains normal text together with "argument specifiers", special symbols like "%s" and "%d".

for lists use the %s operator.

- %s - String (or any object with a string representation, like numbers)

- %d - Integers

- %f - Floating point numbers

- %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.

- %x/%X - Integers in hex representation (lowercase/uppercase)

> What is object data, dosent seem to be a list.
> ```py
> data=("john","doe","53.44")
> ```

### The object: string
The `len(string_name)` returns the length of the string.
```py
astring="Hello World"
print(astring.index("o")) # returns the index of o,
print(astring.count("l")) # returns the counts of l,
print(astring[2])# returns the elements in index 2,
print(astring[2:7])# returns the elements from index 2 through 6,
# If negative number is specified, then the reference is from the end of the string. 
# if we do not have a staring number, but just the colon, then it will print from the start of the string,
# if there is no ending number, then it will print till the end of the string.
print(astring[3:7:2])
# prints 3 thorugh 7 but skips one character.

#To  reverse a string, use this
print(astring[::-1])

# TO convert all characters to uppercase or lowercase use this
print(astring.upper())
print(astring.lower())

# To check if the string starts or ends with the characters, use this
print(astring.startswith("Hello"))
print(astring.endswith("World"))
# these return the values true or false.

# To split a string into lists containing strings, then use this:
afewwords = astring.split(" ") # splits at a " ".
```
## Conditions:

When an expression is compared or evaluated, a true or flase value is returned.
Boolean conditions:
```py 2 == 3 # This statement has a value and its false```

```py
x = 2
print(x == 3) # prints false
print(x == 2) # prints true
print(x < 3) # pritns true
```

### if, elif and else conditional statements
Syntax:
```py
if <condition> :
    # do something
elif <condition> :
    # do something
else:   
    # do something
```

### in operator
The `in` operator evaluates if the given variable is in the given list of values.<br>

`if name in ["Jogn", "Rick"]`

### is operator
The **is** operator compares the instance of the objects or the variables.
EG:
```py
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False
```

### not operator
The **not** operator inverts the value of a boolean expression.

> The `len` funtion can take in strings as well as lists.


