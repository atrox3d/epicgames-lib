def format_date(date:str) -> str:
    m, d, y = date.split('/')
    return f'{y}/{m:>02}/{d:>02}'
