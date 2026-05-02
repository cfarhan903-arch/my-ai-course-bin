import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.alibaba.com/trade/search?spm=a2700.product_home_newuser.header.132.2ce267afSeLPmg&SearchText=Auto+Accessories&indexArea=product_en&search_cource_scene=pc_home_product_category&has4Tab=true&tab=all"
r = requests.get (url)

soup = BeautifulSoup(r.content,'')