"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request
from scrapper import extract_jobs

app = Flask("Scrapping remote-job")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    term = request.args.get("term")
    jobs = extract_jobs(term)
    return render_template("search.html", jobs)

app.run(host="localhost", port=5005)