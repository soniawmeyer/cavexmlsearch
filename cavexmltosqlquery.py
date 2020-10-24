#CIS41B - Sonia Meyer - Lab 4
#The lab4_server.py acts as the back end server. It creates a database from
#an XML file, has a query function, and creates a socket to listen for data requests.

import json
import xmltodict
import pandas as pd
import sqlite3

xmlfile = "allcaves-database.xml"

class CaveXMLtoSQLQuery:
    def __init__(self):
        '''the constructor created a database from the xmlfile'''
        try:
            with open(xmlfile, 'r') as f:
                xmlString = f.read() #opens and reads the xml file
            xml_dict = xmltodict.parse(xmlString) #converts xml string to dict
            xml_df = pd.DataFrame(xml_dict['CaveDataBase']['record']) #xml dict to pandas dataframe
            xml_df = xml_df.astype('str') #fix later, can't all be a string
        except:
            print(f"Error: Failed to read or process {xmlfile}")

        try:
            sqliteConnection = sqlite3.connect('XML.db')
            cursor = sqliteConnection.cursor()
            xml_df.to_sql('XML', con=sqliteConnection, if_exists='replace')
            #creates sqlite3 database if doesn't already exist
        except:
            print("Error: Failed to create database")

        #class variables
        self.tag = "any" #lava tunnel
        self.length = "20" #null default to 0
        self.depth = "20"
        self.altitude = "20"
        self.length_gtlt = ">=" #must be >= or <=
        self.depth_gtlt = ">="
        self.altitude_gtlt = ">="

    def sql_statement(self):
        '''the sql_statement takes self.year_selection and self.year_selection
        class variables and returns an sql string'''
        if self.tag == 'any':
            return f'''select * from XML where length {self.length_gtlt} {self.length} and `vertical-extent` {self.depth_gtlt} {self.depth} and altitude {self.altitude_gtlt} {self.altitude}'''
        else:
            return f'''select * from XML where `cave-type` = "{self.tag} and length {self.length_gtlt} {self.length} and `vertical-extent` {self.depth_gtlt} {self.depth} and altitude {self.altitude_gtlt} {self.altitude}'''

    def query(self, sql):
        '''the query function takes a sql statement as a string and return a json string'''
        with sqlite3.connect('XML.db') as conn:
            data = conn.execute(sql) #executes sql query
            return json.dumps(data.fetchall()) #returns json string

    def main(self):
        sql = self.sql_statement()
        print(sql)
        print(self.query(sql))


if __name__ == "__main__":
    s = Server()
    s.main()
    # s.server_program()
    # sql = '''select * from XML where country-name = "Australia"'''
    # sql = 'select * from XML'
    # print(s.query(sql))
