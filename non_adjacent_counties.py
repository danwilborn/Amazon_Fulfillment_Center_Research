#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


adjacent_counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')
all_counties_df = pd.read_csv('../data/csv/Unemployment_Rate.csv')

non_adjacent_counties= set()
only_counties = set()

for i, row in work_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .01:
        FIPS = format(row['residence_state_FIPS'], '02d')+format(row['residence_county_FIPS'], '03d')
        adjacent_counties.add((row['residence_county'],row['residence_state'],str(FIPS),row['Year Opened']))
        only_counties.add((row['residence_county'],row['residence_state']))

for i, row in residence_counties_df.iterrows():
    if row['Number']/row['POPESTIMATE2010'] > .01:
        FIPS = format(row['work_state_FIPS'], '02d')+format(row['work_county_FIPS'], '03d')
        adjacent_counties.add((row['work_county'],row['work_state'],str(FIPS),row['Year Opened']))
        only_counties.add((row['work_county'],row['work_state']))

print(len(adjacent_counties))
print(len(only_counties))
#print(adjacent_counties)

with open('../data/csv/adjacent_counties.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['County','State','FIPS','Year Opened'])
    for row in adjacent_counties:
        csv_out.writerow(row)

