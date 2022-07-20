import json
from datetime import datetime

valid_formats = ['%d %b %Y', '%b %d %Y', '%d %B %Y', '%B %d %Y', '%Y-%m-%dT%H', '%Y-%m-%dT%H:%M:%S']


def get_formatted_date(date_text: str):
    parsed_date = None
    for fmt in valid_formats:
        try:
            parsed_date = datetime.strptime(date_text.strip(), fmt)
            break
        except ValueError:
            parsed_date = datetime.now()
    return parsed_date
