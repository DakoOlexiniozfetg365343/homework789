import requests
from bs4 import BeautifulSoup

URL = "https://bank.gov.ua/"

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')





