#!/usr/bin/python3

import csv
import pandas as pd

for year in range(1994, 2017):
    df = pd.read_csv('../data/csv/unemployment_files/'+str(year)+'.csv')
    print(year)
    with open('../data/csv/unemployment_files/'+str(year)+'_unemp.csv', 'w') as out_file:
        csv_out = csv.writer(out_file)
        csv_out.writerow(['FIPS', 'County/State', 'Year', 'Labor_Force', 'Employed', 'Unemployed', 'Unemployment_Rate'])
        for i, row in df.iterrows():
            FIPS = format(row['State FIPS'], '02d')+format(row['County FIPS'], '03d')
            output = [FIPS, row['County/State'], row['Year'], row['Labor Force'], row['Employed'], row['Unemployed'], row['Unemployment_Rate']]
            csv_out.writerow(output)
