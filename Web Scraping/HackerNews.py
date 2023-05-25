import requests
from bs4 import BeautifulSoup

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, 'html.parser')
# print(soup.title) # everything inside title tag
# print(soup.body) # everything inside the <body> tag
# print(soup.body.contents[0]) # returns everything inside the body tag in a list form

# votes = soup.find_all("span", class_ = "titleline")
# a_tags = soup.find_all("a")
# for idx, tag in enumerate(a_tags):
#     print(f'{idx}, {tag}')

links = soup.select(".titleline > a")
scores = soup.select(".score")

def create_custom_hn(links, scores):
    hn = list(zip(links, scores))
    hn = list(filter(lambda x: int((x[1].text)[0:x[1].text.index(" ")]) > 100, hn))
    modified = []
    for data in hn:
        modified.append({'Title: ' + data[0].text, 'Link: ' + data[0].get('href'), 'Score: ' + data[1].text})
    return modified

print(create_custom_hn(links, scores))
