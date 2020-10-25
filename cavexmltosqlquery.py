import json
import xmltodict
import pandas as pd
import sqlite3
import numpy as np
import re

xmlfile = "allcaves-database.xml"

class CaveXMLtoSQLQuery:
    def __init__(self):
        '''the constructor creates and formats a database from the xmlfile'''

        def find_min(string):
            '''finds the min value of numbers within a string'''
            try:
                return min(list(map(int, re.findall(r'\d+', string))))
            except:
                return np.nan

        def find_max(string):
            '''finds the max value of numbers within a string'''
            try:
                return max(list(map(int, re.findall(r'\d+', string))))
            except:
                return np.nan

        try:
            with open(xmlfile, 'r') as f:
                xmlString = f.read() #opens and reads the xml file
            xml_dict = xmltodict.parse(xmlString) #converts xml string to dict
            xml_df = pd.DataFrame(xml_dict['CaveDataBase']['record']) #xml dict to pandas dataframe

            #formats the pandas dataframe for conversion to sqlite db
            xml_df.columns = [i.replace('-', '_') for i in xml_df.columns]
            problem_columns = ['state_or_province','phys_area_name','other_cave_name','contents','comments','reference','branch_name','altitude','vertical_extent','length']
            for column in problem_columns:
                xml_df[column] = xml_df[column].astype('str')
            xml_df.latitude = xml_df.latitude.astype('float')
            xml_df.longitude = xml_df.longitude.astype('float')
            number_columns = ['altitude','vertical_extent','length']
            for column in number_columns:
                xml_df[f'{column}_max'] = xml_df[column].apply(find_max)
                xml_df[f'{column}_min'] = xml_df[column].apply(find_min)
        except:
            print(f"Error: Failed to read or process {xmlfile}")

        try:
            sqliteConnection = sqlite3.connect('XML.db')
            cursor = sqliteConnection.cursor()
            xml_df.to_sql('XML', con=sqliteConnection, if_exists='replace')
            #creates sqlite3 database if doesn't already exist
        except:
            print("Error: Failed to create database")

    def sql_statement(self, tag, length, vertical_extent, altitude, length_gtlt, vertical_extent_gtlt, altitude_gtlt):
        '''the sql_statement takes class variables and returns an sql string'''
        if length_gtlt == "<=":
            length_max_min = "length_max"
        else:
            length_max_min = "length_min"

        if vertical_extent_gtlt == "<=":
            vertical_extent_max_min = "vertical_extent_max"
        else:
            vertical_extent_max_min = "vertical_extent_min"

        if altitude_gtlt == "<=":
            altitude_max_min = "altitude_max"
        else:
            altitude_max_min = "altitude_min"

        if tag == 'any':
            return f'''select * from XML where {length_max_min} {length_gtlt} {length} and {vertical_extent_max_min} {vertical_extent_gtlt} {vertical_extent} and {altitude_max_min} {altitude_gtlt} {altitude}'''
        else:
            return f'''select * from XML where cave_type = "{tag} and {length_max_min} {length_gtlt} {length} and {vertical_extent_max_min} {vertical_extent_gtlt} {vertical_extent} and {altitude_max_min} {altitude_gtlt} {altitude}'''

    def query(self, sql):
        '''the query function takes a sql statement as a string and return a json string'''
        with sqlite3.connect('XML.db') as conn:
            data = conn.execute(sql) #executes sql query
            return json.dumps(data.fetchall()) #returns json string

    def main(self):
        sql = self.sql_statement()
        return self.query(sql)


if __name__ == "__main__":
    s = CaveXMLtoSQLQuery()
    s.main()

# #checks every columns for sql compatiblity
# for column in xml_df.columns:
#     df = xml_df[column]
#     try:
#         sqliteConnection = sqlite3.connect('XML.db')
#         cursor = sqliteConnection.cursor()
#         df.to_sql('XML', con=sqliteConnection, if_exists='replace')
#     except:
#         print(column)

#xml_df.altitude.isnull().T.any().T.sum() #sum of null values in df

#future: convert number-of-entrances #can use same apply find_max
#future: split multiple entrances into separate entries? (branch_name, altitude)
