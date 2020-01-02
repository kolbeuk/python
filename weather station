%matplotlib notebook

import matplotlib.pyplot as plt
import mplleaflet
import pandas as pd
import datetime

df = pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

# record high and record low temperatures by day of the year over the period 2005-2014

# extract and shape the 2015 data
data2015 = df.where(df['Date'].str.contains('2015')).dropna()
data2015['Date'] = data2015.Date.str[5:]
high2015 = data2015.groupby('Date')['Data_Value'].max()
low2015 = data2015.groupby('Date')['Data_Value'].min()

# extract and shape the monthly data min and max
df['Date'] = df.Date.str[5:]
df = df[df['Date'] != '02-29']
high = df.groupby('Date')['Data_Value'].max()
low = df.groupby('Date')['Data_Value'].min()

record_high2015 = high2015[high2015 >= high.reindex_like(high2015)]
record_low2015 = low2015[low2015 <= low.reindex_like(low2015)]

x = [n for n in range(0,365) if (high2015.iloc[n] >= high.iloc[n]) ]
y = [n for n in range(0,365) if (low2015.iloc[n] <= low.iloc[n])]

import numpy as np

plt.figure(figsize=(12,10))

#note the date range has to be one further to incldue the last day
observation_dates = np.arange('2015-01-01', '2016-01-01', dtype='datetime64[D]')
observation_dates = list(map(pd.to_datetime, observation_dates))

#Setup the charge legend and names
plt.xlabel('Day of Year')
plt.ylabel('Temperature (tenths of degrees C')
plt.title('Record highest and lowest temperature by day of the year')

# rotate the tick labels for the x axis
xa = plt.gca().xaxis
for item in xa.get_ticklabels():
    item.set_rotation(45)
    
#plt.plot(observation_dates, high2015, '-', observation_dates, low2015, '-', zorder=1)
plt.plot(high.values, c = 'red', label ='Record High', linewidth=0.5)
plt.plot(low.values, c = 'blue', label ='Record Low', linewidth=0.5)

plt.gca().fill_between(range(len(low)), low, high, facecolor='lightgray', alpha=0.25)

#4.	Overlay a scatter of the 2015 data for any points (highs and lows) for which the ten year record (2005-2014) record high or record low was broken in 2015
# x and y are list range upto 365
plt.scatter(x, record_high2015, c = 'blue',zorder=2, s=90, alpha=0.4, label = 'Broken High in 2015')
plt.scatter(y, record_low2015, c = 'red', zorder=2, s=90, alpha=0.4, label = 'Broken Low in 2015')

plt.legend(loc = 8, fontsize=18, frameon = False)
