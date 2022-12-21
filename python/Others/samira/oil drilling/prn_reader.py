import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
import time
db = []

total_exec_time = 0
start=time.time()
file1=open("H12 ST1 (P6) Survey.prn","r")
for line in file1.readlines():
    line = [float(a) for a in line.split()]
    db.append(line)
end=time.time()
total_exec_time+=end-start
print("Reading from file...\t%.4f"%(end-start))
df = pd.DataFrame(db)
#print(df)
start=time.time()
df.columns = [str(a) for a in df.columns]
dfCols = [df[a] for a in df.columns]
fig, axes = plt.subplots(nrows=1,ncols=len(dfCols))
for a in range(len(dfCols)):
    dfCols[a].plot(ax=axes[a],c=[random.random()*0.75,random.random()*0.75,random.random()*0.75])
end=time.time()
total_exec_time+=end-start
print("Drawing plots...\t%.4f"%(end-start))
print("Total execution time...\t%.4f"%total_exec_time)
plt.show()