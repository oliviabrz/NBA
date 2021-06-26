#!/usr/bin/env python3

from nba_db_record import TeamRecord, PlayerRecord

def extract_teams_from_json(json_dict):
    rec_list = []

    for items in json_dict['data']:   
        #create new instance of class TeamRecord 
        teamrec = TeamRecord()
    
        #populate TeamRecord with values from the json_dict items 
        teamrec.ID = items['id']
        teamrec.Abbreviation = items['abbreviation'] 
        teamrec.City = items['city']
        teamrec.Conference = items['conference']
        teamrec.Division = items['division'] 
        teamrec.FullName = items['full_name']
        teamrec.Name = items['name']

        #add teamrec instance to rec_list 
        rec_list.append(teamrec)
        
    return rec_list

def extract_players_from_json(json_dict):
    rec_list = []
    for items in json_dict['data']:   
        #create new instance of class PlayerRecord 
        player_rec = PlayerRecord()

        #get Team Abbreviation 
        #team = items['team']
        #player_rec.TeamAbbreviation = team['abbreviation']      
    
        #populate record with values from the json_dict items 
        player_rec.ID = items['id']
        player_rec.FirstName = items['first_name'].replace("'", "")
        player_rec.LastName = items['last_name'].replace("'", "")
        player_rec.Position = items['position']
        player_rec.HeightFeet = items['height_feet'] 
        player_rec.HeightInches = items['height_inches']
        player_rec.WeightPounds = items['weight_pounds']
        team_id = items['team']
        player_rec.TeamID = team_id['id']
        
        #add rec instance to rec list 
        rec_list.append(player_rec)
        
    return rec_list