import requests
from bs4 import BeautifulSoup

# def parsed_page(url):
#     req = requests.get(url)
#     page = req.text
#     soup = BeautifulSoup(page, "html.parser")
#     return soup
#
# def from_so(url):
#     soup = parsed_page(url)
#     jobs = []
#     jobList = soup.find("div", {"class": "listResults"})
#     jobContainers = jobList.find_all("div", {"class": "js-dismiss-overlay-container"}, recursive=False)
#     for jobContainer in jobContainers:
#         title = jobContainer.find("a", {"class": "stretched-link"})["title"]
#         company = jobContainer.find("h3", {"class": "fc-black-700 fs-body1 mb4"}).find("span").text
#         href = jobContainer.find("a", {"class": "stretched-link"})["href"]
#         href = f"https://stackoverflow.com{href}"
#         job = {"title": title, "url": href, "company": company}
#         jobs.append(job)
#     return jobs
#
# def extract_info(jobInfos):
#     jobs = []
#     for jobInfo in jobInfos:
#         jobInfo = jobInfo.find("a", recursive=False)
#         jobUrl = jobInfo["href"]
#         jobUrl = f"https://weworkremotely.com/{jobUrl}"
#         title = jobInfo.find("span", {"class": "title"}).text
#         company = jobInfo.find("span", {"class": "company"}).text
#         job = {"title": title, "url": jobUrl, "company": company}
#         jobs.append(job)
#     return jobs
#
# def from_wr(url):
#     soup = parsed_page(url)
#     jobLists = soup.find("div", {"id": "job_list"})
#     articles = jobLists.find_all("article")
#     jobs = []
#     for article in articles:
#         jobList = article.find("ul")
#         jobInfos = jobList.find_all("li", {"class": ""}, recursive=False)
#         jobInfos_feature = jobList.find_all("li", {"class": "feature"}, recursive=False)
#         subJobs = extract_info(jobInfos) + extract_info(jobInfos_feature)
#         print(subJobs)
#         jobs = jobs + subJobs
#     return jobs
#
# def from_ro(url):
#     pass
#
# def extract_jobs(term):
#     url_so = f"https://stackoverflow.com/jobs?r=true&q={term}"
#     url_wr = f"https://weworkremotely.com/remote-jobs/search?term={term}"
#     url_ro = f"https://remoteok.io/remote-dev+{term}-jobs"
#
#     fromSo = from_so(url_so)
#     fromWr = from_wr(url_wr)
#     fromRo = from_ro(url_ro)
#
#     jobs = fromSo + fromWr + fromRo
#     return jobs

url = "https://remoteok.io/remote-dev+python-jobs"
req = requests.get(url)
page = req.text
soup = BeautifulSoup(page, "html.parser")
# title, company
articles = soup.find("tbody", recursive=False).find_all("tr", {"class": "job"})
for article in articles:
    info = article.find("td", {"class": "company_and_position"}, recursive=False)
    title = info.find("a", {"itemprop": "hiringOrganization"}).find("h3", {"itemprop": "name"}).text
    print(title)









