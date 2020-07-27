"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-dev+python-jobs

Good luck!
"""

from flask import Flask, render_template, request, send_file, send_from_directory
from werkzeug.utils import redirect

from scrapper import extract_jobs
from save import save_to_file

app = Flask("Scrapping remote-job")
db = {}

@app.route("/")
def home():
    return render_template("home.html")

def check(term):
    if term in db:
        jobs = db[term]
    else:
        jobs = extract_jobs(term)
        db[term] = jobs
    return jobs

@app.route("/search")
def search():
    term = request.args.get("term").lower()
    jobs = check(term)
    number = len(jobs)
    return render_template("search.html", jobs=jobs, number=number, term=term)

@app.route("/export")
def export():
    try:
        term = request.args.get("term").lower()
        if not term:
            raise Exception
        jobs = db.get(term)
        if not jobs:
            raise Exception
        save_to_file(term, jobs)
        return send_file(f"remote_{term}_jobs.csv")
    except:
        return "lalalalal"
app.run(host="localhost", port=5005)