import pandas as pd
from io import StringIO
import re 

f = open("Day4Input.txt", "r")
text = f.read()
text = text.replace('\n', '*').replace('**', '\n').replace('*', ' ')
data = StringIO(text)
print(text)

columns = [
    "byr",# (Birth Year)",
    "iyr",#  (Issue Year)",
    "eyr",#  (Expiration Year)",
    "hgt",#  (Height)",
    "hcl",#  (Hair Color)",
    "ecl",#  (Eye Color)",
    "pid",#  (Passport ID)",
    "cid"]#  (Country ID)"

data=pd.read_csv(data, names= ["Raw", "byr","iyr","eyr","hgt","hcl","ecl","pid","cid"], header=None)

def datacheck(check):
    if check.find(col) > 0:
        #magic = r'\b'+col+'\S*'  
        magic = col+'\S+'   
        return str(re.search(magic, check)[0]).replace(col+":","")
    else:
        return 
for col in columns:
    data[col]=data.apply(lambda row: datacheck(row.Raw), axis=1)

data = data.drop(columns=["Raw"])

#print(data)

data['missing'] = data.apply(lambda x: 8-x.count(), axis=1)
print(data['missing'].value_counts())
print(data)