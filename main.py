import requests
from bs4 import BeautifulSoup
import json

url = "http://mmis.ipt.kpi.ua"
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")

# text_from_article = soup.find("div", class_ = "alone-article clearfix")
all_a = soup.find(class_ = "menu").find_all("a")


all_articles_links_dict = []
for item in all_a:
    item_url = item.get("href")

    if(item_url == "#"):
        continue

    resp_article = requests.get(item_url)
    soup_article = BeautifulSoup(resp_article.text, "lxml")
    text_from_article = soup_article.find("div", class_ = "alone-article clearfix").text

    count = 0
    for index in range(len(text_from_article)):
        if(text_from_article[index] == ' '):
            count += 1
            
        if(count == 100):
            text_from_article = text_from_article[:index]
            count = 0
            break

    all_articles_links_dict.append((item.text, item_url, text_from_article))

with open("articles.json", "w") as file:
    json.dump(all_articles_links_dict, file, indent=4, ensure_ascii=False)
