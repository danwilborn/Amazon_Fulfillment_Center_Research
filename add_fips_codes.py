#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')
non_adj_counties_df = pd.read_csv('../data/csv/non_adjacent_counties.csv')
fips_codes_df = pd.read_csv('../data/csv/national_county.csv')

# Join Adjacent Counties with County Data
joined_counties_df = pd.merge(counties_df, fips_codes_df, how='inner', left_on=['County','State'], right_on=['County','State'])
joined_non_adj_counties_df = pd.merge(non_adj_counties_df, fips_codes_df, how='inner', left_on=['County','State'], right_on=['County','State'])

print(fips_codes__df)

