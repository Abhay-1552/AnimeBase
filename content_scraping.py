from bs4 import BeautifulSoup
import requests
from mal_api import MAL


class Info:
    def __init__(self, name):
        self.title = name
        self.url_name = name.replace(' ', '_').replace(':', '').replace('?', '').lower()

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

            english_name = main_content.find('p', {'class': 'title-english title-inherit'})
            e_name = english_name.text.strip() if english_name else self.title

            name_id = [int(x) for x in content_link.split('/') if x.isnumeric()]

            data = MAL(self.title, name_id[0])
            mal_data = data.mal_search()

            return mal_data

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."


if __name__ == '__main__':
    app = Info('My Happy Marriage')
    print(app.anime_data())
