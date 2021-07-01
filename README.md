# NBA

## Setup ODBC for module pyodbc (unixODBC)
1. Down load the driver for your specific database
1. Open terminal
2. Run `odbcinst -j`
You should see something like
`
unixODBC 2.3.9
DRIVERS............: /etc/odbcinst.ini
SYSTEM DATA SOURCES: /etc/odbc.ini
FILE DATA SOURCES..: /etc/ODBCDataSources
USER DATA SOURCES..: /Users/oliviabrzozowski/.odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
`
3. Open file to the right of `DRIVERS:`
4. Enter your driver information something similiar to
`
[ODBC Driver 17 for SQL Server]
Description=Microsoft ODBC Driver 17 for SQL Server
Driver=/usr/local/lib/libmsodbcsql.17.dylib
UsageCount=1
`
5. In your python code, use the string within the brackets for the 'Driver='

## Fixing Flask issue with 'address already in use'
Killing the Flask process does not stop the port it's using
The Fix:
> ps -fA | grep python
>
> kill -9 `<pid>`

