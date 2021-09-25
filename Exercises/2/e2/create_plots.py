import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from natsort import index_natsorted

filename1 = sys.argv[1]
filename2 = sys.argv[2]

df1 = pd.read_csv(filename1, sep=' ', header=None, index_col=1,
            names=['lang', 'page', 'views', 'bytes'])
df2 = pd.read_csv(filename2, sep=' ', header=None, index_col=1,
            names=['lang', 'page', 'views2', 'bytes'])


df1 = df1.sort_values(by=['views'], ascending=True)
df2 = df2.sort_values(by=['views2'], ascending=True)

df3 = pd.concat([df1, df2['views2']], axis=1)

print(df3)

df1 = df1.sort_values(by=['views'], ascending=False)

plt.figure(figsize=(10,5)) #Change the size to something sensible
plt.subplot(1, 2, 1) #Subplots in 1 row, 2 columns, select the first
plt.plot(df1['views'].values) #build plot 1
plt.title("Page vs Views")
plt.xlabel("Page")
plt.ylabel("Views")
plt.subplot(1, 2, 2) #Subplots in 1 row, 2 columns, select the second
plt.scatter(df3['views'], df3['views2']) #build plot 2
plt.xscale('log') #Scaling x axis
plt.yscale('log') #Scaling y axis
plt.title("Page Views - Hour 1 vs Hour 2")
plt.xlabel("Hour 1 Page Views")
plt.ylabel("Hour 2 Page Views")
plt.savefig('wikipedia.png')

