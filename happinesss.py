import pandas as pd
import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report"
res = requests.get(URL).text
soup = BeautifulSoup(res,'lxml')


table = soup.find('table',{'class':'wikitable sortable'})
table_rows = table.find_all('tr')

data = []
for row in table_rows:
    data.append([t.text.strip() for t in row.find_all('td')])
#print(data)

df = pd.DataFrame(data, columns=['index', 'Country', 'Happiness_score', 'GDP per capital', 'soacial support',
                       'healthylife', 'freedom', 'generosity', 'perceptions'])
#print(df.head())
df1 = df.dropna()
df1.to_csv("happyy.csv", index= False)

'''import pandas as pd
import requests

d =  pd.read_html("https://en.wikipedia.org/wiki/World_Happiness_Report#2019_report")

#print(d[4])
df1.to_csv("list_html.csv", index= False)
print(df.columns.values)'''