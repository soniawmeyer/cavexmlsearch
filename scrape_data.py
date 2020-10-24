
from bs4 import BeautifulSoup
import requests
import pandas as pd


def extract_cave_data(pages): 
    
    
    '''
    http://registry.gsg.org.uk/sr/browse.php 
    '''
    
    df = pd.DataFrame(columns = ['Name', 'Tags', 'Length', 'VR', 'Altitude']) 
    
    for i in range(0,pages+1): 
        url = f'http://registry.gsg.org.uk/sr/browse.php?page={i}'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        table = soup.find(class_='rowhover')
          
        df = df.append(pd.read_html(str(table))[0])
                        
    df.reset_index(inplace=True, drop=True)
    
    # I don't love this, I was extractig the URLs directly but had a bug in my code. I will try and come up with a better method 
    # after figuring out XML conversion 
    df['Link'] = [f'http://registry.gsg.org.uk/sr/sitedetails.php?id={i+1}' for i in list(df.index)]
    
    return df



extracted_data = extract_cave_data(20) #20 pages, connection was aborted when scraping large number of pages  
extracted_data.to_csv('extracted_data.csv', index=False)

