#!/usr/bin/env python3

import json
from nba_db_record import PlayerRecord
from flask import Flask, request, jsonify
import requests
import pyodbc
from json import JSONEncoder
from sql_connection import SqlConnection


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
    response = jsonify(json_rec)
    response.headers.add("Access-Control-Allow-Origin", "*")
    
    return response

@app.route('/api/nba/player/list', methods=['GET'])
def get_player_list():

    player_rec = PlayerRecord()

    cn = SqlConnection()

    player_list = player_rec.get_player_list(cn)

    #iterate over each player rec and convert into dictionary 
    player_json_list = []
    for rec in player_list:
        player_json_list.append(rec.__dict__)
    
    response = jsonify(player_json_list)
    response.headers.add("Access-Control-Allow-Origin", "*")

    return response
    

if __name__ == '__main__':
    app.run(port=5000)