#!/usr/bin/python
# -*- encoding:UTF-8-*-
import pandas as pd
import numpy as np

# data = pd.read_csv('air.csv')
# print(data.head())
# print('\n Data Types:')
# print(data.dtypes)

dateparse = lambda dates:pd.datetime.strptime(dates,'%Y-%m')
data = pd.read_csv('air.csv',parse_dates= 'Month' ,index_col='Month',date_parser=dateparse)
print(data.head())