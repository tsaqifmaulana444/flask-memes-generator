from flask import Flask, render_template
import requests
import json
from func import get_meme

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
async def index():
    meme_pic, subreddit, title, author, postLink = get_meme()
    return render_template("index.html", meme_pic = meme_pic, subreddit = subreddit, title = title, author = author, postLink = postLink)

app.run(host="0.0.0.0")