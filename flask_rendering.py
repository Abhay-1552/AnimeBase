from flask import Flask, render_template, request
import mongodb

app = Flask(__name__, template_folder='template', static_folder='static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/retrieve_data")
def retrieve_data():
    data_type = mongodb.Anime.get_anime_data
    return render_template('watchlist.html', data=data_type)


if __name__ == '__main__':
    app.run(debug=True)
