from flask import Flask, render_template, request, redirect
from cockroachdb import Anime, AnimeDB
from news_scraping import News

app = Flask(__name__, template_folder='template', static_folder='static')
anime_app = News()


db_url = "postgresql://Abhay:Lo4jQy5LkBDj33DUzqf2tQ@cloudy-tang-7295.8nk.cockroachlabs.cloud:26257/AnimeBase?sslmode=verify-full"

anime_db = AnimeDB(db_url)
anime_instance = Anime(anime_db.conn)


@app.route("/")
def index():
    news_data = anime_app.anime_news()
    return render_template("index.html", data=news_data)


@app.route("/retrieve_data")
def retrieve_data():
    data_type = anime_instance.retrieve_data(anime_db.conn)
    return render_template('watchlist.html', data_types=data_type)


@app.route("/display", methods=["GET", "POST"])
def display():
    if request.method == "POST":
        anime_name = request.form.get('AnimeName')
        anime_type = request.form.get('Types')
        anime_episode = request.form.get('Episodes')
        return f"Form submitted with Username"

    return render_template('anime.html')


if __name__ == '__main__':
    app.run(debug=True)
