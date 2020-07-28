import csv

def save_to_file(term, jobs):
    file = open(f"downloaded_file/remote_{term}_jobs.csv", "w", -1, "utf-8")
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Apply"])
    for job in jobs:
        writer.writerow(list(job.values()))