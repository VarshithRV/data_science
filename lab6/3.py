import pandas as pd

# Create the basic data frame

d = {"Name":["Ram","Sam","Prabhu"], 
	"Account_Number":["1","8","7"],
	"Account_Type":["SB","CA","SB"],
	"Adhaar_No":["959389389173","959389389179","959389389159"],
	"Balance":[8989839,7690990,989330]}

df = pd.DataFrame(d)

# debit, update
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

print(df)

accn = input("ENter the account number : ")
print(df.loc[index])
