from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    title = response["title"]
    return meme_large, subreddit, title

@app.route("/")
async def index():
    meme_pic, subreddit, title = get_meme()
    return render_template("index.html", meme_pic = meme_pic, subreddit = subreddit, title = title)

app.run(host="0.0.0.0")