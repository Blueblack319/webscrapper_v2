import os
import requests

print("Welcome to IsItDown.py!\nPlease write an URL or URLs you want to check. (seperated by comma)")

question = "y"
while question == "y":
    os.system("cls")

    writing = input()
    split_writing = writing.split(",")
    check = ""
    for url in split_writing:
        url = url.strip()
        if "." not in url:
            print(f"{url} is not a valid URL")
        elif "http" not in url:
            url = "http://" + url
            try:
                check = requests.get(url)
                if check.status_code == requests.codes.ok:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url} is down!")
        else:
            try:
                check = requests.get(url)
                if check.status_code == requests.codes.ok:
                    print(f"{url} is up!")
                else:
                    print(f"{url} is down!")
            except:
                print(f"{url} is down!")
    re = 1
    while re == 1:
        question = input("Do you want to start over? y/n")
        question = question.lower()
        if question == "y":
            re = 0
            continue
        elif question == "n":
            print("OK. bye")
            break
        else:
            print("That is not a valid answer.")




