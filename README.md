# cavexmlsearch

## Contents 
1. XML.db - xml converted to sqlite database
2. XMLconversion.py - converts csv file to xml data
3. allcaves-database.xml - sample xml data used for testing purposes. Retrieved from:  https://github.com/nschorgh/CaveXML/blob/master/allcaves-database.xml 
4. cave_data.xml - scraped data converted to a CaveXML format as defined here: https://github.com/nschorgh/CaveXML/blob/master/cavexml.md
5. cavexmltosqlquery.py - converts xml file to sqlite database class with query function
6. extracted_cave_data.csv - cave data scraped from: http://registry.gsg.org.uk/sr/browse.php
7. flask_app.py - flask app is the backend
8. sample_scraped.csv - sample of scraped data, used for reference purposes 
9. scrape_data.py - code to scrape data from: http://registry.gsg.org.uk/sr/browse.php
10. frontend - angular app is the frontend

## Steps to run frontend
1. navigate to cavexml-frontend folder to run angular app
* `cd frontend/cavexml-frontend`
* run `npm install`
* run `ng serve` on the terminal
2. simultaneously run flask app from the root folder
* `export FLASK_APP = flask_app.py`
* `flask run`
3. visit https://localhost:4000

## Technical Notes 

The cave data is first scraped from http://registry.gsg.org.uk/sr/browse.php using scrape_data.py. The name of the cave, tags associated with the cave type, length of the cave, vertical range and altitude of the caves are scraped from the main table. The link for each record is also obtained so that the user can refer back to the original source. The scraped data is stored in a dataframe and saved to a csv file as this is a common data format. 

The csv data is then converted to XML, so it can be used to create a database . An XML constructor was created using CaveXML as defined by Norbert Schörghofer (https://github.com/nschorgh). This constructor is used to convert the scraped data from a csv to an XML format using XMLconversion.py.

cavexmltosqlquery.py converts an XML data file to an SQLite database class with query function. flask_app.py creates an instance of this class and runs the query it receives a get request from the angular app front end and returns a json string.

Next Steps: The angular frontend does is not able to collect user input for the query parameters. There is no display for the return data.
