from flask import Flask, render_template, request, redirect, url_for
from cockroachdb import Anime, AnimeDB
from news_scraping import News
from mal_api import MAL
from dotenv import load_dotenv
import os


load_dotenv('.env')

app = Flask(__name__, template_folder='template', static_folder='static')

# Anime news instance
anime_app = News()

# Anime database Instance
db_url = os.getenv('db_url')

anime_db = AnimeDB(db_url)
anime_instance = Anime(anime_db.conn)

# IP addresses
allowedIPs = os.getenv('allowedIPs')


@app.route("/")
def index():
    news_data = anime_app.anime_news()
    return render_template("index.html", data=news_data)


@app.route("/retrieve_data")
def retrieve_data():
    data_type = anime_instance.retrieve_data()
    anime_count = anime_instance.types_of_anime()

    user_ip = request.remote_addr

    if user_ip in allowedIPs:
        return render_template('watchlist.html', data_types=data_type, anime_count=anime_count, form_enabled=True)
    else:
        return render_template('watchlist.html', data_types=data_type, IP=user_ip, anime_count=anime_count, form_enabled=False)


@app.route("/form_data", methods=["POST"])
def form_data():
    if request.method == 'POST':
        anime_name = request.form.get('inputName')
        anime_id = request.form.get('malId')

        anime_info = MAL(anime_name, anime_id)
        mal_data = anime_info.mal_search()

        anime_instance.insert_data(data=mal_data)

        return redirect(url_for('retrieve_data'))
    return '', 204


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, )
