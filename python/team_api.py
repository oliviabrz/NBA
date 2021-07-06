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
    abbreviation = request.args.get('abbreviation')

    team_rec = TeamRecord()
    team_rec.Abbreviation = abbreviation

    cn = SqlConnection()

    team_rec.get_team_rec_by_abbreviation(cn)
    json_rec = team_rec.__dict__
    response = jsonify(json_rec)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route('/api/nba/team/list', methods=['GET'])
def get_team_list():

    team_rec = TeamRecord()

    cn = SqlConnection()

    team_list = team_rec.get_team_list(cn)

    #iterate over each player rec and convert into dictionary 
    team_json_list = []
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