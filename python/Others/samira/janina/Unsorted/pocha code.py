import os
import pandas as pd
path = r"E:\codes\python\Others\samira\janina\Unsorted"

files=os.listdir(path)

#print(files)

for a in range(len(files)):
    if files[0][-4:]==".xls":
        files.append(files.pop(0))
    else:
        files.pop(0)

#print(files)

filedir=path+"\\"+files[0]
print(filedir)
data = pd.read_excel(filedir)

col = data.columns[5]
date = col.rows[0]

print(date)