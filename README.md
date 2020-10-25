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
1. XML.db 
2. XMLconversion.py 
3. allcaves-database.xml - sample xml data used for testing purposes. Retrieved from:  https://github.com/nschorgh/CaveXML/blob/master/allcaves-database.xml 
4. cave_data.xml - scraped data converted to a CaveXML format as defined here: https://github.com/nschorgh/CaveXML/blob/master/cavexml.md
5. cavexmltosqlquery.py 
6. extracted_cave_data.csv - cave data scraped from: http://registry.gsg.org.uk/sr/browse.php
7. flask_app.py 
8. sample_scraped.csv - sample of scraped data, used for reference purposes 
9. scrape_data.py - code to scrape data from: http://registry.gsg.org.uk/sr/browse.php 