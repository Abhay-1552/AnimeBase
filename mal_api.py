from mal import AnimeSearch


class MAL:
    def __init__(self):
        self.anime_details = []

    def mal_api(self, name):
        search = AnimeSearch(name)

        anime = search.results[0]

        data = {
            "English Title": name,
            "Japanese Title": anime.title,
            "Anime Type": anime.type,
            "Episodes": anime.episodes,
            "Anime ID": anime.mal_id,
            "Anime URL": anime.url,
            "Anime Image": anime.image_url,
            "Anime Score": anime.score,
            "Anime Synopsis": anime.synopsis
        }

        self.anime_details.append(data)

        return self.anime_details
