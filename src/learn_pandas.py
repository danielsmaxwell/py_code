# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

ghog_day = eval(input('Please enter the number of groundhog days: '))

for idx in range(1, ghog_day + 1):
    print("When will this day end? I've already lived it", idx, "times!")
    
df = pd.read_csv('c:/informatics/gapminder.csv', index_col = 0)

df_gap = df.loc['United States']

df_gap = df.loc['France']

df_gap = df.loc['Brazil']

print(df_gap)


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
    


idx = 5
print("When will this day end? I've already lived it ", idx, " times!")
