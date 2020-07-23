# create index.html
# create scrapper -> select, scrapper
# make fakeDb
# create reading.html
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
print(db)
@app.route("/")
def index():
    return render_template("index.html", subreddits=subreddits)

@app.route("/read", methods=["GET"])
def reading():
    selected = []
    for subreddit in subreddits:
        check = request.args.get(subreddit)
        if check == "on":
            selected.append(subreddit)
    newDb = get_articles(selected, db)
    print(newDb)
    db = db.update(newDb)


    return render_template("read.html", db=db)

app.run(host="localhost", port=5001)
