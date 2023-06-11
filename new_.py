from bs4 import BeautifulSoup
import requests

url = ("https://www.regexsoftware.com/placement-oriented-competitive-programming-program-july-2022/")
data=requests.get(url).text
soup=BeautifulSoup(data,"lxml")
# print(soup.prettify)


# for i in soup.find_all(("div"),{"class":"elementor-element elementor-element-52bbf464 elementor-widget elementor-widget-text-editor"}):
#     for j in i.find_all(("div"),{"class":"elementor-text-editor elementor-clearfix"}):
#         print(j.text)


for i in soup.find_all(("div"),{"class":"elementor-element elementor-element-56da8e4b elementor-widget elementor-widget-text-editor"}):
    for j in i.find_all(("div"),{"class":"elementor-text-editor elementor-clearfix"}):
        print(j.text)


