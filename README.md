# About The Process
This README documents my learning process to obtain the skills required for a career in Software Development. It began with successfully completing Coursera's [**Google IT Automation with Python**](https://www.coursera.org/professional-certificates/google-it-automation?utm_source=gg&utm_medium=sem&utm_campaign=11-GoogleITwithPython-US&utm_content=11-GoogleITwithPython-US&campaignid=8986236679&adgroupid=119480419197&device=c&keyword=&matchtype=b&network=g&devicemodel=&adpostion=&creativeid=506915205324&hide_mobile_promo&gclid=CjwKCAjwpMOIBhBAEiwAy5M6YC58jIqHwDL-Nn4oPzbaQXaImQMMyW30OKlaNC2EtrXvSsRVKHdxehoCvroQAvD_BwE) course and receiving a certificate of completion. After completion of the course, my mentor felt it was essential to learn about Full Stack Development. We decided to build an Angular web application called [**NBA**](https://www.olib.cloud/) to display various NBA statistics. The application is built using Angular for the front end, Python Flask scripts for the Api's, and MySQL for the database. The site itself is hosted in Azure Cloud on a Ubuntu Linux VM. 

This entire process, from start to finish, took me approximately 8 months. I will be honest, this journey was quite challenging because my professional background in higher education/college athletics did not come with the hard skills necessary in IT. My motivation to change careers came during the pandemic when I realized the IT world would allow me to explore different industries. My mentor, who has 30 years of experience as a Software Engineer, guided me through the entire process. Looking back, what got me through was dedicating as much time as possible 7 days a week and keeping an open mind, despite the many challenges I faced. 

The content below highlights the various technologies and concepts I learned.

## Python
- Data Types
    -string, integer, float, list, set, tuple, dictionary, bool
- Variables
    - a user declared name that points to a memory location containing data of some data type 
- Loops
    - for loop (iterate over a range)
    - while loop (iterate while something is true)
- Expressions 
    - Expressions are made of operators and operands. An expression is like 2 + 3 
- Operators 
    - the symbols which tells the Python interpreter to do some mathematical or logical operation 
- Conditionals
    -if/elif/else statements 
- Collections
    - list (mutable, ordered, allows duplicates)
    - tuple (immutable, ordered, allow duplicates)
    - sets (mutable, unordered, no duplicates)
    - dictionary(mutable, key/value)
- Functions
    - A block of code that runs only when it's called
    - Can accept parameters (variables) 
    - Can return data 
    - Makes code more modular by separating it into smaller, more specialized tasks 
- Classes
    - Bundles data and functionality together 
    - A class definition defines a new type of object, allowing new instances of that type to be made (see car example)
    - Instances of a class represent:
        - a location in **allocated memory** 
        - Properties of the class exist in memory and have an **initial state**
        - Example: An instance of class Car exists in memory and its property, current_speed == 0mph (initial state)
        - The **dunder** __init__ is a specialized function (constructor) that gets called when a new instance is being created and allows   you to specify properties and their initial values 
- Interpreter
    - A program that converts python scripts to an executable program that runs on a specific CPU/operating system (macOS, Linux, Windows)
- Resources
    - https://www.w3schools.com/python/default.asp

## Operating System
- Windows, MacOS, Linux
- Reading and writing files
- CSV files
- Regular expressions
    - https://help.relativity.com/9.3/Content/Relativity/Regular_expressions/Regular_expression_metacharacters.htm
    - https://regex101.com/
- Unit tests
- Bash

## Git 
- Version Control System
- Software that tracks changes in any set of files so you have a record of what's been done
    - Can also revert to specific versions if you ever need to 
- Used for collaborating and coordinating work among programmers 
- 3 main components of a Git project:
    - Repository
        - the .git/folder inside a project
        - if .git/folder is deleted, your project's history will be deleted 
    - Working tree
        - where files are modified 
    - Index
        - staging area where commits are prepared by comparing files in the working tree to the files in the repo
- Basic Git Workflow:
    - Modify file in the working tree
    - Stage the changes you want to include in the next commit 
        - `git add`
    - Commit changes to the repo 
        - `git commit -m` 
