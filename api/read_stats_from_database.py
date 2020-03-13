import re
from datetime import datetime
from glob import glob

import pandas as pd


def get_all_jsons_paths_by_date():
    json_files = glob('../stats records/*.json')
    paths_by_date = {datetime.strptime(re.findall('[0-9]+.[0-9]+.[0-9]+', file_path)[0], '%d.%m.%Y'): file_path
                     for file_path in json_files}
    return paths_by_date


def get_min_max_date_of_json_paths(min_date=False, max_date=False):
    paths_by_date = get_all_jsons_paths_by_date()
    if max_date:
        return max(paths_by_date.keys())
    elif min_date:
        return min(paths_by_date.keys())
    else:
        return {
            'min_date': min(paths_by_date.keys()).strftime('%d.%m.%Y'),
            'max_date': max(paths_by_date.keys()).strftime('%d.%m.%Y'),
        }


def get_latest_json_file_path(only_file_date=False):
    paths_by_date = get_all_jsons_paths_by_date()
    max_date = get_min_max_date_of_json_paths(max_date=True)

    if only_file_date:
        return max_date.strftime('%d.%m.%Y')
    else:
        return paths_by_date[max_date]


def get_json_path_by_date(date):
    """
    :param date: format - DD.MM.YY
    :return: str, json file path
    """
    paths_by_date = get_all_jsons_paths_by_date()
    formatted_date = datetime.strptime(date, '%d.%m.%Y')
    if formatted_date not in paths_by_date:
        return False
    else:
        return paths_by_date[formatted_date]


def read_json_file_to_dataframe(path):
    df = pd.read_json(path)
    return df


def get_current_total_cases():
    path = get_latest_json_file_path()
    df = read_json_file_to_dataframe(path)
    total_cases_df = df[df['Country,Other'] == 'Total:']
    return total_cases_df.to_dict()


def get_records_by_country_from_dataframe(df, country):
    camel_case_country_name = country.title()
    try:
        df = df[df['Country,Other'] == camel_case_country_name]
    except:
        df = df[df['Country'] == camel_case_country_name]
    return df


def get_only_countries_from_dataframe(df):
    try:
        only_countries_df = df[['Country,Other']][:-1]
    except:
        only_countries_df = df[['Country']][:-1]
    return only_countries_df.to_dict()


def get_records_from_database(specific_date=None, country=None):
    if specific_date:
        json_file_path = get_json_path_by_date(specific_date)
        if not json_file_path:
            available_date_range = {'Error': 'selected date is not exists, see available min and max dates'}
            available_date_range.update(get_min_max_date_of_json_paths())
            return available_date_range
    else:
        json_file_path = get_latest_json_file_path()

    if json_file_path and country:
        all_countries_df = read_json_file_to_dataframe(json_file_path)
        df = get_records_by_country_from_dataframe(all_countries_df, country)
        if len(df) == 0:
            available_countries = {'Error': 'selected country not exists, see available countries'}
            available_countries.update(get_only_countries_from_dataframe(all_countries_df))
            return available_countries
    else:
        df = read_json_file_to_dataframe(json_file_path)

    return df.to_dict()
