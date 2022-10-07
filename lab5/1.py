# Menu driven programming for matrix manipulation using numpy
import numpy as np

# Two matrices
mx1 = np.array([[5, 10], [15, 20]])
mx2 = np.array([[25, 30], [35, 40]])

## Big list
matrix = []

# Input function : 
row = (int)input("Enter the number of rows : ")
column = (int)(input("Enter the number of columns : "))

j = 0
while j < row
	# inpt a list and append it
	i = 0
	list = []
	while i < column:
		temp = (int)(input("Enter the element : "))
		list.append(temp)
		i += 1
	matrix.append(list)
	print(list)

print(matrix)




print("Matrix1 =\n",mx1)
print("\nMatrix2 =\n",mx2)

# The addition() is used to add matrices
print ("\nAddition of two matrices: ")
print (np.add(mx1,mx2))

# The subtract() is used to subtract matrices
print ("\nSubtraction of two matrices: ")
print (np.subtract(mx1,mx2))

# The divide() is used to divide matrices
print ("\nMatrix Division: ")
print (np.divide(mx1,mx2))

# The multiply()is used to multiply matrices
print ("\nMultiplication of two matrices: ")
print (np.multiply(mx1,mx2))