- https://training.github.com/downloads/github-git-cheat-sheet.pdf
- file:///Users/oliviabrzozowski/Downloads/SWTM-2088_Atlassian-Git-Cheatsheet.pdf
- GitHub is a widely used Git repository hosting service 
- Remote vs Local
    - Local repository resides on the computer of the worker
    - Remote repositories are hosted on a server, such as GitHub
## Concepts
- SOC (separation of concerns)
    - the process of separating unrelated functionality from each other 
    - achieved through functions, classes, modules, etc.
    - makes code more understandable and maintainable 
- Client/Server
    - A model where clients make requests to a server which fulfills the request
- ### Network Concepts
    - localhost and 127.0.0.1
        - a hostname that refers to the current computer at the network level
        - defined in `/etc/hosts` file
    - DNS/Domain Name (domain name system)
        - Domain name
            - a user friendly name for an IP Address
            - example: `olib.cloud`
        - DNS maps domain name to an IP address 
            - example: `nslookup olib.cloud`
    - IP Address
        - a unique **Internet Protocol** address that identifies a device on the internet or a local network
    - Port Number 
        - Identifies a particular application or service on a system
        - Example: think of an IP address as an apartment building's street address, and port number as a
        specific apartment number

## Compute Resources
- CPU
    - Central Processing Unit 
    - The electronic circuitry that executes instructions comprising a computer program
    - The CPU performs basic arithmetic, logic, controlling, and input/output operations specified by the instructions in the program
    - The register within a CPU is what determines the size of the CPU (32/64 bit)
        - https://techterms.com/definition/register
- Memory
    - Random Access Memory (RAM) is the high speed, non-persistent storage part of the computer that stores various parts of a running program
    - Non-persistent means when the computer shuts down, everything in memory is lost
    - This is where instructions, functions, variables, instances of classes, etc. are stored 
- Hard Drive
    - The part of a computer where persistent data is stored so that it can be retrieved after the computer restarts 
    - Persistent means when the computer shuts down, the data still exists and can retrieved when the program runs
    - Significantly slower than RAM 
    - Examples are databasing systems (SQL servers)

## Binary
- Bits/Bytes
- Base-2
- https://www.mathsisfun.com/numbers/bases.html

## ODBC/DBMS
- DBMS (database management system)
    - A server or software system that enables users to define, create, maintain and control access to data in a database
    - MySQL, Microsoft SQL Server, MariaDB, PostgreSQL
- ODBC (Open Database Connectivity)
    - A specification that describes or defines a generic way of accessing DBMS's
    - It is meant to be independent of any specific database or operating system
    - A ODBC Driver is what implements the specific way of accessing DBMS's
        - For your program to work with a specific DBMS, you will use a driver specific to the DBMS to implement your requests
    ### Relational Database
    - A type of database that stores and provides access to data points that are related to one another
    - SQL (Structered Query Language)
        - The standard language for relational DBMS's 
    - Primary key
        - Uniquely identifies each record in a table
    - Foreign key
        - a database key that is used to link two tables together
    - Normal forms
        - First normal form
            - The relation cannot contain any repeating groups
        - Second normal form
            - Every field in the relation must be functionally dependent upon the entire primary key
        - Third normal form
            - The relation cannot contain any transitive dependencies
    - CRUD
        - Create, Read, Update, Delete
        - The 4 types of operations that can be performed on a database 
## HTTP (hypertext transmission protocol)
- HTTP is a protocol which allows the fetching of resources on the Internet 
    - https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview
- HTTP vs HTTPS
    -HTTP is insecure
    -https is secured by a certificate on a server that tells clients that they are talking to the domain they intended to talk to 
        - PKI (public key infrastructure)
            - public/private key
            - used to make https secure
            - https://www.sslshopper.com/public-key-infrastructure-pki-overview.html
- URL (Uniform Resource Locater)
    - The path to a unique resource on the Web
    - https://blog.hubspot.com/marketing/parts-url
    - https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_is_a_URL 
