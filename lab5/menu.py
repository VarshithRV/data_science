import numpy as np

def Input_matrix(row,column):
	matrix = [] # empty list
	list = [] # temp list to store rows
	j = 0
	while j < row:
		# inpt a list and append it
		i = 0
		list = []
		while i < column: # to input the ith row
			temp = (int)(input("Enter the element : "))
			list.append(temp)
			i += 1
		matrix.append(list)
		j += 1	
	return matrix


row = (int)(input("Enter the number of rows : "))
column = (int)(input("Enter the number of columns : "))

print("Enter the matrix one")
# numpy the matrix1 
mx1 = np.array(Input_matrix(row,column))
print(mx1)

print("Enter the matrix two")
# numpy the matrix2
mx2 = np.array(Input_matrix(row,column))
print(mx2)

# Menu for the program

print("Your choices are : ")	
print("0 to exit")
print("1 for mx1 + mx2 ")
print("2 for mx1 - mx2 ")
print("3 for scalar multiplication mx1 ")
print("4 for elementwise matrix multiplication ")
print("5 for mx1*mx2 ")
print("6 for (mx1)' ")
print("7 for trace(mx1)  ")
print("8 for solving a system of linear equaitons ")
print("9 for Det(mx1) ")
print("10 for Inverse(mx1) ")
print("11 for singular value decompositions of mx1 ")
print("12 for eigen value mx1 ")
print("13 to search an element in mx1 ")
print("14 for difference of sum of upper and lower triangular matrix mx1")

while True:
	choice = (int)(input("Enter your choice : "))
	if(choice == 0):
		break
	elif(choice == 1):
		print(np.add(mx1,mx2))
	elif(choice == 2):
		print(np.subtract(mx1,mx2))
	elif(choice == 3):
		n = (int)(input("Enter the number which should be mutliplied : ")		)
		print((mx1)*n)
	elif(choice == 4):
		print((mx1)*(mx2))
	elif(choice == 5):
		print(np.matmul(mx1,mx2))
	elif(choice == 6):
		print(mx1.T)
	elif(choice == 7):
		print(mx1.trace())
	elif(choice == 8):
		print(np.linalg.solve(mx1,mx2))
	elif(choice == 9):
		print(np.linalg.det(mx1))
	elif(choice == 10):
		print(np.linalg.inv(mx1))
	elif(choice == 11):
		print(np.linalg.svd(mx1))
	elif(choice ==12):
		print(np.linalg.eig(mx1))
	elif(choice == 13):
		y = int(input("Enter the search element : "))
		print(np.where(mx1 == y))
	elif(choice == 14):
		uppersum = 0
		lowersum = 0
		for i in range(row):
                        for j in range(column):
                                if (j <= i):
                                        lowersum += mx1[i][j];
		
		for i in range(row):
                        for j in range(column):
                                if (i <= j):
                                        uppersum += mx1[i][j];
	
		print(uppersum - lowersum)
	else:
		break
	
	

