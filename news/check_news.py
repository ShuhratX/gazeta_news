import requests
from bs4 import BeautifulSoup


def fetch_news():
    with requests.Session() as se:
        se.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 YaBrowser/24.6.0.0 Safari/537.36",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,"
                      "*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "ru,en;q=0.9,uz;q=0.8,tg;q=0.7"
        }

    gazeta = 'https://www.gazeta.uz/' #asosiy sayt linki
    response = se.get(f"{gazeta}oz/list/news/") #yangiliklar uchun link
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = soup.find_all("div", {"class": "nblock"}, limit=10) #Oxirgi 10 ta yangiliklarni ajratish

    for article in articles:
        title = article.find("h3").get_text() #Maqola sarlavhasini ajratib olish
        print(title)
        content = article.find_all("a")[1].get("href") #Maqolaga kirish uchun linkni ajratib olish
        print(content)
        soup2 = BeautifulSoup(se.get(f"{gazeta}{content}").content, 'html.parser')
        # print(soup2,  "\n\n\n")
        content_top = soup2.find('h4').get_text()
        content_bottom = ''
        parags = soup2.find('div', {"itemprop": "articleBody"}).find_all("p")
        for prg in parags:
            if '"Gazeta.uz"da reklama' not in prg.get_text():
                content_top += prg.get_text()
            else:
                content_top += prg.get_text()[:-22]
        print("\n", content_top) #Maqola matnini olish

        category = soup2.find('span', {"itemprop": "name"}).get_text() #Maqoladan kategoriyasini olish
        print(category)

        for_manbaa = soup2.find("a", {"rel": "noopener noreferrer"})
        manbaa = ''
        if for_manbaa:
            manbaa = for_manbaa.get("href") #Maqolaga manbaani olish
        else:
            manbaa = "Bu maqolada manbaa keltirilmagan"
        print(manbaa)

        date_pub = content[4:14] #Maqola joylangan sana ma'lumotini olish
        print(date_pub, "\n\n\n")

    return "news_list"

news = fetch_news()
