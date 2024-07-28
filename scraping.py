from pathlib import Path
from bs4 import BeautifulSoup
import datetime
from typing import Generator

# import requests

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

def get_date_and_title(soup:BeautifulSoup) -> Generator[list[datetime.datetime | str], None, None]:
    table = soup.select('table')[0]
    rows = table.select('[class=am-0]')
    for row in rows:
        tds = row.select('td')[:2]
        txt = [td.text for td in tds]
        if len(txt):
            dt, title = txt
            yield dt, title