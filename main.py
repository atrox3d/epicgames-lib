import scraping
import formatting

if __name__ == '__main__':
    soup = scraping.get_soup('transactions.html')

    rows = scraping.get_date_and_title(soup)
    for dt, title in rows:
        print(formatting.format_date(dt), title)
