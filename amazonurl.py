from bs4 import BeautifulSoup
import requests

url = ("https://www.amazon.in/s?k=redmi+11&sprefix=re%2Caps%2C210&ref=nb_sb_ss_softlines-tsdoa-contextual-iss_9_2")
data  = requests.get(url).text
soup=BeautifulSoup(data,"lxml")

for i in soup.find(("div"),{"class":"s-widget-container s-spacing-small s-widget-container-height-small celwidget slot=MAIN template=SEARCH_RESULTS widgetId=search-results_1"}):
    print(i.text)