import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("cls")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

# main, ask_from, ask_to, ask_money, convert
def show_list():
    url = "https://www.iban.com/currency-codes"
    req = requests.get(url)
    page = req.text
    soup = BeautifulSoup(page, "html.parser")

    table = soup.find("table")
    rows = table.find_all("tr")[1:]
    index = 0
    countries = []

    print("Welcome to CurrencyConvert PRO 2020")
    for row in rows:
        country_all = row.find_all("td")
        name = country_all[0].get_text()
        currency = country_all[2].get_text()
        if currency != "No universal currency":
            country = {name: currency}
            countries.append(country)
            print(f"#{index} {name}")
            index += 1
    return countries

def search(countries):
    try:
        selection = int(input("#: "))
        if selection > len(countries) or selection < 0:
            print("Choose a number from the list.")
            return search(countries)
        else:
            name = list(countries[selection])[0]
            currency = countries[selection].get(name)
            print(name, "\n")
            return currency
    except ValueError:
        print("That wasn't a number.")
        return search(countries)

def ask_from(countries):
    print("Where are you from? Choose a country by number.\n")
    code = search(countries)
    return  code

def ask_to(countries):
    print("Now choose another country.\n")
    code = search(countries)
    return code

def ask_amount(currency_from, currency_to):
    try:
        amount = int(input((f"How many {currency_from} do you want to convert to {currency_to}?\n")))
        return amount
    except:
        print("That wasn't a number.")
        return ask_amount(currency_from, currency_to)

def convert(code_from, code_to, source):
    try:
        url_trans = 'https://transferwise.com/gb/currency-converter/{}-to-{}-rate?amount={}'.format(code_from, code_to, source)
        req = requests.get(url_trans)
        page = req.text
        soup = BeautifulSoup(page, "html.parser")

        rate = float(soup.select_one("input#rate")["value"])
        target = source*rate
        amount_source = format_currency(source, code_from, locale="ko_KR")
        amount_converted = format_currency(target, code_to, locale="ko_KR")

        print(f"{amount_source} is {amount_converted}")

    except:
        print("Such coutries are not in transferwise...Sorry")

def main():
    countries = show_list()
    code_from = ask_from(countries)
    code_to = ask_to(countries)
    source = ask_amount(code_from, code_to)
    convert(code_from, code_to, source)

main()


