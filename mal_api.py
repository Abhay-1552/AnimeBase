from mal import Anime


class MAL:
    def __init__(self, name, mal_id):
        self.anime_name = name
        self.mal_id = mal_id
        self.anime_details = []

    def mal_search(self):
        search = Anime(self.mal_id)

        data = {
            "English_Title": self.anime_name,
            "Japanese_Title": search.title,
            "Anime_Type": search.type,
            "Episodes": search.episodes,
            "Anime_ID": search.mal_id,
            "Anime_URL": search.url,
            "Anime_Image": search.image_url,
            "Anime_Score": search.score,
        }

        self.anime_details.append(data)

        return self.anime_details
