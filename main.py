import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


url = 'https://cbr.ru/cash_circulation/memorable_coins/coins_base/#2'


if __name__ == '__main__':
    r = requests.get(url)
    print(r.status_code)
    soup = bs(r.text, "html.parser")
    catalog_numbers = soup.find_all('td', class_='coins-list_item_number middle right')
    names = soup.find_all('td', class_='coins-list_item_name middle')
    metalls = soup.find_all('td', class_='coins-list_item_metall middle')
    values = soup.find_all('td', class_='coins-list_item_face-value middle')
    dates = soup.find_all('td', class_='coins-list_item_date middle right')
    for number in catalog_numbers:
        print(number.text)
    for name in names:
        print(name.text)
    for metall in metalls:
        print(metall.text)