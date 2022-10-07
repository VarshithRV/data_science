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
myset.clear()
myset = {1,2,3,5,15,21}
myset2 = {1,2,3,4,5,6,7,8,9,0}
# union
newset = myset | myset2
print(newset) # myset.union(myset2) or myset2.union(myset)
# intersection
newset.clear()
newset = (myset & myset2)
print(newset)# msyet.intersection(myset2) myset2.intersection(myset)
# set difference
newset.clear()
newset = myset2 - myset #myset2.difference(myset)
print(newset)
# symmetric difference
newset.clear()
newset = myset ^ myset2 #myset.symmetricdifference(myset2)
print(myset)
# discard
print(myset)
myset.discard(2)
print(myset)
# check if an element is present in our set
set1 = set("apple")
print(set1)
print('p' in set1)
