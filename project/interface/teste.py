import requests
from bs4 import BeautifulSoup
import re
class Foo:
    
    def __init__(self, link):
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html')
        self.soup = soup
    def prices(self):
        prices = self.soup.find_all(text=re.compile('td'))
        print(prices[0])

huh = Foo('https://www.basketball-reference.com/players/c/chealjo01.html')

huh.prices()