from bs4 import BeautifulSoup
import requests
import re

gpu = input("What gpu do you want to search for? ")

url = f'https://www.newegg.ca/p/pl?d=3080&N=4131'

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")

page_text = doc.find(class_="list-tool-pagination-text").strong

pages = int(str(page_text).split("/")[-2].split(">")[-1][:-1])



for page in range(1, pages + 1):
  url = f'https://www.newegg.ca/p/pl?d={gpu}&N=4131&page={page}'
  result = requests.get(url)
  doc = BeautifulSoup(result.text, "html.parser")
  items = doc.find_all(text=re.compile(gpu))
  for item in items:
    print(item)
