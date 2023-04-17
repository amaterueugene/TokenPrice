import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

agent = UserAgent().random

headers = {'User-Agent': agent}

base_url = 'https://crypto.com/price'


def parse_tokens():
    tokens_data = []
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='css-1v8x7dw').find('table', class_='chakra-table css-1qpk7f7').find('tbody')
    tokens = data.find_all('tr')
    for token in tokens:
        token_id = token.find('td', class_='css-w6jew4').text
        token_name = token.find('p', class_='chakra-text css-rkws3').text
        token_short_name = token.find('span', class_='chakra-text css-1jj7b1a').text
        token_price = token.find('div', class_='css-b1ilzc').text
        token_change = token.find('td', class_='css-1b7j986').find('p').text
        token_volume = token.find_all('td', class_='css-1nh9lk8')[0].text
        token_cap = token.find_all('td', class_='css-1nh9lk8')[1].text
        tokens_data += [token_id, token_name, token_short_name, token_price, token_change, token_volume, token_cap]
    return tokens_data


parse_tokens()