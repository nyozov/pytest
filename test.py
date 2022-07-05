from bs4 import BeautifulSoup
import requests

url = 'https://www.newegg.ca/p/pl?d=nvidia+3080&N=100006663%20601357247%20100007708'

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")


prices = doc.find_all(text="$")


strong = prices[0].parent.find("strong")

for price in prices:
    print(price.parent.find("strong").string)
