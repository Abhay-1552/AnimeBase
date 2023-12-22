from bs4 import BeautifulSoup
import requests


class News:
    def __init__(self):
        self.url = 'https://myanimelist.net/news'
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
        }
        self.anime_storage = []

    def anime_news(self):
        try:
            response = requests.get(self.url, headers=self.header)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            main_content = soup.find_all('div', {'class': 'news-unit clearfix rect'})

            for movie_card in main_content:
                if len(self.anime_storage) == 10:
                    break
                else:
                    title_element = movie_card.find('p', {'class': 'title'})
                    news_title = title_element.find('a').get_text() if title_element else "N/A"

                    image_element = movie_card.find('a', {'class': 'image-link'})
                    thumbnail_image = image_element.find('img').get('src') if image_element else "N/A"

                    info_element = movie_card.find('p', {'class': 'info di-ib'})
                    information = info_element.get_text() if info_element else "N/A"

                    news_date = information.strip().split(" by")[0]

                    data = {
                        "image_url": thumbnail_image,
                        "title": news_title,
                        "date": news_date
                    }

                    self.anime_storage.append(data)

            return self.anime_storage

        except requests.exceptions.RequestException as e:
            print("Error fetching content:", e)
            return "Error fetching data."
