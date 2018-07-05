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


if __name__ == "__main__":
    
    df = pd.read_csv('c:/informatics/gapminder.csv')
    
