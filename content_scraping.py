from bs4 import BeautifulSoup
import requests
from mal_api import MAL


class Info:
    def __init__(self, name):
        self.name = name
        self.url_name = name.replace(' ', '_').replace(':', '').replace('?', '').lower()

        self.title = None

        self.url = f'https://www.google.com/search?q={self.url_name}+myanimelist'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

    def anime_data(self):
        try:
            response = requests.get(self.url, headers=self.header)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find('a', {'jsname': 'UWckNb'})
            content_link = main_content.get('href')

            name_content = soup.find('div', {'class': 'h1-title'})

            japanese_name = name_content.find('h1', {'class': 'title-name h1_bold_none'})
            j_name = japanese_name.strong.get_text()

            english_name = name_content.find('p', {'class': 'title-english title-inherit'})
            e_name = english_name.get_text() if english_name else self.name

            name_id = [int(x) for x in content_link.split('/') if x.isnumeric()]

            if e_name is None:
                self.title = j_name
            else:
                self.title = e_name

            data = MAL(self.title, name_id[0])
            mal_data = data.mal_search()

            return mal_data

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."


if __name__ == '__main__':
    app = Info('My Happy Marriage')
    print(app.anime_data())
