import requests
from bs4 import BeautifulSoup
from pprint import pprint

# print(soup.title) # everything inside title tag
# print(soup.body) # everything inside the <body> tag
# print(soup.body.contents[0]) # returns everything inside the body tag in a list form

# votes = soup.find_all("span", class_ = "titleline")
# a_tags = soup.find_all("a")
# for idx, tag in enumerate(a_tags):
#     print(f'{idx}, {tag}')

def gather_data():
    all_links, all_scores = [], []
    for i in range(1, 27):
        res = requests.get("https://news.ycombinator.com/")
        if i != 1:
            res = requests.get(f'https://news.ycombinator.com/?p={i}')
        soup = BeautifulSoup(res.text, 'html.parser')
        links = soup.select(".titleline > a")
        scores = soup.select(".score")
        if (len(links) != 0 and len(scores) != 0):
            all_links.append(links)
            all_scores.append(scores)
    return [all_links, all_scores]

def sort_stories_by_votes(hn):
    return sorted(hn, reverse = True, key = lambda k: int(k[1].text.replace(" points", "")))

def create_custom_hn(links, scores):
    hn = list(zip(links, scores))
    filtered_content = []
    for page_content in hn:
        combined = list(zip(page_content[0], page_content[1]))
        filtered_content.append(list(filter(lambda x: int((x[1].text)[0:x[1].text.index(" ")]) > 100, combined)))
    modified = []
    for filtered in filtered_content:
        for content in filtered:
            modified.append(content)
    modified = sort_stories_by_votes(modified)
    res = []
    for data in modified:
        points = int(data[1].text.replace(" points", ""))
        res.append({'Title': data[0].text, 'Link': data[0].get("href"), 'Points': points})
    return res

if __name__ == "__main__":
    pprint(create_custom_hn(gather_data()[0], gather_data()[1]))
