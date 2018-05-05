#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


center_df = pd.read_csv('../data/csv/fulfillment_centers.csv')
population_df = pd.read_csv('../data/csv/county_population.csv')
commuting_df = pd.read_csv('../data/csv/commuting_flows.csv')


# Joining center data with commuting data
work_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['work_county','work_state'])
residence_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['residence_county','residence_state'])

# Joining center/commuting data with population data
work_counties_df = pd.merge(work_counties_df, population_df, how='inner', left_on=['work_county','work_state'], right_on=['CTYNAME','STNAME'])
residence_counties_df = pd.merge(residence_counties_df, population_df, how='inner', left_on=['residence_county','residence_state'], right_on=['CTYNAME','STNAME'])


non_adjacent_counties= set()
only_counties = set()

for i, row in work_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] < .00001:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        non_adjacent_counties.add((row['work_county'],row['work_state'],FIPS,row['Year Opened']))
        only_counties.add((row['work_county'],row['work_state']))

for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] < .00001:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        non_adjacent_counties.add((row['work_county'],row['work_state'],FIPS,row['Year Opened']))
        only_counties.add((row['work_county'],row['work_state']))

print(len(non_adjacent_counties))
print(len(only_counties))
#print(adjacent_counties)

with open('../data/csv/non_adjacent_counties.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['County','State','FIPS','Year Opened'])
    for row in non_adjacent_counties:
        csv_out.writerow(row)

