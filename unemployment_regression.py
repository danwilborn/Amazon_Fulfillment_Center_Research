#!/usr/bin/python2.7

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt


df = pd.read_csv('../data/csv/year_and_county_data.csv')
#X = df[['Near_Dummy', 'Time_Dummy', 'Time*Near']]
X = df[['Near_Dummy', 'Time*Near']]
y = df['Unemployment_Rate']

X = sm.add_constant(X)
est = sm.OLS(y,X).fit()

print est.summary()


y = df['Log(Unemployment)']

X = sm.add_constant(X)
est = sm.OLS(y,X).fit()

print est.summary()
