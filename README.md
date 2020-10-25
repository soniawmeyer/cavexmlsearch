# cavexmlsearch
pull the changes - `git pull`
For staging/adding `git add .`
for commit - `git commit -a -m "commit_msg"`
for pushing code- `git push origin main`

## steps to run frontend
1. navigate to cavexml-frontend folder using `cd frontend/cavexml-frontend`
2. run `npm install`
3. run `ng serve` on the terminal
4. visit https://localhost: 4000

## Contents 
XML.db - 
XMLconversion.py - 
allcaves-database.xml - sample xml data used for testing purposes. Retrieved from:  https://github.com/nschorgh/CaveXML/blob/master/allcaves-database.xml 
cave_data.xml - scraped data converted to a CaveXML format as defined here: https://github.com/nschorgh/CaveXML/blob/master/cavexml.md
cavexmltosqlquery.py - 
extracted_cave_data.csv - cave data scraped from: http://registry.gsg.org.uk/sr/browse.php
flask_app.py - 
sample_scraped.csv - sample of scraped data, used for reference purposes 
scrape_data.py - code to scrape data from: http://registry.gsg.org.uk/sr/browse.php 