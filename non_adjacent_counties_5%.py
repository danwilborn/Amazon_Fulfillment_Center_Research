#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


adj_counties_df = pd.read_csv('../data/csv/adjacent_counties_5%.csv')
center_df = pd.read_csv('../data/csv/fulfillment_centers.csv')
population_df = pd.read_csv('../data/csv/county_population.csv')
commuting_df = pd.read_csv('../data/csv/commuting_flows.csv')


# Configuring data
just_adj_counties_df = adj_counties_df[['State', 'County']]

all_counties_df = population_df[['STNAME', 'CTYNAME']]
all_counties_df.columns = ['State', 'County']
all_counties_df = all_counties_df.append(just_adj_counties_df)

# all counties that are not directly adjacent (in adjacent_counties.csv)
init_non_adj_counties_df = all_counties_df.drop_duplicates(subset=['State', 'County'], keep=False)

# Join center data with commuting data
# work counties = fulfillment center is in work county
# residence counties = fulfillment center is in residence county
work_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['work_county','work_state'])
residence_counties_df = pd.merge(center_df, commuting_df, how='inner', left_on=['County','State'], right_on=['residence_county','residence_state'])

# Joining center/commuting data with population data
work_counties_df = pd.merge(work_counties_df, population_df, how='inner', left_on=['work_county','work_state'], right_on=['CTYNAME','STNAME'])
residence_counties_df = pd.merge(residence_counties_df, population_df, how='inner', left_on=['residence_county','residence_state'], right_on=['CTYNAME','STNAME'])

# Join initial non adjacent counties with center data -> opposite of name (destination or source -> opposite of fulfillment center)
#work_counties_df = pd.merge(work_counties_df, init_non_adj_counties_df, how='inner', left_on=['residence_county','residence_state'], right_on=['County','State'])
reisdence_counties_df = pd.merge(residence_counties_df, init_non_adj_counties_df, how='inner', left_on=['work_county','work_state'], right_on=['County','State'])

#print(residence_counties_df)

non_adjacent_counties = set()
only_counties = set()


for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] < .00001:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        if (row['work_county'],row['work_state']) not in only_counties:
            only_counties.add((row['work_county'],row['work_state']))
            non_adjacent_counties.add((row['work_county'],row['work_state'],str(FIPS),row['Year Opened']))

#print(non_adjacent_counties)

print(len(non_adjacent_counties))
print(len(only_counties))


with open('../data/csv/non_adjacent_counties_5%.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['County','State','FIPS','Year Opened'])
    for row in non_adjacent_counties:
        csv_out.writerow(row)


'''
adjacent_counties= set()
only_counties = set()

for i, row in work_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .01:
        FIPS = format(row['residence_state_FIPS'], '02d')+format(row['residence_county_FIPS'], '03d')
        if (row['residence_county'],row['residence_state']) not in only_counties:
            only_counties.add((row['residence_county'],row['residence_state']))
            adjacent_counties.add((row['residence_county'],row['residence_state'],str(FIPS),row['Year Opened']))
        
for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .01:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        if (row['work_county'],row['work_state']) not in only_counties:
            only_counties.add((row['work_county'],row['work_state']))
            adjacent_counties.add((row['work_county'],row['work_state'],str(FIPS),row['Year Opened']))

print(len(adjacent_counties))
print(len(only_counties))
#print(adjacent_counties)

'''
