#!/usr/bin/env python3

import json
from nba_db_record import PlayerRecord, TeamRecord
from flask import Flask, request, jsonify
import requests
import pyodbc
from json import JSONEncoder
from sql_connection import SqlConnection


app = Flask(__name__)

#------------------------
# Player Api's
#------------------------
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

#------------------------
# Team Api's
#------------------------
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

if __name__ == '__main__':
    app.run(port=5000)