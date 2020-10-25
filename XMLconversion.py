
import pandas as pd
import urllib


def read_data(url):
    data = pd.read_csv(url)
    return data


cave_df = read_data('https://raw.githubusercontent.com/soniawmeyer/cavexmlsearch/main/extracted_cave_data.csv')


# adjusting data to make columns consistent with CaveXML format: 
# https://github.com/nschorgh/CaveXML/blob/master/cavexml.md

cave_df = cave_df.rename(columns={'Name': 'principal-cave-name', 'Length' : 'length', 'VR': 'vertical-extent', 'Altitude': 'altitude', 'Link': 'reference', 'Tags' : 'cave-type'})



# https://stackoverflow.com/questions/18574108/how-do-convert-a-pandas-dataframe-to-xml 

def func(row):
    
    tags = ['country-name', 'state-or-province', 'phys-area-name', 'principal-cave-name', 'other-cave-name','latitude'
        'longitude', 'altitude', 'length','vertical-extent', 'number-of-entrances', 'rock-type', 'cave-type','contents',
        'ice-deposit-type','comments','cave-system','branch-name','reference','cave-use']
    
    xml = ['<record>']
    for item in tags:
        if item in row.index: 
            xml.append(f'  <{item}>{row[item]}</{item}>')
        else: 
            xml.append(f'  <{item}></{item}>')
    xml.append('</record>')
    return '\n'.join(xml)


output = '\n'.join(cave_df.apply(func, axis=1))
output_final = '<CaveDataBase>\n' + output + '\n</CaveDataBase>'


with open('cave_data.xml', 'w') as f:
    f.write(output_final)

