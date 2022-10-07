astring = "Hello World"

# Print the length of astring
print(len(astring))

# Print the index of the first o
print(astring.index("o"))

# Print the number of 'l's in the string
print(astring.count("l"))

# Print the first 5 letter of the string
print(astring[:5])

# Print the slice from index 3 to 5
print(astring[3:6])

print(astring[3:7])

print(astring[3:7:1])

print(astring[3:7:2])

print(astring[3::1])

print(astring[3::2])

print(astring[::2])

print(astring[::-1])

print(astring[::-2])

afewwords = astring.split("H")

print(afewwords)