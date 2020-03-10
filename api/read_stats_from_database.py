import re
from datetime import datetime
from glob import glob


def search_json_by_date(date):
    json_files = glob('/stats records/*.json')
    paths_by_date = {datetime.strptime(re.findall('[0-9]+\.[0-9]+\.[0-9]+', file_path)[0], '%d.%m.%Y'): file_path
                     for file_path in json_files}
    return paths_by_date[date]


def read_json_file_to_dataframe(path):
    df = None
    return df


def get_records_from_dataframe(df, country=None):
    if country:
        pass
    return