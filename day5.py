import requests
from bs4 import BeautifulSoup

def result(num, list=[]):
    country_name = list[num][0]
    currency_code = list[num][1]
    print(f"You chose {country_name}")
    print(f"The currency code is {currency_code}")

def select():
    try:
        number = int(input("#: "))
        if number >= 0 and number <= 265:
            return number
        else:
            print("Choose the number from the list.")
            return select() # select() is Error when I write 432432 at first and then write number from the list -> Why??
    except:
        print("That wasn't a number.")
        return select()# select() is Error when I write 432432(example) at first and then write number from the list -> Why??


def main():
    url = "https://www.iban.com/currency-codes"
    req = requests.get(url)
    page = req.text
    soup = BeautifulSoup(page, "html.parser")

    table = soup.find("tbody")
    rows = table.find_all("tr")
    country_num = 0
    countries = []

    print("Hello! Please choose select a country by number:")
    for country in rows:
        currency = country.select_one("td:nth-of-type(2)").get_text()
        country_name = country.select_one("td:nth-child(1)").get_text()
        country_code = country.select_one("td:nth-child(3)").get_text()
        if currency != "No universal currency":
            countries.append((country_name, country_code))
            print(f"# {country_num} {country_name}")
            country_num += 1

    num = select()
    result(num, countries)

main()