# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

clean_file = open('fips_file_clean.txt','w')

for line in open('fips_file.txt'):
    if (line.find('County') != -1):
        new_line = line.replace('County','')
    
    if (line.find('Parish') != -1):
        new_line = line.replace('Parish','')
 
    if (line.find('Municipio') != -1):
        new_line = line.replace('Municipio','')

    if (line.find('Borough') != -1):
        new_line = line.replace('Borough','')

    if (line.find('Census Area') != -1):
        new_line = line.replace('Census Area','')

    if (line.find('Municipality') != -1):
        new_line = line.replace('Municipality','')

    if (line.find('city') != -1):
        new_line = line.replace('city','')
 
    clean_file.write(new_line)
       
    print(new_line)

clean_file.close()
  
