# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 13:24:26 2018

@author: danielmaxwell
"""

import sqlite3

def db_connect():
    sqlite_file = 'C:/informatics/gapminder.db'
    
    conn = sqlite3.connect(sqlite_file)
     
    return(conn)
    
def main():
    print('In the main() function.')
    
    conn = db_connect()
    
    conn.close()
  
   
if __name__ == "__main__": 
    main()