- HTTP server
    - Computer software that accepts requests via HTTP
    - All web applications/api's require a http server
    - Examples: Apache Tomcat, IIS, node.js, python flask/waitress
- Most common HTTP methods
    - GET, POST, PUT, DELETE
- Headers
    - Area in an http request/response where key/value pairs of information about the request/response reside
        - Example: **User-Agent:** Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:50.0) Gecko/20100101 Firefox/50.0

## Web API
- API (Application Programming Interface)
    - An interface which has a set of functions that allow programmers to access specific features or data of an application, operating     system or other services 
- Web API
    - A set of functions that are called or requested using HTTP 
    - Requests are received by an HTTP server and passed to a programmer defined service running on a computer that executes the functions
    - example: https://www.balldontlie.io/#getting-started
- JSON (JavaScript Object Notation)
    - A text based data format used to send/receive lightweight messages between computers
    - Uses key/value pairs to structure data
- Media Type
    - Formally known as MIME type (Multipurpose Internet Mail Extensions)
    - A standard way of classifying file types on the Internet according to their nature and format
## HTML
- HTML (Hypertext Markup Language)
- The set of markup symbols or codes inserted into a file intended for display on the Internet
- The markup tells web browsers how to display a web page's words and images
- JavaScript
    - A programming language that can add interactivity to a website 
    - https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics
    - https://developer.mozilla.org/en-US/docs/Web/JavaScript/A_re-introduction_to_JavaScript
- DOM (Document Object Model)
    - When a web page is loaded, the browser creates a **D**ocument **O**bject **M**odel of the page
        - The HTML DOM model is constructed as a tree of objects and exposes an api of functions and properties that can be easily accessed programatically
            -  https://www.w3schools.com/js/js_htmldom.asp
        - JavaScript can modify the DOM in realtime using the DOM api to give a much more interactive user experience 
            - https://www.digitalocean.com/community/tutorial_series/understanding-the-dom-document-object-model
    - You can visualize this using `F12` to bring up the browser debugger
        - Go to `Console`, then type in `document.` and you should see the DOM api functions pop up
## Angular
- https://angular.io/docs
- A development platform, built on TypeScript, used for building single page web applications 
- SPA (Single-Page Application)
    - A web application that loads most resources (HTML+CSS+Scripts) once when the site is first pulled up
    - Only data is transmitted back and forth
    - This is all made possible by the DOM
- Components
    - The main building block for Angular applications
    - Each component consists of:
        - An HTML template that declares what renders on the page
        - A Typescript class that defines behavior
        - A CSS selector that defines how the component is used in a template
        - Optionally, CSS styles applied to the template
- TypeScript(ts)
    - an open-source language which builds on JavaScript
- Interfaces
    -user defined data type that describes data to create a data contract
    -data contract
        -a formal agreement that describes data to be exchanged 
    -strong typing
- Databinding
    -ngModel
    -NgModule
- Structure
    -HTML
    -CSS
    -TypeScript (ts)
- app.module.ts
- HttpClient service class
    -https://angular.io/guide/http
    -this is what we used to call our Restful api's
- Angular Client (ng)
    -https://angular.io/cli
    -scaffold new application
        -ng new 
    -build application
        -ng build
    -run application
        -ng serve
- MaterialTable (MatTable)
    -https://stackblitz.com/edit/angular-kj6g7p?file=src%2Fapp%2Fcomponents-table%2Fcomponents-table.component.html

## Possible ideas for site functionality 
- Search player stats based on player name or team
- Try to find how many 3 pointers a team has to shoot to get to expected total points x
- How many guards are on a team where the team shoots above average the 3 point percentage? Plot the teams 3 point percentage to the number of guards

## SSL Certification
In order to run our Angular NBA app on our azure VM, we had to secure it with an SSL certificate. The following is the process we used to get our certificate:

