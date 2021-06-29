#!/usr/bin/env python3

import json
from nba_db_record import PlayerRecord
from flask import Flask, request, jsonify
import requests
import pyodbc
from json import JSONEncoder


app = Flask(__name__)

@app.route('/api/nba/player', methods=['GET'])
def get_player_by_name():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')

    player_rec = PlayerRecord()
    player_rec.FirstName = first_name
    player_rec.LastName = last_name

    cn = SqlConnection()

    player_rec.get_player_rec_by_name(cn)
    json_rec = player_rec.__dict__
    #json_rec = json.dumps(player_rec, cls=PlayerEncoder) 
    #print(json_rec)
    
    return jsonify(json_rec)

class SqlConnection:
    def __init__(self):
        # here we are telling python what to connect to (our SQL Server)
        driver = "Driver={MySQL ODBC 8.0 ANSI Driver};"
        cnstring = f'{driver}Server=localhost;Database=NBA;UID=root;PWD=LearnSql123;CHARSET=UTF8' 

        #connect to server
        self.cnxn = pyodbc.connect(cnstring)

    #----------
    #return connection variable
    def connection(self):
        return self.cnxn

    #----------
    #return cursor from connection
    def cursor(self):
        return self.cnxn.cursor()    

if __name__ == '__main__':
    app.run()