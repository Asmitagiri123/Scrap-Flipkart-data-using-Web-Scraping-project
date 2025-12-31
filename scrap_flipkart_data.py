import pandas as pd 
from bs4 import BeautifulSoup 
import requests
url="https://www.flipkart.com"
r=requests.get(url)
print(r)