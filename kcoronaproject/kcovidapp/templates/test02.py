from bs4 import BeautifulSoup
import requests

# 전세계
r = requests.get('https://www.worldometers.info/coronavirus/')
html = r.content

soup = BeautifulSoup(html, 'html.parser')
# titles = soup.select('.post-content > h4 > a')
titles = soup.select('.maincounter-number > span')

corona_world_list = list()

print(titles)
for title in titles:
    corona_world_list.append(title.text)

print(corona_world_list[0])
