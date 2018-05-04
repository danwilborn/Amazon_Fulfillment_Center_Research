#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('adjacent_counties.csv')
non_adj_counties_df = pd.read_csv('non_adjacent_counties.csv')
unemployment_rate_df = pd.read_csv('Unemployment_Rate.csv')

# Join Adjacent Counties with County Data
joined_counties_df = pd.merge(counties_df, unemployment_rate_df, how='inner', left_on=['County','State'], right_on=['County','State'])
joined_non_adj_counties_df = pd.merge(non_adj_counties_df, unemployment_rate_df, how='inner', left_on=['County','State'], right_on=['County','State'])

#print(joined_counties_df)


# Need to convert to dictionary of dataframes
opened_1997 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 1997]
opened_1999 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 1999]
opened_2000 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2000]
opened_2005 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2005]
opened_2006 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2006]
opened_2007 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2007]
opened_2008 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2008]
opened_2009 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2009]
opened_2010 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2010]
opened_2011 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2011]
opened_2012 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2012]
opened_2013 = joined_counties_df.loc[joined_counties_df['Year Opened'] == 2013]


'''
year = 2007
year_totals = dict.fromkeys([2007, 2008, 2009, 2010, 2011, 2012])
year_averages = dict.fromkeys([2007, 2008, 2009, 2010, 2011, 2012])


for i, row in opened_2007.iterrows():
    for j in range(0,4):
        year_totals[year] += row[str(year)]
        year += 1
    year = 2007
'''

for year in range(2007,2012):
    avg = opened_2007[str(year)].mean()
    
for year in range(2010,2015):
    avg = opened_2010[str(year)].mean()
    print(avg)

