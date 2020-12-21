import pandas as pd

data = pd.read_csv('Day2Input.txt', sep=" ", header=None)
data.columns = ["Rule", "Letter", "Password"]
#print(data)

#Clean the Letter column
data['Letter'] = data['Letter'].str.replace(':', '')

#Split Rule column to Min and Max columns 
new = data["Rule"].str.split("-", n = 1, expand = True) 
data["Min"]= new[0] 
data["Max"]= new[1] 
data.drop(columns =["Rule"], inplace = True) 
data = data[["Min","Max", "Letter", "Password"]]

#Define a function to check the password
def passwordcheck(minposcheck,maxposcheck,check,pword):
    if ((pword[int(minposcheck)-1] == check) and (pword[int(maxposcheck)-1] != check)) or ((pword[int(minposcheck)-1] != check) and (pword[int(maxposcheck)-1] == check)):
        return "Yes"
    else:
        return "No"

#Iterate on the dataframe
data['Valid']=data.apply(lambda row: passwordcheck(row.Min, row.Max, row.Letter, row.Password), axis=1)

#Count the valid passwords
print((data['Valid']=='Yes').sum())

#print(data)  