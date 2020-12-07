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
# 총 3개
# 총 감염자 / 사망자 / 회복된 사람

print('')

corona_K_list = list()
# 한국
r = requests.get('https://www.worldometers.info/coronavirus/country/south-korea/')
html = r.text

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('.maincounter-number > span')

for title in titles:
    corona_K_list.append(title.text)

# 총 3개
# 총 감염자 / 사망자 / 회복된 사람


html = requests.get('https://www.worldometers.info/coronavirus/').text
html_soup = BeautifulSoup(html, 'html.parser')
rows = html_soup.find_all('tr')


def extract_text(row, tag):
    element = BeautifulSoup(row, 'html.parser').find_all(tag)
    text = [col.get_text() for col in element]
    return text


corona_list = []
for row in rows:
    test_data = extract_text(str(row), 'td')[1:9]
    corona_list.append(test_data)

print(corona_list)

print(str(corona_list))

# for i in corona_list:
#    for j in i:
#        print(corona_list)


a = [1, 2, 3]

# corona_list
# 0 => 국가
# 1 => 총 확진자
# 2 => 새 확진자(당일 나온 사람)
# 3 => 총 사망자
# 4 => 새 사망자(당일 나온 사람)
# 5 => 총 완치자
# 6 => 새 완치자(당일 나온 사람)
# 7 => 현재 걸린 사람 수
