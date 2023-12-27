from flask import Flask, render_template, request, redirect, url_for
from cockroachdb import Anime, AnimeDB
from news_scraping import News
from content_scraping import Info


app = Flask(__name__, template_folder='template', static_folder='static')

# Anime news instance
anime_app = News()

# Anime database Instance
db_url = "postgresql://Abhay:Lo4jQy5LkBDj33DUzqf2tQ@cloudy-tang-7295.8nk.cockroachlabs.cloud:26257/AnimeBase?sslmode=verify-full"

anime_db = AnimeDB(db_url)
anime_instance = Anime(anime_db.conn)


@app.route("/")
def index():
    news_data = anime_app.anime_news()
    return render_template("index.html", data=news_data)


@app.route("/retrieve_data")
def retrieve_data():
    data_type = anime_instance.retrieve_data()
    return render_template('watchlist.html', data_types=data_type)


@app.route("/form_data", methods=["POST"])
def form_data():
    if request.method == 'POST':
        anime_name = request.form.get('inputName')

        anime_info = Info(anime_name)
        mal_data = anime_info.anime_data()
        print("Requested", mal_data)

        anime_instance.insert_data(data=mal_data)

        return redirect(url_for('retrieve_data'))
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
