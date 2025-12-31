import pandas as pd 
from bs4 import BeautifulSoup 
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')
product_name=[]
product_price=[]
product_review=[]

for i in range(2,10):
 url="https://www.flipkart.com/search?q=mobile+under+50000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)
 headers = {
    "User-Agent": "Mozilla/5.0"
 }

 r=requests.get(url)
 # print(r)
 soup=BeautifulSoup(r.text,"html.parser")
 box=soup.find("div",class_="QSCKDh dLgFEE")
 names=box.find_all("div",class_="RG5Slk")

 for i in names:
     product_name.append(i.text)
    #  print(i.text)

#  print("Total mobiles found:", len(product_name))

 prices=box.find_all("div",class_="hZ3P6w DeU9vF")
 for i in prices:
     product_price.append(i.text)
    #  print(i.text)
#  print(len(product_price))    

 reviews=box.find_all("div",class_="MKiFS6")
 for i in reviews:
     product_review.append(i.text)
    #  print(i.text)
#  print(len(product_review))    

    
# print(soup.prettify())
# np=soup.find("a",class_="jgg0SZ").get("href")
# cnp="https://www.flipkart.com"+np
# print(cnp)
df=pd.DataFrame({"Product Name": product_name,"Prices": product_price,"Reviews": product_review})
# print(df)
df.to_csv("C:/Users/HP/OneDrive/Desktop/Flipkart_data_scrap/mobiles-under-5000.csv",index=False, encoding='utf-8-sig')