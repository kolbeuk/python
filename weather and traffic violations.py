import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
import numpy as np

# month mapping for pivot tables
months={'April': '04',
            'August': '08',
            'December': '12',
            'February': '02',
            'January': '01',
            'July': '07',
            'June': '06',
            'March': '03',
            'May': '05',
            'November': '11',
            'October': '10',
            'September': '09'}

#data set from https://www.ncdc.noaa.gov
# stormevents in USA
dfs = pd.read_csv('StormEvents_details-ftp_v1.0_d2015_c20191116.csv')

#data set from data_world, this is an SQL subset of the data.  https://data.world/dataneer/tsopp-mi. 
#[TSOPP] Police Traffic Stops for Michigan 2001–2016
dfp = pd.read_csv('police-tsopp-mi-QueryResult-2.csv')

# subset the dataset and change months to numbers
dfs = dfs[dfs['STATE'] == 'MICHIGAN']
dfs['MONTH_NAME']= dfs['MONTH_NAME'].map(months)

# prepare pivot table for strom events
wevent = dfs.groupby(['MONTH_NAME', 'EVENT_TYPE'])['EVENT_TYPE'].agg(['count'])
wevent.sort_values(by=['MONTH_NAME', 'EVENT_TYPE'], inplace=True, ascending=True)
wevent = wevent.reset_index()
wflatdata = wevent.pivot(index='EVENT_TYPE', columns = 'MONTH_NAME', values='count')
ay = wflatdata.plot(kind="bar", stacked=True,figsize=(14,10))
ay.set_ylabel('Number of Severe Weather Reports')
ay.set_xlabel('Severe Weather Types')
ay.set_title('Severe Weather in Michigan 2015')

# prepare pivot table for police violations
dfp['MONTH_NAME'] = dfp['stop_date'].str[5:7]
pevent = dfp.groupby(['MONTH_NAME', 'violation'])['violation'].agg(['count'])
pevent.sort_values(by=['MONTH_NAME', 'violation'], inplace=True, ascending=True)
pevent = pevent.reset_index()
pflatdata = pevent.pivot(index='violation', columns = 'MONTH_NAME', values='count')
pflatdata = pflatdata[pflatdata.sum(axis=1) > 2120]

ax = pflatdata.plot(kind="bar", stacked=True,figsize=(14,10))
ax.set_ylabel('Number of Violations')
ax.set_xlabel('Violations')
ax.set_title('Traffic Violations in Michigan 2015')
