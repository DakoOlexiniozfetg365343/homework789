import requests
from bs4 import BeautifulSoup

URL = "https://bank.gov.ua/"

r = requests.get(URL)

data = r.text

soup = BeautifulSoup (data, 'html.parser')

zxc = soup.find_all('div', {
    "class":"value"
})


print ("На данний момент в Україні спроживча інфляція становить")
print(zxc[0].text)





