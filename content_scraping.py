from bs4 import BeautifulSoup
import requests


class Info:
    def __init__(self, name):
        self.url = f'https://www.google.com/search?q={name}+myanimelist'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.anime_content = []

    def anime_link(self):
        try:
            response = requests.get(self.url, headers=self.header)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find('a', {'jsname': 'UWckNb'})
            content_link = main_content.get('href')

            return content_link

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."

    def anime_info(self):
        try:
            link = Info.anime_link(self)

            response = requests.get(link, headers=self.header)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find('div', {'class': 'leftside'})
            img_link = main_content.find('img').get('data-src')

            return link, img_link

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."
