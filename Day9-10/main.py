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
commentsDb = {}
app = Flask("DayNine")


@app.route("/")
def home():
  orderBy = request.args.get("order_by") or "popular"
  if orderBy == "new":
    fromDb = db.get("new")
    if fromDb:
      articles = fromDb
    else:
      articles = extract_info(info_new)
      db["new"] = articles
    return render_template("home.html", articles=articles, order_by=orderBy)
  elif orderBy == None or "popular":
    fromDb = db.get("pop")
    if fromDb:
        articles = fromDb
    else:
        articles = extract_info(info_pop)
        db["pop"] = articles
    return render_template("home.html", articles=articles, order_by=orderBy)

@app.route("/<id>")
def detail(id):

    fromDb = commentsDb.get(id)
    if fromDb:
        comments = fromDb
    else:
        comments = []
        urlDetail = make_detail_url(id)
        req = requests.get(urlDetail)
        textDetail = req.json()
        infoDetails = textDetail["children"]
        # title, points, author, url
        title = textDetail["title"]
        points = textDetail["points"]
        author = textDetail["author"]
        url = textDetail["url"]
        article = {"title": title, "points": points, "author": author, "url": url}
        comments.append({"article": article})
        # author, text in children
        for infoDetail in infoDetails:
            if infoDetail["author"] is None:
                comment = {}
            else:
                author = infoDetail["author"]
                text = infoDetail["text"]
                comment = {"author": author, "text": text}
            comments.append(comment)
        commentsDb[id] = comments

    article = comments[0]["article"]
    comments = comments[1:]

    return render_template("detail.html", comments=comments, article=article)

app.run(host="localhost", port=5002)
