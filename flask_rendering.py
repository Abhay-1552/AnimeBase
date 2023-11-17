from flask import Flask, render_template, request
import mongodb
from news_scraping import News

app = Flask(__name__, template_folder='template', static_folder='static')
anime_app = News()


@app.route("/")
def index():
    news_data = anime_app.anime_news()
    print(news_data)
    return render_template("index.html", data=news_data)


@app.route("/retrieve_data")
def retrieve_data():
    data_type = mongodb.Anime.get_anime_data
    return render_template('watchlist.html', data=data_type)


if __name__ == '__main__':
    app.run(debug=True)
