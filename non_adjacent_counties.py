#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


center_df = pd.read_csv('fulfillment_centers.csv')
population_df = pd.read_csv('county_population.csv')
commuting_df = pd.read_csv('commuting_flows.csv')


# Joining center data with commuting data
work_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['work_county','work_state'])
residence_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['residence_county','residence_state'])

# Joining center/commuting data with population data
work_counties_df = pd.merge(work_counties_df, population_df, how='inner', left_on=['work_county','work_state'], right_on=['CTYNAME','STNAME'])
residence_counties_df = pd.merge(residence_counties_df, population_df, how='inner', left_on=['residence_county','residence_state'], right_on=['CTYNAME','STNAME'])


non_adjacent_counties= set()
only_counties = set()

for i, row in work_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] < .000001:
        non_adjacent_counties.add((row['residence_county'],row['residence_state'],row['Year Opened']))
        only_counties.add((row['residence_county'],row['residence_state']))

for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] < .000001:
        non_adjacent_counties.add((row['work_county'],row['work_state'],row['Year Opened']))
        only_counties.add((row['work_county'],row['work_state']))

print(len(non_adjacent_counties))
print(len(only_counties))
#print(adjacent_counties)

with open('non_adjacent_counties.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['County','State','Year Opened'])
    for row in non_adjacent_counties:
        csv_out.writerow(row)
