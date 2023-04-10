import requests
import json

def get_meme():
    url = "https://meme-api.com/gimme"
    response = json.loads(requests.request("GET", url).text)
    meme_large = response["preview"][-2]
    subreddit = response["subreddit"]
    title = response["title"]
    author = response["author"]
    postLink =  response["postLink"]
    return meme_large, subreddit, title, author, postLink