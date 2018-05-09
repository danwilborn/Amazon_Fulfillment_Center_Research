#!/usr/bin/python3

import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


counties_df = pd.read_csv('../data/csv/adjacent_counties.csv')
non_adj_counties_df = pd.read_csv('../data/csv/non_adjacent_counties.csv')
CPI_df = pd.read_csv('../data/csv/CPI_base_year_2000.csv')

with open('../data/csv/year_and_county_data.csv','w') as out_file:
    csv_out = csv.writer(out_file)
    csv_out.writerow(['FIPS', 'State', 'County', 'Year_Opened', 'Year', 'Time_Dummy', 'Near_Dummy', 'Time*Near', 'Annual_Wage', 'CPI', 'Real_Wage', 'Unemployment_Rate', 'Log(Real_Wage)', 'Log(Unemployment)'])

    for Year in range(1994,2016):
        wage_df = pd.read_csv('../data/csv/wage_files/'+str(Year)+'.annual.singlefile.csv')
        wage_df = wage_df[['area_fips', 'industry_code', 'own_code', 'avg_annual_pay']]
        wage_df = wage_df[wage_df['industry_code'] == '10']
        wage_df = wage_df[wage_df['own_code'] == 0]

        wage_and_counties_df = pd.merge(counties_df, wage_df, how='inner', left_on='FIPS', right_on="area_fips")
      
 
        empl_df = pd.read_csv('../data/csv/unemployment_files/'+str(Year)+'_unemp.csv')
        #empl_df = empl_df[str(empl_df['Unemployment_Rate']) != 'N.A.']
        

        all_data_counties_df = pd.merge(wage_and_counties_df, empl_df, how='inner', left_on='FIPS', right_on='FIPS')        

        CPI_year_df = CPI_df[CPI_df['DATE'] == str(Year)+'-01-01']
        CPI = CPI_year_df.iloc[0]['CPI']

        for i, row in all_data_counties_df.iterrows():
            FIPS = row['FIPS']
            State = row['State']
            County = row['County']
            Year_Opened = row['Year Opened']
            Near_Dummy = 1
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Wage = row['avg_annual_pay']
            Real_Wage = float((Wage*100)/CPI)
            if Real_Wage == 0:
                break
            Unemployment_Rate = float(row['Unemployment_Rate'])
            time_near_interaction = Near_Dummy*Time_Dummy
            log_wage = float(np.log(Real_Wage))
            log_unempl = np.log(Unemployment_Rate)
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, time_near_interaction, Wage, CPI, Real_Wage, Unemployment_Rate, log_wage, log_unempl])                                     

        wage_and_non_adj_counties_df = pd.merge(non_adj_counties_df, wage_df, how='inner', left_on='FIPS', right_on="area_fips")
        #wage_and_non_adj_counties_df.drop_duplicates(subset=['FIPS', 'State', 'County', 'avg_annual_pay'], keep='first')        

        all_data_non_adj_counties_df = pd.merge(wage_and_non_adj_counties_df, empl_df, how='inner', left_on='FIPS', right_on='FIPS')

        for i, row in all_data_non_adj_counties_df.iterrows():
            FIPS = row['FIPS']
            State = row['State']
            County = row['County']
            Year_Opened = row['Year Opened']
            Near_Dummy = 0
            if Year > Year_Opened:
                Time_Dummy = 1
            else:
                Time_Dummy = 0
            Wage = row['avg_annual_pay']
            Real_Wage = float((Wage*100)/CPI)
            if Real_Wage == 0:
                break
            Unemployment_Rate = float(row['Unemployment_Rate'])
            time_near_interaction = Near_Dummy*Time_Dummy
            log_wage = float(np.log(Real_Wage))
            log_unempl = np.log(Unemployment_Rate)
            csv_out.writerow([FIPS, State, County, Year_Opened, Year, Time_Dummy, Near_Dummy, time_near_interaction, Wage, CPI, Real_Wage, Unemployment_Rate, log_wage, log_unempl])                                     
           
    
