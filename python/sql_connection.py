#!/usr/bin/env python3

import pyodbc

class SqlConnection:
    def __init__(self):
        # here we are telling python what to connect to (our SQL Server)
        driver = "Driver={MySQL ODBC 8.0 ANSI Driver};"
        cnstring = f'{driver}Server=localhost;Database=NBA;UID=root;PWD=LearnSql123;CHARSET=UTF8' 

        #connect to server
        self.cnxn = pyodbc.connect(cnstring)
        
        self.cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')
        self.cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding='utf-8')
        self.cnxn.setencoding(encoding='utf-8')

    #----------
    #return connection variable
    def connection(self):
        return self.cnxn

    #----------
    #return cursor from connection
    def cursor(self):
        return self.cnxn.cursor()