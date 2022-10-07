import pandas as pd

# creating a secong dictionary
d2 = {"Name":["Ram","Sam","Prabhu"],"Adhaar_No":["959389389173","959389389179","959389389159"],
	"Contact_No":["9840787333","9840787343","9840787353"],
      "DOB":['12-2-1990','12-2-2000','12-2-2010'],
      "Address":['No 23, Kandigai, Chennai 127','No 73, Melakottiaiyu, Chennai 127','No 43, Melakottiaiyu, Chennai 127']}
df2 = pd.DataFrame(d2)
df2.to_csv('Aadhar_DB.csv', index=False)
df2 = pd.read_csv('Aadhar_DB.csv')
#print(df2)

     
d = {"Name":["Ram","Sam","Prabhu"], 
	"Account_Number":["1","8","7"],
	"Account_Type":["SB","CA","SB"],
	"Adhaar_No":["959389389173","959389389179","959389389159"],
	"Balance":[8989839,7690990,989330]}

df1 = pd.DataFrame(d)
df1.to_csv('SBIAccountHolder.csv', index=False)
df1 = pd.read_csv('SBIAccountHolder.csv')
print(df1,"\n",df2)

output1 = pd.merge(df1, df2, 
                   on='Adhaar_No', 
                   how='inner')

print(output1)
