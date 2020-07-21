import requests
from flask import Flask, render_template, request

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


# API-Done // Flask-Done

req_pop = requests.get(popular)
req_new = requests.get(new)
text_pop = req_pop.json()
text_new = req_new.json()
info_pop = text_pop['hits']
info_new = text_new["hits"]


# title, url, points, author, comments

def extract_info(list):
    articles = []
    for info in list:
        title = info["title"]
        url = info["url"]
        points = info["points"]
        author = info["author"]
        comments = info["num_comments"]
        objectID = info["objectID"]
        article = {"title": title, "url": url, "points": points, "author": author, "comments": comments, "objectID": objectID}
        articles.append(article)
    return articles

db = {}
app = Flask("DayNine")


@app.route("/", methods=["GET", "POST"])
def home():
  order_by = request.args.get("order_by") or "popular"
  if order_by == "new":
    fromDb = db.get("new")
    if fromDb:
      articles = fromDb
    else:
      articles = extract_info(info_new)
      db["new"] = articles
    return render_template("home.html", articles=articles, order_by=order_by)
  elif order_by == None or "popular":
    fromDb = db.get("pop")
    if fromDb:
        articles = fromDb
    else:
        articles = extract_info(info_pop)
        db["pop"] = articles
    return render_template("home.html", articles=articles, order_by=order_by)


app.run(host="localhost")