1. Purchased `olib.cloud` domain from GoDaddy.com, a domain registrar
2. Purchased SSL certificate from RapidSSLOnline.com, a Certificate Authority (CA)
3. Create Certificate Signing Request (CSR) as follows:
    ### Creating CSR
    - generate CSR here: https://www.digicert.com/easy-csr/openssl.htm
    - this generates the openSSL command to generate the CSR and private key
    > openssl req -new -newkey rsa:2048 -nodes -out junk.csr -keyout junk.key -subj "/C=US/ST=KS/
    > L=your city/O=junk/CN=junk"
    - copy generated CSR and paste into RapidSSL CSR screen
    ### Domain Control Verification (DCV)
    See: https://docs.digicert.com/manage-certificates/demonstrate-control-over-domains-pending-certificate-order/use-http-practical-demonstration-validation-method-verify-domain-control/
    Before a certificate can be issued to a domain, you must prove to the CA that you control the domain.
    There are numerous methods for DCV such as email and HTTP Practical Demonstration.
    We chose HTTP Practical Demonstration. This process is as follows:
        - In GoDaddy, add an `A` record that points to the IP Address of our VM
            - To verify domain IP, run `nslookup olib.cloud` and verify the IP address is correct
        - In RapidSSL, choose HTTP file verification method
            - You will be given a .txt file to download 
            - You will be given the verification URL to pull the file from your VM
        - On your VM, do the following:
            - Copy .txt file to a local directory given in the verification URL 
            - Run `sudo python3 -m  http.server 80` from the root of the path in the verification URL
            - Verify you can pull the .txt file using the verification URL

## Useful Tools
- Chrome debugger
- VisualStudio Code
- DBeaver
- Postman

## Azure
## Linux
### Setup Python Flask Api as a service 
https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267
sudo nano /etc/systemd/system/api.service
copy/paste contents of systemd.txt
sudo systemctl daemon-reload
sudo systemctl enable api.service
sudo systemctl start api.service
sudo systemctl status api.service

~/NBA/run/python
/var/www/olib.cloud/html/
/etc/nginx/sites-available
www_olib_cloud.key
www_olib_cloud.pem

### NGINX
https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-20-04
https://dev.to/thetrebelcc/how-to-run-a-flask-app-over-https-using-waitress-and-nginx-2020-235c
https://medium.com/@anasecn/how-to-serve-an-angular-app-with-node-js-api-on-a-nginx-server-ca59de51850
sudo mkdir -p /var/www/olib.cloud/html
sudo chown -R $USER:$USER /var/www/olib.cloud/html
sudo chmod -R 755 /var/www/olib.cloud
nano /var/www/olib.cloud/html/index.html
sudo nano /etc/nginx/sites-available/olib.cloud
sudo ln -s /etc/nginx/sites-available/olib.cloud /etc/nginx/sites-enabled/
sudo nano /etc/nginx/nginx.conf
sudo systemctl restart nginx

## NBA
- Flask
- Api
sudo -H pip install Flask
sudo -H pip install pyodbc
sudo -H pip install waitress
- mysql
        -https://phoenixnap.com/kb/install-mysql-ubuntu-20-04
- dbeaver 
        -client tool used on a mac
    ### Setup ODBC Driver for module pyodbc (unixODBC)
        - pyodbc is the python implentation of the ODBC specification
        1. Download the driver for your specific database
        2. Open terminal
        3. Run `odbcinst -j`
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
        4. Open file to the right of `DRIVERS:`
        5. Enter your driver information something similiar to
        `
        [ODBC Driver 17 for SQL Server]
        Description=Microsoft ODBC Driver 17 for SQL Server
        Driver=/usr/local/lib/libmsodbcsql.17.dylib
        UsageCount=1
        `
        6. In your python code, use the string within the brackets for the 'Driver='
        ### Pyodbc
        This line fixed issue with returning dictionary generated using __dict__ where strings were returned with the unicode replacement character
        > self.cnxn.setdecoding(pyodbc.SQL_CHAR, encoding='utf-8')

    ## Fixing Flask issue with 'address already in use'
    Killing the Flask process does not stop the port it's using.
    The Fix:
    > ps -fA | grep python
    >
    > kill -9 `<pid>`




