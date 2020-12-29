from bs4 import BeautifulSoup
import requests

r = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

soup = BeautifulSoup(r.content, 'html.parser')
# soup.prettify()
