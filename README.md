# NBA

## Git
1. 

## Python
1. Classes
    -SOC (separation of concerns)
2. Functions
3. Data Types
4. Variables
5. Flow control
    -looping
6. Flask
7. Api

## Relational Database
1. sql language
2. mysql
3. first, second, third normal form
4. dbeaver 
    -client tool used on a mac
5. ODBC
    -we used pyodbc module for the odbc implentation
6. primary and foreign keys
7. CRUD
    -Create, Read, Update, Delete

## Restful API
1. JSON
2. Media Type
3. URL (Uniform Resource Locator)
    -the path to a unique resource on the Web
    -breakdown https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL

## Http (hypertext transmission protocol)
1. http vs https 
    -http is insecure
    -https is secured by a certificate on a server that tells clients that they are talking to the domain they intended to talk to 
2. PKI (public key infrastructure)
    -public/private key
    -used to make https secure
3. http server
4. HTTP methods
    -GET, POST, PUT, DELETE

## Chrome debugger
## Network Concepts
1. localhost and 127.0.0.1
    - /etc/hosts file
2. DNS (domain name system)
    - maps domain name to an IP address
    - domain name 
        -
3. port numbers 
    -as an example, think of IP address as an apartment building street address, and port number as a
    specific apartment number

## Setup ODBC for module pyodbc (unixODBC)
1. Download the driver for your specific database
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

## Pyodbc
This line fixed issue with returning dictionary generated using __dict__ where strings were returned with the unicode replacement character
> self.cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

## Fixing Flask issue with 'address already in use'
Killing the Flask process does not stop the port it's using.
The Fix:
> ps -fA | grep python
>
> kill -9 `<pid>`

## HTML
1. Javascript basics 
    https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
    https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
2. DOM basics 
    https://www.digitalocean.com/community/tutorial_series/understanding-the-dom-document-object-model

## Angular
https://angular.io/docs
Things we've learned about:
1. Components
2. TypeScript(ts)
    -Interfaces
        -user defined data type that describes data to create a data contract
        -data contract
            -a formal agreement that describes data to be exchanged 
        -strong typing
3. Databinding
    -ngModel
    -NgModule
4. Structure
    -HTML
    -CSS
    -TypeScript (ts)
5. app.module.ts
6. HttpClient service class
    -https://angular.io/guide/http
    -this is what we used to call our Restful api's
7. Angular Client 
    -ng 
    -scaffold new application
        -ng new 
    -build application
        -ng build
    -run application
        -ng serve

## Possible ideas for site functionality 
1. Search player stats based on player name or team
2. Try to find how many 3 pointers a team has to shoot to get to expected total points x
3. How many guards are on a team where the team shoots above average the 3 point percentage? Plot the teams 3 point percentage to the number of guards