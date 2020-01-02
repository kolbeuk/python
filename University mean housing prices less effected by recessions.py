import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the 
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ], 
    columns=["State", "RegionName"]  )
    
    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''

    # Read File list of university towns in the United States
    result = list()
    with open('university_towns.txt') as file:
        for line in file:
            # Strip whitespace 
            line = line.rstrip()
            # lines with edit are states
            if'[edit]' in line:
                state = line.replace('[edit]', '')
            elif '(' in line:
            # find the ( and only take the part before it 
                    town = line[:line.index('(')-1] 
                    result.append([state,town])
            else:
                town = line
                result.append([state,town])
                
    unitowns = pd.DataFrame(result, columns=['State', 'RegionName'])

    return unitowns

get_list_of_university_towns()

def get_recession_start():
    import pandas as pd
    import numpy as np
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
        # Read File From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars 
    GDP = pd.read_excel('gdplev.xls',
                           header=None,
                           skiprows=220,
                           names=['Quarter', 'GDP'],
                           parse_cols=[4,5])
    GDP.index.name = 'Quarter'
    for i in range(0,GDP.shape[0]-1):
        if (GDP.iloc[i-2][1]> GDP.iloc[i-1][1]) and (GDP.iloc[i-1][1]> GDP.iloc[i][1]):
            startdate= GDP.iloc[i-3][0]
    return  startdate

get_recession_start()


def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    import pandas as pd
    import numpy as np
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
        # Read File From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars 
    GDP = pd.read_excel('gdplev.xls',
                           header=None,
                           skiprows=220,
                           names=['Quarter', 'GDP'],
                           parse_cols=[4,5])
    GDP.index.name = 'Quarter'
    start = get_recession_start()
    start_index = GDP[GDP['Quarter'] == start].index.tolist()[0]
    GDP=GDP.iloc[start_index:]
    for i in range(2, len(GDP)):
        if (GDP.iloc[i-2][1] < GDP.iloc[i-1][1]) and (GDP.iloc[i-1][1] < GDP.iloc[i][1]):
            return GDP.iloc[i][0]

get_recession_end()

def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    import pandas as pd
    import numpy as np
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
        # Read File From Bureau of Economic Analysis, US Department of Commerce, the GDP over time of the United States in current dollars 
    GDP = pd.read_excel('gdplev.xls',
                           header=None,
                           skiprows=220,
                           names=['Quarter', 'GDP'],
                           parse_cols=[4,5])
    GDP.index.name = 'Quarter'
    start = get_recession_start()
    start_index = GDP[GDP['Quarter'] == start].index.tolist()[0]

    end= get_recession_end()
    end_index = GDP[GDP['Quarter'] == end].index.tolist()[0]
    
    GDPW = GDP.iloc[start_index:end_index+1]
    bottom = GDPW.groupby('GDP').min()
    return bottom.iloc[0]['Quarter']

get_recession_bottom()

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    # Read File Zillow research data site there is housing data for the United States.
    housedata = pd.read_csv('City_Zhvi_AllHomes.csv', header=0, usecols=[1,2,*range(51,251)])
    housedata.replace({'State':states}, inplace = True)
    housedata.set_index(['State','RegionName'],inplace = True)
    
    # Convert to qtrs
    houseqtr = (housedata.groupby(pd.PeriodIndex(housedata.columns, freq='Q'), axis=1)
                        .apply(lambda x: x.mean(axis=1)))
    houseqtr.columns = houseqtr.columns.strftime('%Yq%q')
    
    return houseqtr

convert_housing_data_to_quarters()

def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    # get values for recession 
    bstart = get_recession_start()
    rend = get_recession_end()
    rbottom = get_recession_bottom()

    # get file details.
    unitowns = get_list_of_university_towns()
    housingdata = convert_housing_data_to_quarters()

    # Set raito for house prices, start one qtr before recession
    housingdata = housingdata.reset_index()
    rstart = housingdata.columns[housingdata.columns.get_loc(bstart)-1]
    housingdata['ratio'] = housingdata[rstart].div(housingdata[rbottom])
    
    #create lists of uni and nonuni housing data
    unitowns_data = pd.merge(housingdata, unitowns, how='inner') 
    unitowns_data['unitown'] = True
    nonunitowns_data = pd.merge(housingdata, unitowns_data, how='outer')
    
    #Check point from Coursera 
    # You have 269 university towns from master file of 517 towns 
    # 10461 non-university towns from housingdata file of 10730
    unitowns_result = unitowns_data[unitowns_data['unitown'] == True]
    nonunitowns_result = nonunitowns_data[nonunitowns_data['unitown'] != True]
    
    # calcuate the p-value and stats
    statistic, p_value = ttest_ind(unitowns_result['ratio'].dropna(), nonunitowns_result['ratio'].dropna())
    
    different = True if p_value < 0.01 else False
    better = "university town" if unitowns_result['ratio'].mean() < nonunitowns_result['ratio'].mean() else "non-university town"

    print(unitowns_result['ratio'].mean())
    print(nonunitowns_result['ratio'].mean())
    return (different, p_value, better)

run_ttest()
