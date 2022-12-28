import requests
from bs4 import BeautifulSoup as bs


coin_catalog_url = 'https://cbr.ru/cash_circulation/memorable_coins/coins_base/#2'
coin_item_url = 'https://cbr.ru/cash_circulation/memorable_coins/coins_base/ShowCoins/?cat_num='

def link_parsing():
    r = requests.get(coin_catalog_url)
    soup = bs(r.text, "html.parser")
    #find_table = soup.find_all('div', {'class': "database-coins _list-wrap"})
    for data in soup.find_all('div', {'class': "database-coins _list-wrap"}):
        for row in data.find_all('tr'):
            print(dir(row))

    #item_parser(catalog_numbers_list)

def item_parser(catalog_numbers):
    for number in catalog_numbers:
        work_url = coin_item_url + number
        r = requests.get(work_url)
        soup = bs(r.text, "html.parser")
        catalog_number = number
        item_date = soup.find_all('div', class_='money_option_value')
        nominal_value = soup.find_all('div', class_='characteristic_value col-md-5 offset-md-1')
        print(nominal_value)