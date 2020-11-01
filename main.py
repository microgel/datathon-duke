# Load the Pandas libraries with alias 'pd'
import pandas as pd 
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
data = pd.read_csv("dataset/affinity.csv")
# Preview the first 5 lines of the loaded data 
mp =  dict()
mp.update({
    '1':'Los Angeles',
    '2':'New York City',
    '3':'Chicago',
    '4':'Houston',
    '5':'Phoenix',
    '6':'San Diego',
    '7':'Dallas',
    '8':'Las Vegas',
    '9':'Seattle',
    '10':'Fort Worth',
    '11':'San Antonio',
    '12':'San Jose',
    '13':'Detroit',
    '14':'Philadelphia',
    '15':'Columbus',
    '16':'Austin',
    '17':'Charlotte',
    '18':'Indianapolis',
    '19':'Jacksonville',
    '20':'Memphis',
    '21':'San Francisco',
    '22':'El Paso',
    '23':'Baltimore',
    '24':'Portland',
    '25':'Boston',
    '26':'Oklahoma City',
    '27':'Louisville',
    '28':'Denver',
    '29':'Washington',
    '30':'Nashville',
    '31':'Milwaukee',
    '32':'Albuquerque',
    '33':'Tucson',
    '34':'Fresno',
    '35':'Sacramento',
    '36':'Atlanta',
    '37':'Kansas City',
    '38':'Miami',
    '39':'Raleigh',
    '40':'Omaha',
    '41':'Oakland',
    '42':'Minneapolis',
    '43':'Tampa',
    '44':'New Orleans',
    '45':'Wichita',
    '46':'Cleveland',
    '47':'Bakersfield',
    '48':'Honolulu',
    '49':'Boise',
    '50':'Salt Lake City',
    '51':'Virginia Beach',
    '52':'Colorado Springs',
    '53':'Tulsa'
})

for ind in data.index:
    data['cityid'][ind] = mp[str(data['cityid'][ind])]

print(data)
data.to_csv('affinity2.csv',index=False)