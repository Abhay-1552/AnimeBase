from bs4 import BeautifulSoup
import requests


class Info:
    def __init__(self, name):
        self.url = f'https://www.google.com/search?q={name}+myanimelist'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }

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

            link_content = soup.find('div', {'class': 'leftside'})
            img_link = link_content.find('img').get('data-src')

            name_content = soup.find('div', {'itemprop': 'name'})
            japanese_name = name_content.find('h1', {'class': 'title-name h1_bold_none'})
            j_name = japanese_name.text.strip() if japanese_name else 'Japanese Name'

            english_name = name_content.find('p', {'class': 'title-english title-inherit'})
            e_name = english_name.text.strip() if english_name else 'English Name'

            anime_id = link.split('/')[-2]

            return link, img_link, j_name, e_name, anime_id

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."


if __name__ == '__main__':
    app = Info('another')
    print(app.anime_info())
