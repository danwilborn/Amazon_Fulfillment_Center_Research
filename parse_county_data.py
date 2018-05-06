#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')
non_adj_counties_df = pd.read_csv('../data/csv/non_adjacent_counties.csv')
unemployment_rate_df = pd.read_csv('../data/csv/Unemployment_Rate.csv')

# Join Adjacent Counties with County Data
joined_counties_df = pd.merge(counties_df, unemployment_rate_df, how='inner', left_on=['County','State'], right_on=['County','State'])
joined_non_adj_counties_df = pd.merge(non_adj_counties_df, unemployment_rate_df, how='inner', left_on=['County','State'], right_on=['County','State'])

#print(joined_counties_df)

with open('../data/csv/year_and_county_data.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['FIPS', 'State', 'County', 'Year_Opened', 'Year', 'Time_Dummy', 'Near_Dummy', 'Unemployment'])
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
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy])

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
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy])



