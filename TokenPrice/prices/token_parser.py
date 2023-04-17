import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

agent = UserAgent().random

headers = {'User-Agent': agent}

base_url = 'https://crypto.com/price'


def parse_tokens():
    tokens_data = []
    digits = [1,2,3,4,5,6,7,8,9,0]
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_='css-1v8x7dw').find('table', class_='chakra-table css-1qpk7f7').find('tbody')
    tokens = data.find_all('tr')
    for token in tokens:
        token_id = token.find('td', class_='css-w6jew4').text
        token_name = token.find('p', class_='chakra-text css-rkws3').text
        token_short_name = token.find('span', class_='chakra-text css-1jj7b1a').text
        token_price = token.find('div', class_='css-b1ilzc').text.replace('$','').replace(',','')
        token_change = token.find('td', class_='css-1b7j986').find('p').text.replace('%','')
        token_volume = token.find_all('td', class_='css-1nh9lk8')[0].text.replace('B','').replace('M','').replace('$','').replace(',','')
        
        token_volume_char = str(token.find_all('td', class_='css-1nh9lk8')[0].text)
        for char in token_volume_char:
            if not char.isalpha():
                token_volume_char = token_volume_char.replace(char, '')

        token_cap = token.find_all('td', class_='css-1nh9lk8')[1].text.replace('B','').replace('M','').replace('$','').replace(',','')
        token_cap_char = token.find_all('td', class_='css-1nh9lk8')[1].text.replace('$','').replace(',','').split(' ')[-1]
        print(str(token_name) + str(token_cap_char) + str(token_volume_char))
        tokens_data += [[token_id, token_name, token_short_name, token_price, token_change, token_volume, token_volume_char, token_cap, token_cap_char]]
    return tokens_data