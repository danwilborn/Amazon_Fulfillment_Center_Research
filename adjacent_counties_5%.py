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


adjacent_counties= set()
only_counties = set()

for i, row in work_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .05:
        FIPS = format(row['residence_state_FIPS'], '02d')+format(row['residence_county_FIPS'], '03d')
        if (row['residence_county'],row['residence_state']) not in only_counties:
            only_counties.add((row['residence_county'],row['residence_state']))
            adjacent_counties.add((row['residence_county'],row['residence_state'],str(FIPS),row['Year Opened']))
        
for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .05:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        if (row['work_county'],row['work_state']) not in only_counties:
            only_counties.add((row['work_county'],row['work_state']))
            adjacent_counties.add((row['work_county'],row['work_state'],str(FIPS),row['Year Opened']))

print(len(adjacent_counties))
print(len(only_counties))
#print(adjacent_counties)

with open('../data/csv/adjacent_counties_5%.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['County','State','FIPS','Year Opened'])
    for row in adjacent_counties:
        csv_out.writerow(row)

