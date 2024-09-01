import json
import pandas as pd
import os

with open('pokemon_db.json', 'r') as file:
    pockimon_ls = json.load(file)

sort=input("enter the number of the sort type you want to use 1-name 2-type 3-number")
filtered_pockimon = []

if sort=='1':
    pockimon_name=input("enter the name")
    for pockimon in pockimon_ls:
        if pockimon['name']==pockimon_name: 
            filtered_pockimon.append(pockimon)
            
if sort=='2':
    pockimon_type=input("enter the type")
    for pockimon in pockimon_ls:
        if pockimon['type_one']==pockimon_type:
            filtered_pockimon.append(pockimon)

if sort=='3':
    pockimon_number=input("enter the number")
    for pockimon in pockimon_ls:
        if pockimon['number']==pockimon_number:                        
            filtered_pockimon.append(pockimon)

df = pd.DataFrame([filtered_pockimon])
df.to_excel("pockimon.xlsx", index=False)
os.startfile('pockimon.xlsx')