#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')

with open('../data/csv/year_and_county_data.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    counties_df.drop_duplicates(subset=['FIPS'])        
    counties_df.to_csv('../data/csv/adjacent_counties.csv')
        
