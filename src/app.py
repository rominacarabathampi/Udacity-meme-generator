import random
import os
import requests

from pathlib import Path
from MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor
from flask import Flask, render_template, request

app = Flask(__name__)


meme = MemeEngine("./static")


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']
    quotes = []

    for file in quote_files:
        print(file)
        quotes.extend(Ingestor.parse(file))
        print(Ingestor.parse(file))

    images_path = "./_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith('.jpg'):
            imgs.append(os.path.join(images_path, file))

    return quotes, imgs


quotes, imgs = setup()


@app.route("/")
def meme_rand():
    """Generate a random meme"""

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """User input for meme information"""
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """Create a user defined meme"""
    if not request.form["image_url"]:
        return render_template("meme_form.html")

    image_url = request.form['image_url']
    # Check if the path to the tmp file exists, otherwise create it.
    Path("./tmp/").mkdir(parents=True, exist_ok=True)
    try:
        r = requests.get(image_url, verify=False)

        tmp = f'./tmp/{random.randint(0, 1000000)}.png'
        img = open(tmp, 'wb').write(r.content)
    except requests.exceptions.ConnectionError:
        print('Bad Image URL, please try a different URL')
        return render_template('meme_error.html')

    body = request.form['body']
    author = request.form['author']
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
