# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:06:36 2019

@author: danielmaxwell
"""

import sqlite3
from sqlite3 import Error
from pathlib import Path

def create_connection(db_file):
    """ Create a connection to the SQLite database specified by the db_file
        argument.  The function checks if the file exists.  If the file does
        not exist, it asks the user if they want to create a new one.  The 
        sqlite3 connect() function automatically creates a new database if the
        requested database does not exist.  Hence, the need for this prompt.
         
        :param db_file: database file
        :return: Connection object or None
    """
    db_path = Path(db_file)
   
    if not(db_path.is_file()):
        yn = input("Database does not exist - Create one (Y/N): ")
    
    if (yn.upper() == 'N'):
        return None
    
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None


conn = sqlite3.connect("c:/informatics/test.db")

cur  = conn.cursor()

cur.execute("select * from sqlite_master")

rows = cur.fetchall()

for row in rows:
    print(row)

print(cur.fetchone())

conn.close()
