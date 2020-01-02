import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import pandas as pd
import numpy as np

#data set from https://www.ncdc.noaa.gov › stormevents
dfs = pd.read_csv('StormEvents_details-ftp_v1.0_d2015_c20191116.csv')

#data set from data_world
dfp = pd.read_csv('police-tsopp-mi-QueryResult-2.csv')

dfs = dfs[dfs['STATE'] == 'MICHIGAN']

# prepare pivot table for strom events
wevent = dfs.groupby(['MONTH_NAME', 'EVENT_TYPE'])['EVENT_TYPE'].agg(['count'])
wevent.sort_values(by=['MONTH_NAME', 'EVENT_TYPE'], inplace=True, ascending=True)
wevent = wevent.reset_index()
wevent.pivot(index='EVENT_TYPE', columns = 'MONTH_NAME', values='count')

# prepare pivot table for police violations
dfp['MONTH_NAME'] = dfp['stop_date'].str[5:7]
pevent = dfp.groupby(['MONTH_NAME', 'violation'])['violation'].agg(['count'])
pevent.sort_values(by=['MONTH_NAME', 'violation'], inplace=True, ascending=True)
pevent = pevent.reset_index()
pevent.pivot(index='violation', columns = 'MONTH_NAME', values='count')

