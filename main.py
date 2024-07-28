from pathlib import Path
from bs4 import BeautifulSoup
# import requests


def get_currency(in_currency, out_currency):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()
    rate = float(rate[:-4])
    return rate

def get_html(filepath:str|Path) -> str:
    try:
        with open(filepath, encoding="utf-8") as fp:
            contents = fp.read()
    except FileNotFoundError as fnfe:
        print(f"ERROR| {fnfe}\nexiting...")
        exit(1)
    except UnicodeDecodeError as ude:
        print(f"ERROR| {ude}\nexiting...")
        exit(2)
    return contents

def get_soup(filepath:str|Path) -> BeautifulSoup:
    html = get_html(filepath)
    soup = BeautifulSoup(html, 'html.parser')
    return soup

if __name__ == '__main__':
    # print(get_currency('USD', 'EUR'))
    soup = get_soup('transactions.html')
    # //table[contains(@class, "am")]//tr[@class="am-0"]
    # rows = soup.find_all("tr", {"class": "am-0"})   
    # for row in rows:
    #     print(row)
    table = soup.select('table')[0]
    rows = table.select('[class=am-0]')
    for row in rows:
        tds = row.select('td')[:2]
        txt = [td.text for td in tds]
        print(txt)