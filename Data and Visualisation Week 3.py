import matplotlib.pyplot as plt
import statsmodels.stats.api as sms
from scipy import stats
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

df

df.describe()

threshold = 42000
mean = df.mean(axis=1)
std = df.std(axis=1)
n = df.shape[1]
yerr = std/np.sqrt(n) * ss.t.ppf(1-0.05/2, n-1)

plt.figure(1, figsize=(7, 6))

plt.axhline(y=threshold, color = 'black', label = 'davidkolb')
plt.text(4, threshold, threshold, fontsize=20, va='center', ha='center', backgroundcolor='w')
         
bar=plt.bar(range(df.shape[0]), mean, yerr = yerr,color=['blue','gray','blue','red'],)

plt.title('Data between 1992 and 1995 (David)')
index = range(len(df.index))
plt.xticks(index, df.index)
plt.show()

