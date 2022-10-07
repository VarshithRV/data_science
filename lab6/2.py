#############################################################
'''
CS20B1096
VARSHITH R V


NOTE : 
-For simplicity, account number is made '1', '8S' and '7' respectively


'''
#############################################################

import pandas as pd

# Create the basic data frame

d = {"Name":["Ram","Sam","Prabhu"], 
	"Account_Number":["1","8","7"],
	"Account_Type":["SB","CA","SB"],
	"Adhaar_No":["959389389173","959389389179","959389389159"],
	"Balance":[8989839,7690990,989330]}

df = pd.DataFrame(d)
df.to_csv('SBIAccountHolder.csv', index=False)

print(df)

# Menu driven program

print("Enter 1 to append record")
print("Enter 2 to delete a record")
print("Enter 3 to credit a record")
print("Enter 4 to debit a record")
print("Enter 5 to print the records")


while(True):
	
	choice = int(input("Enter your choice : "))

	if(choice == 0): # break
		break

	elif(choice == 1): # append a row
		account_number = input("Enter the account number : ")
		name = input("Enter the name : ")
		account_type = input("Enter the account_type : ")
		adhaar_no = input("Enter the aadhaar number : ")
		balance = input("Enter the balance : ")
		d2 = {"Name":[name], "Account_Number":[account_number],
				"Account_Type":[account_type], "Adhaar_No":[adhaar_no],
				"Balance":[balance]}
		print(d2)
		df2 = pd.DataFrame(d2) 
		print(df2)
		df = df.append(df2,ignore_index = True)
		print("After appending the row : \n",df)
		df.to_csv('SBIAccountHolder.csv', index=False)
	
	elif(choice == 2): # drop a row
		index = int(input("Enter the index to be dropped : "))
		df = df.drop(index)
		print("Dataframe after modification : \n",df)
		df.to_csv('SBIAccountHolder.csv', index=False)

	elif(choice == 3): # credit
		credit = int(input("Enter the amount to be credited : "))
		accn = input("Enter your account number : ")
		index = df[df['Account_Number']=="7"].index.values
		#print(index[0])
		print("Balance before credit : ",df.at[0,'Balance'])
		df.at[0,'Balance'] += credit
		print("Balance after credit : ",df.at[0,'Balance'])
		df.to_csv('SBIAccountHolder.csv', index=False)

	elif(choice == 4): # debit
		debit = int(input("Enter the amount to be debited : "))
		accn_type = input("Enter the account type : ")
		accn = input("Enter the account number : ")
		index = df[df['Account_Number'] == accn].index.values
		if(accn_type == 'SB'):
			if(df.at[index[0],'Balance']-debit<0):
				print("Error, broke lol")
			else:
				df.at[index[0],'Balance']-=debit
				print("Balance after debit = ",df.at[index[0],'Balance'])
		else:
			print("Balance before debit = ",df.at[index[0],'Balance'])
			df.at[index[0],'Balance']-=debit
			print("Balance after debit = ",df.at[index[0],'Balance'])
		df.to_csv('SBIAccountHolder.csv', index=False)

	elif(choice == 5): #print the details given the account number
		accn = input("ENter the account number : ")
		index = df[df['Account_Number'] == accn].index.values
		print(df.loc[index])

	else:
		print("Wrong choice!!Enter agian.")


# creating a second dictionary
d2 = {"Name":["Ram","Sam","Prabhu"],"Adhaar_No":["959389389173","959389389179","959389389159"],
	"Contact_No":["9840787333","9840787343","9840787353"],
      "DOB":['12-2-1990','12-2-2000','12-2-2010'],
      "Address":['No 23, Kandigai, Chennai 127','No 73, Melakottiaiyu, Chennai 127','No 43, Melakottiaiyu, Chennai 127']}

df2 = pd.DataFrame(d2)
print("New data frame : \n",df2)
df2.to_csv('Aadhar_DB.csv', index=False)

## merging the two files to create a new file :
output1 = pd.merge(df, df2, 
                   on='Adhaar_No', 
                   how='inner')

print("merged data frame : ",output1)
output1.to_csv('merge.csv', index = False)


			
			

		
		
		
