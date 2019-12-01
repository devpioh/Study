import sys
import urllib.request as req
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/"
web = req.urlopen( url )

soup = BeautifulSoup( web, "html.parser" )

price = soup.select_one("div.head_info > span.value").string

print( "usd/krw=", price )