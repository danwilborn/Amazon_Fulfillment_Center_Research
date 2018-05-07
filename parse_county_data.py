#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')
non_adj_counties_df = pd.read_csv('../data/csv/non_adjacent_counties.csv')


with open('../data/csv/year_and_county_data.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['FIPS', 'State', 'County', 'Year_Opened', 'Year', 'Time_Dummy', 'Near_Dummy', 'Time*Near', 'Annual_Wage'])

    for Year in range(1994,2016):
        wage_df = pd.read_csv('../data/csv/wage_files/'+str(Year)+'.annual.singlefile.csv')
        wage_df = wage_df[['area_fips', 'industry_code', 'own_code', 'avg_annual_pay']]
        wage_df = wage_df[wage_df['industry_code'] == '10']
        wage_df = wage_df[wage_df['own_code'] == 0]
        wage_and_counties_df = pd.merge(counties_df, wage_df, how='inner', left_on='FIPS', right_on="area_fips")
        
        for i, row in wage_and_counties_df.iterrows():
            FIPS = row['FIPS']
            State = row['State']
            County = row['County']
            Year_Opened = row['Year Opened']
            Near_Dummy = 1
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Wage = row['avg_annual_pay']
            time_near_interaction = Near_Dummy*Time_Dummy
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, time_near_interaction, Wage])                                     

        wage_and_non_adj_counties_df = pd.merge(non_adj_counties_df, wage_df, how='inner', left_on='FIPS', right_on="area_fips")
        #wage_and_non_adj_counties_df.drop_duplicates(subset=['FIPS', 'State', 'County', 'avg_annual_pay'], keep='first')        

        for i, row in wage_and_non_adj_counties_df.iterrows():
            FIPS = row['FIPS']
            State = row['State']
            County = row['County']
            Year_Opened = row['Year Opened']
            Near_Dummy = 0
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Wage = row['avg_annual_pay']
            time_near_interaction = Near_Dummy*Time_Dummy
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, time_near_interaction, Wage])           
    






'''
    for i, row in joined_counties_df.iterrows():
        FIPS = row['FIPS']
        State = row['State']
        County = row['County']
        Year_Opened = row['Year Opened']
        Near_Dummy = 1
        for Year in range(2007,2016):
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Unemployment = row[str(Year)]
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, Unemployment])

    for i, row in joined_non_adj_counties_df.iterrows():
        FIPS = row['FIPS']
        State = row['State']
        County = row['County']
        Year_Opened = row['Year Opened']
        Near_Dummy = 0
        for Year in range(2007,2016):
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Unemployment = row[str(Year)]
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, Unemployment])
    '''


