import requests
from bs4 import BeautifulSoup

from typing import Any


def fetch_news():
    with requests.Session() as se:
        se.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "ru,en;q=0.9,uz;q=0.8,tg;q=0.7"
        }

    gazeta: str = 'https://www.gazeta.uz/' #asosiy sayt linki,  Pythonda type larni qo'llash uchun namuna
    response = se.get(f"{gazeta}oz/list/news/") #yangiliklar uchun link
    soup = BeautifulSoup(response.content, 'html.parser')
    articles: Any = soup.find_all("div", {"class": "nblock"}, limit=11) #Oxirgi 10 ta yangiliklarni ajratish
    article_list = []
    for article in articles:
        title = article.find("h3").get_text() #Maqola sarlavhasini ajratib olish
        content = article.find_all("a")[1].get("href") #Maqolaga kirish uchun linkni ajratib olish
        soup2 = BeautifulSoup(se.get(f"{gazeta}{content}").content, 'html.parser')
        content_top = soup2.find('h4').get_text()
        parags = soup2.find('div', {"itemprop": "articleBody"}).find_all("p")
        for prg in parags:
            if '"Gazeta.uz"da reklama' not in prg.get_text():
                content_top += prg.get_text()
            else:
                content_top += prg.get_text()[:-22]

        category = soup2.find('span', {"itemprop": "name"}).get_text() #Maqoladan kategoriyasini olish

        sources = soup2.find("a", {"rel": "noopener noreferrer"})

        if sources:
            link = sources.get("href") #Maqolaga manbasini olish
        else:
            link = "Bu maqolada manba keltirilmagan"

        pub_date = content[4:14] #Maqola joylangan sana ma'lumotini olish

        article_list.append({
            'title': title,
            'content': content_top,
            'category': category,
            'link': link,
            'pub_date': pub_date
        })
    return article_list

