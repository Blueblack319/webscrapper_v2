import requests

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
  return f"{base_url}/items/{id}"

# API-Done // Flask-ToDo : styling, Using data

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
    article = {"title": title, "url": url, "points": points, "author": author, "comments": comments}
    articles.append(article)
  return articles

order_by_pop = extract_info(info_pop)
order_by_new = extract_info(info_new)

print(list(order_by_pop[0].values()))
