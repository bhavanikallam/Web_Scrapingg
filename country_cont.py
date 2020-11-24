import sys
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://simple.wikipedia.org/wiki/List_of_countries_by_continents'
#url = 'https://blog.talosintelligence.com/2020/10/threat-roundup-1016-1023.html'
#url = sys.argv[1]
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print(page.content.decode())
print(page)
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'lxml')
#print(soup)

lst =[]
f = open("listt.txt", "w")

for i in (soup.find_all("ol")):
    #print(i)
    for a in i.find_all("li"):
        #print(a)
            #print(a.find("a").get('href'))
        try:
            count = a.find("a").get('href')
            count = count[6:]
            #print(count)
            lst.append(count)
            #print(lst)
            df = pd.DataFrame(lst, columns=["COUNTRIES"])
            #print(df)
            f.write(count+ "\n")
        except:
            pass
#print(lst)
#print(df)
f.close()
soup = BeautifulSoup(page.text, "lxml")
txt = (t.text for t in soup.find_all("span", class_="mw-headline"))
conti = list(txt)
conti1 = conti[0:7]
df1= pd.DataFrame(conti1, columns=["CONTINENTS"])
#print(conti1)
#print(df1)
a = pd.concat([df,df1], axis=1)
a.to_csv("continent.csv", index=False)
print(a.head())