## sets in python

thisset = set()# to create an empty set
x = 5 in thisset # returns false if the element is not there in the set
print(x,len(thisset))

### add operation :
thisset.add(5)
print(thisset,5 in thisset)

## create a non empty set
set2 = {1,2,3,4,5}# unordered, non repetitive
print(set2,5 in set2)

## remove set item ;
set2.remove(3)
print(set2)

## loop set items
for y in set2:
    print(y)
set3 = {1,2,3,6,7,8}
print(set3)

##  union operation :
set_union = set2 | set3
print("Union",set_union)

## intersection operation :
set_intersection = set2 & set3
print("Intersection",set_intersection)

## set differece operation
set_diff = set2 - set3
print("Difference",set_diff)

## set sym difference operation :
set_sym = set2 ^ set3
print("Symmetric difference",set_sym)
