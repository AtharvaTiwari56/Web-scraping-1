import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
browser = requests.get(START_URL)
soup = BeautifulSoup(browser.text, 'html.parser')
star_table = soup.find('table')
temp_list  =[]
trs = star_table.find_all('tr')

for tr in trs:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temp_list.append(row)

Name = []
Distance =[]
Mass = []
Radius =[]
Luminosity = []
brightstar_data =[]

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][1])
    Distance.append(temp_list[i][3])
    Mass.append(temp_list[i][5])
    Radius.append(temp_list[i][6])
    Luminosity.append(temp_list[i][7])

brightstar_data = list(zip(Name, Distance, Mass, Radius, Luminosity))
with open("finalstarsnew.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(brightstar_data)