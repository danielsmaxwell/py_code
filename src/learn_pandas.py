# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv('c:/informatics/gapminder.csv')

print(type(df))

print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())

country_df = df['country']
print(country_df.tail())

subset = df[['country','continent','year']]

print(df.tail(n = 1))
print(df.loc[55])
print(df.loc[[0, 99, 999]])
 
r = list(range(3))
print(r) 

if __name__ == "__main__":
    
    df = pd.read_csv('c:/informatics/gapminder.csv')
    
