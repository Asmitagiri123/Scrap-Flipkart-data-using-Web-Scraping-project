import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
product_name=[]
product_price=[]
product_review=[]
product_description=[]
# for i in range(2,10):
url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page=1"
headers = {
    "User-Agent": "Mozilla/5.0"
}

r=requests.get(url)
# print(r)
soup=BeautifulSoup(r.text,"html.parser")
names=soup.find_all("div",class_="RG5Slk")
for i in names:
    product_name.append(i.text)
    print(i.text)

print("Total mobiles found:", len(product_name))
# print(soup.prettify())
# np=soup.find("a",class_="jgg0SZ").get("href")
# cnp="https://www.flipkart.com"+np
# print(cnp)