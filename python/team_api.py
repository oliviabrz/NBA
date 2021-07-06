#!/usr/bin/env python3

import json
from nba_db_record import TeamRecord
from flask import Flask, request, jsonify
import requests
import pyodbc
from json import JSONEncoder


app = Flask(__name__)

@app.route('/api/nba/team', methods=['GET'])
def get_team_by_abbreviation():
    #get query string parameter from the Flask request object
    abbreviation = request.args.get('abbreviation')

    #create team record instance 
    team_rec = TeamRecord()

    #assign the abbreviation field with the value of the query string parameter
    team_rec.Abbreviation = abbreviation

    #get sql connection
    cn = SqlConnection()

    #populate record instance with database values
    team_rec.get_team_rec_by_abbreviation(cn)

    #convert record instance to a dictionary 
    json_rec = team_rec.__dict__

    #create a Flask response object and set the mime-type to application/json
    response = jsonify(json_rec)

    #allow CORS (Cross Origin Resource Sharing)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route('/api/nba/team/list', methods=['GET'])
def get_team_list():

    team_rec = TeamRecord()

    cn = SqlConnection()

    #get list of TeamRecord instances
    team_list = team_rec.get_team_list(cn)

    #list to hold TeamRecord dictionaries 
    team_json_list = []

    #iterate over each TeamRecord instance, convert it to a dictionary and
    #add to dictionary list
    for rec in team_list:
        team_json_list.append(rec.__dict__)
    
    response = jsonify(team_json_list)
    
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response

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

if __name__ == '__main__':
    app.run(port=5000)