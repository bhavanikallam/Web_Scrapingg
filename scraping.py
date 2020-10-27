import sys
import os
import requests
from bs4 import BeautifulSoup
#url = 'https://blog.talosintelligence.com/2020/10/threat-roundup-1002-1009.html'
#url = 'https://blog.talosintelligence.com/2020/10/threat-roundup-1016-1023.html'
url = sys.argv[1]
print(url)
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
page = requests.get(url, headers=headers)
#print(page.content.decode())
print(page)
# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup)


f = open("hashes.csv", "w")
lst =[]
table = soup.find_all("div", attrs={'class':'code'})
for row in table:
    rows = row.find('code')
    #print(rows.text)
    lst.append(rows.text)
    f.write(rows.text)
    
f.close()


data = []

for w in soup.find_all('table', {'class':'threat-breakdown-table'}):
    #table_body = w.find_all('tbody')
    for x in w.find_all('tbody') or w.find_all('thead'):
        for h in w.find_all('th', {'style':"width: 600px;"}):
            #print(h.text)
            data.append(h.text.upper()+"\n")
            for y in x.find_all('tr'):
                #rows = x.find_all('tr')
                for z in y.find_all('td'):
                    #print(z.text)
                    for a in z.findAll('code'):
                        #print(a.text)
                        data.append(a.text.replace("\n", ""))
                    
#print(data) 
f = open("iocs.csv", "w")
for i in data:
    lst = i.split(",")
    lst = list(map(str.strip, lst))
    lst = str(lst)
    lst = lst.replace("\n", " ")
    lst = lst.replace(",", "-")
    a = str(lst)[2:-2]+"\n"
    #print(str(lst))
    f.writelines(a)
    
f.close()

print("Done.. U will find the ouput in hashes.csv and iocs.csv")




          
