import os
import csv
import requests
from bs4 import BeautifulSoup

# main, extract_jobs, save_to_file
def check(object):
    try:
        return object.text
    except AttributeError:
        return None

def extract_jobs(brand_list):
    # place, title, time, pay, date
    jobs = []
    index = 1
    for brand in brand_list:
        brand_url = brand.find("a")["href"]
        req = requests.get(brand_url)
        page = req.text
        soup = BeautifulSoup(page, "html.parser")
        print(f"Scrapping jobs: brand {index}")
        index += 1

        table = soup.find("div", {"id": "NormalInfo"})
        job_list = table.find("tbody").find_all("tr")[::2]

        for job_info in job_list:
            if not job_info.find("td", {"align": "center"}):
                job_place = check(job_info.find("td", {"class": "local first"}))
                job_title = check(job_info.find("td", {"class": "title"}).find("span", {"class": "title"}))
                job_time = check(job_info.find("td", {"class": "data"}).find("span", {"class": "time"}))
                job_pay = check(job_info.find("td", {"class": "pay"}))
                job_date = check(job_info.find("td", {"class": "regDate last"}))
                job = {"place": job_place, "title": job_title, "time": job_time, "pay": job_pay, "date": job_date}
                jobs.append(job)
    return jobs

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8", newline="")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "time", "pay", "date"])
    for job in jobs:
        writer.writerow(list(job.values()))

def main():
    alba_url = "http://www.alba.co.kr"

    req = requests.get(alba_url)
    page = req.text
    soup = BeautifulSoup(page, "html.parser")

    brand_list = soup.find("div", {"id": "MainSuperBrand"}).find("ul", {"class": "goodsBox"}).find_all("li")

    jobs = extract_jobs(brand_list)
    save_to_file(jobs)


main()






