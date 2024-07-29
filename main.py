import scraping
import formatting
from db.db import Db
from db.jsondb import JsonDb



if __name__ == '__main__':
    soup = scraping.get_soup('transactions.html')

    rows = scraping.get_date_and_title(soup)
    # for dt, title in rows:
    #     print(formatting.format_date(dt), title)
    db = JsonDb('epicgames-library.json')
    db.create(rows)
    match = db.title_like('tomb')
    print(match)