from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv
import requests
import pandas as pd
START_URL="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(START_URL)
soup=BeautifulSoup(page.text,"html.parser")
startTable=soup.find('table')
tableList=[]
tableRows=startTable[0].find_all('tr')
for tr in tableRows:
    td=tr.find_all('td')
    row=[i.text.rstrip() for i in td]
    tableList.append(row)
Name=[]
Distance=[]
Mass=[]
Radius=[]
for i in range(1, len(tableList)):
    Name.append(tableList[i][0])
    Distance.append(tableList[i][5])
    Mass.append(tableList[i][8])
    Radius.append(tableList[i][9])
df=pd.DataFrame(list(zip(Name,Distance,Mass,Radius)),columns=['star_name','distance',"mass",'radius'])
df.to_csv('dwarfStars.csv')