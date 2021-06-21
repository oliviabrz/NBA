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

    def insert(self, cn):
        insert_statement = f"""
        insert into Team
        (ID, Abbreviation, City, Conference, Division, FullName, Name)
        values (?,?,?,?,?,?,?)
        """
        #execute insert statement from the cursor
        cn.cursor().execute(insert_statement,
        (self.ID, self.Abbreviation, self.City, self.Conference, self.Division, self.FullName, self.Name))
        
        #commit insert statement to database from the connection
        cn.connection().commit()

    def __str__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
Name: {self.Name}\n"""
        return string

    def __repr__(self):
        string = f"""ID: {self.ID}, Abbreviation: {self.Abbreviation}, City: {self.City}, 
Conference: {self.Conference}, Division: {self.Division}, FullName: {self.FullName},
Name: {self.Name}\n"""         
        return string

