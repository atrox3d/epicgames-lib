import scraping
import formatting
from db.db import Db
from db.db_factory import get_db



if __name__ == '__main__':
    soup = scraping.get_soup('transactions.html')

    rows = scraping.get_date_and_title(soup)
    # for dt, title in rows:
    #     print(formatting.format_date(dt), title)
    db = get_db('epicgames-library.db')
    db.populate(rows)
    print(len(db.rows()))

    for title in sorted(db.titles(remove_the=True)):
        print(title)

    # matches = db.title_like('ghost')
    # for match in matches:
        # print(match)
