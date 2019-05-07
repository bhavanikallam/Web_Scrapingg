from bs4 import   BeautifulSoup
import requests
import lxml
import pandas as pd
import csv

import sys
http = requests.get('https://www.snopes.com/fact-check/')
soup = BeautifulSoup(http.content, 'lxml')


for g in soup.findAll('article', {"class":"list-group-item media"}):
 for w in g.findAll('div', {"class":"media-body"}):
     for j in w.findAll('p', {"class":"card-subtitle"}):
         w=w.get_text(strip=True)
         w=w.replace("					","")
         
         w=w.replace(",","")
         print(w,file=open("test.csv","a",encoding="utf-8"))


http = requests.get('https://www.ndtv.com/')
soup = BeautifulSoup(http.content, 'lxml')


for g in soup.findAll('div', {"class":"featured_cont"}):
 for f in g.findAll('a'):
        
        j=f.get_text(strip=True)
        j=j.replace(",","") 
        print(j,file=open("test.csv","a"))
       

#for a in soup.findAll('div', {"class":"description"}):
for a in soup.findAll('div', {"class":"row"}):
    for b in a.findAll('a'):
         l=b.get_text(strip=True)
         l=l.replace(",","") 
       
                    
                    
print(l,file=open("test.csv", "a",encoding='utf-8') )
