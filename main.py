from bs4 import BeautifulSoup as BS
import requests


class Parser:
    HTML = ""
    RES = []


    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        response = requests.get(self.url).text
        self.HTML = BS(response, 'lxml')


    def parsing(self):
        news = self.HTML.find_all('div', class_='caption')
        for item in news:
            title = item.find('h3', {'class': 'topic-title'}).text
            href = item.find('a').get('href')
            author = item.find('a', {'class':'topic-info-author-link'}).text.strip()
            self.RES.append({
            'title': title,
            'href': href,
            'author': author})

    def save(self):
        with open(self.path, 'w') as f:
            i = 1
            for elem in self.RES:
                f.write(f"Новость № {i}\n\nНазвание: {elem['title']}\nСсылка: {elem['href']}\nАвтор: {elem['author']}")
                f"\n\n{'*' * 20}\n"
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()
