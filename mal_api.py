from mal import AnimeSearch, Anime
from content_scraping import Info


class MAL:
    def __init__(self, name):
        self.anime_name = name
        self.anime_details = []

    def mal_api(self):
        search = AnimeSearch(self.anime_name)

        anime = search.results[0]

        data = {
            "English_Title": self.anime_name,
            "Japanese_Title": anime.title,
            "Anime_Type": anime.type,
            "Episodes": anime.episodes,
            "Anime_ID": anime.mal_id,
            "Anime_URL": anime.url,
            "Anime_Image": anime.image_url,
            "Anime_Score": anime.score,
            "Anime_Synopsis": anime.synopsis
        }

        self.anime_details.append(data)

        return self.anime_details

    def comparison(self):
        MAL.mal_api(self)

        print("Hello")

