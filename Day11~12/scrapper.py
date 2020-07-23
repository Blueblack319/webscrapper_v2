import requests
from bs4 import BeautifulSoup

def get_articles(subreddits, db):
    newDb = {}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    for subreddit in subreddits:
        fromDb = db.get(subreddit)
        if fromDb:
            articles = fromDb
        else:
            url = f"https://www.reddit.com/r/{subreddit}/top/?t=month"
            req = requests.get(url, headers=headers)
            page = req.text
            soup = BeautifulSoup(page, "html")
            # title, upvotes, url
            list = soup.find("div", {"class": "rpBJOHq2PR60pnwJlUyP0"})
            items = list.find_all("div", {"class": "_3xuFbFM3vrCqdGuKGhhhn0"})
            articles = []
            for item in items:
                upvotes = item.find("div", {"class": "_1rZYMD_4xY3gRcSS3p8ODO"}).text
                address = item.find("article", {"class": "yn9v_hQEhjlRNZI0xspbA"}).find("div", {"class": "_2wImphGg_1LcEF5MiErvRx"}).find("a").get("href")
                url = f"https://reddit.com{address}"
                title = item.find("article", {"class": "yn9v_hQEhjlRNZI0xspbA"}).find("div", {"class": "_2wImphGg_1LcEF5MiErvRx"}).find("a").find("div", {"class": "_2SdHzo12ISmrC8H86TgSCp"}).find("h3", {"class": "_eYtD2XCVieq6emjKBH3m"}).text
                article = {"upvotes": upvotes, "url": url, "title": title}
                articles.append(article)
        newDb[subreddit] = articles
        return newDb

