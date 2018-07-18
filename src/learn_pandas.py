# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
https://jakevdp.github.io/PythonDataScienceHandbook/04.01-simple-line-plots.html

"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('seaborn-whitegrid')

ghog_day = eval(input('Please enter the number of groundhog days: '))

for idx in range(1, ghog_day + 1):
    print("When will this day end? I've already lived it", idx, "times!")
    
df  = pd.read_csv('c:/informatics/gapminder.csv', index_col = 0)

df_gap = df.loc['United States']
plt.plot(df_gap[['year']], df_gap[['lifeExp']], color = 'blue')

df_gap = df.loc['France']
plt.plot(df_gap[['year']], df_gap[['lifeExp']], color = 'red')

df_gap = df.loc['Brazil']
plt.plot(df_gap[['year']], df_gap[['lifeExp']], color = 'green')

print(df_gap)

x = np.linspace(0, 10, 1000)
plt.plot(x, np.sin(x - 0), color='blue') 
plt.plot(x, np.sin(x - 1), color='g')

if __name__ == "__main__":
    
    df = pd.read_csv('c:/informatics/gapminder.csv')
    