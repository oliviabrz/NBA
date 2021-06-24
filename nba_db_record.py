#!/usr/bin/env python3

import pyodbc 

class TeamRecord:
    def __init__(self):
        self.ID = 0
        self.Abbreviation = None
        self.City = None
        self.Conference = None
        self.Division = None
        self.FullName = None
        self.Name = None 

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Team
        (ID, Abbreviation, City, Conference, Division, FullName, Name)
        values ({self.ID}, '{self.Abbreviation}', '{self.City}', '{self.Conference}', '{self.Division}', '{self.FullName}', '{self.Name}')
        """
        #print(insert_statement)
        #execute insert statement from the cursor
        cn.cursor().execute(insert_statement)
        
        #commit insert statement to database from the connection
        cn.connection().commit()

#----------
    def __str__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
Name: {self.Name}\n"""
        return string
        
#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
Name: {self.Name}\n"""         
        return string

class PlayerRecord:
    def __init__(self):
        self.ID = 0
        self.FirstName = None
        self.LastName = None
        self.Position = None
        self.HeightFeet = 0
        self.HeightInches = 0
        self.WeightPounds = 0
        self.TeamID = 0
        self.TeamAbbreviation = None

#----------
    def insert(self, cn):
        insert_statement = f"""
        insert into NBA.Player
        (FirstName, LastName, Position, HeightFeet, HeightInches, WeightPounds,TeamID)
        values ('{self.FirstName}', '{self.LastName}', 
        '{self.Position if self.Position != '' else 'NULL'}', 
        {self.HeightFeet if self.HeightFeet != None else 'NULL'},  
        {self.HeightInches if self.HeightInches != None else 'NULL'},
        {self.WeightPounds if self.WeightPounds != None else 'NULL'}, 
        {self.TeamID})
        """
        #print(insert_statement)
        #execute insert statement from the cursor
        cursor = cn.cursor()
        cursor.execute(insert_statement)
    
        #commit insert statement to database from the connection
        cn.connection().commit()
    
    #----------
    def get_team_id(self, cn, team_abbreviation):
        select_statement = f"""
        select ID from NBA.Team where Abbreviation = '{team_abbreviation}'
        """

        cursor = cn.cursor()
        cursor.execute(select_statement)
        
        result = cursor.fetchone()
        
        if result != None:
            self.TeamID = result[0]
        else:
            print (f'error retrieving ID for Abbreviation [{team_abbreviation}]')

#----------
    def __str__(self):
        string = f"""ID: {self.ID}, FirstName: {self.FirstName}, LastName: {self.LastName}, 
Position: {self.Position}, HeightFeet: {self.HeightFeet}, HeightInches: {self.HeightInches},
WeightPounds: {self.WeightPounds}, TeamID: {self.TeamID}\n"""
        return string

#----------
    def __repr__(self):
        string = f"""ID: {self.ID}, FirstName: {self.FirstName}, LastName: {self.LastName}, 
Position: {self.Position}, HeightFeet: {self.HeightFeet}, HeightInches: {self.HeightInches},
WeightPounds: {self.WeightPounds}, TeamID: {self.TeamID}\n"""
        return string