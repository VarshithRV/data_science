import numpy
row = 2
column = 2 
list = [[0,8],[2,3]]
mx1 = numpy.array(list)
print(mx1)

print(mx1[1][0])

uppersum = 0
lowersum = 0

## test
for i in range(row):
	for j in range(column):
		if (j <= i):
 	               lowersum += mx1[i][j];
print(lowersum)

for i in range(row):
        for j in range(column):
                if (i <= j):
                       uppersum += mx1[i][j];

print(uppersum)


