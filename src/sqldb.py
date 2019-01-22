# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:06:36 2019

@author: danielmaxwell
"""

import sqlite3
from sqlite3 import Error
from pathlib import Path

def create_connection(db_file, db_create = False):
    """ Create a connection to the SQLite database specified by the db_file
        argument.  The function checks if the file exists.  If the file does
        not exist and the db_create flag is True, the function creates a new 
        SQLite database.  Otherwise, the function prints an error message and
        returns None.  The sqlite3 connect() function automatically creates 
        a new database if the requested database does not exist.  Hence, the 
        need for this function.
         
        :param db_file:   the name of the sqlite database file to be opened, 
                          with fully qualified path.
        :param db_create: flag to create new database when one the one to 
                          be opened doesn't exist - acceptable values are 
                          boolean True or False.  The default is False.
        :return: Connection object or None
    """
    db_path = Path(db_file)
   
    if not(db_path.is_file()):
        if (db_create == False):
            print("Error: the database file does not exist - unable to open!")
            return None
        
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
        
    return None

# Driver to test the functions in this library.
    
if __name__ == '__main__':
    conn = create_connection('c:/informatics/test.db')
    
    cur = conn.cursor()
    cur.execute("select * from person")

    rows = cur.fetchall()       # Or, use cur.fetchone() to fetch single row.
    for row in rows:
        print(row)
        
    conn.close()
    
    