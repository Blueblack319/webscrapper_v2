# create index.html
# create scrapper -> select, scrapper
# make fakeDb
# create read.html
from typing import Dict, Any

from flask import Flask, render_template, request
from scrapper import get_articles
app = Flask("DayEleven")

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]
db = {}

@app.route("/")
def index():
    return render_template("index.html", subreddits=subreddits)

@app.route("/read", methods=["GET"])
def read():
    global db
    selected = []
    for subreddit in subreddits:
        check = request.args.get(subreddit)
        if check == "on":
            selected.append(subreddit)
    newDb = get_articles(selected, db)
    db.update(newDb)
    return render_template("read.html", db=newDb, subreddits=selected)

app.run(host="localhost", port=5001)
