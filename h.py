import requests 
from bs4 import BeautifulSoup

url="https://www.worldometers.info/coronavirus/"
    # Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text
    # Parse the html content
soup = BeautifulSoup(html_content, "lxml")
gdp_table = soup.find("table", id = "main_table_countries_today")
# print(gdp_table)

gdp_table_data = gdp_table.tbody.find_all("tr")
dicts = {}
for i in range(len(gdp_table_data)):
    try:
        key = (gdp_table_data[i].find_all('a', href=True)[0].string)
    except:
        key = (gdp_table_data[i].find_all('td')[0].string)

    value = [j.string for j in gdp_table_data[i].find_all('td')]
    dicts[key] = value


region = []
confirmed = []
for i in dicts:
    region.append(dicts[i][0])
    confirmed.append(dicts[i][1])

# for i in range(0,len(region)):
#     print(region[i],"  ",confirmed[i])