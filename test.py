from bs4 import BeautifulSoup

with open("index.html", "r") as f:
  doc = BeautifulSoup(f, "html.parser")


tag = doc.title
print(tag)