from datetime import datetime
from time import sleep

import pandas as pd

import configs
from web_scrap_stats import get_coronavirus_cases_table, save_df_to_json_file


def build_timestamps_dataframe_from_web_archive():
    url = 'http://web.archive.org/cdx/search/cdx?url=https://www.worldometers.info/coronavirus/&output=txt'
    urls_df = pd.read_csv(url, sep=' ')
    urls_df.columns = [0, 'timestamp', 0, 0, 'status_code', 0, 0]
    urls_df = urls_df[['timestamp', 'status_code']]
    urls_df = urls_df[urls_df['status_code'] == '200']
    return urls_df


def get_valid_urls_by_dates_from_timestamps_dataframe(df):
    all_valid_urls_by_date = {}
    df.sort_values(by=['timestamp'], ascending=False, inplace=True)

    unique_dates = []
    for (_, row) in df.iterrows():
        timestamp = row[0]
        valid_date = str(timestamp)[:-6]
        if valid_date not in unique_dates:
            unique_dates.append(valid_date)

        valid_url = f'https://web.archive.org/web/{valid_date}/https://www.worldometers.info/coronavirus/'
        all_valid_urls_by_date[valid_date] = valid_url

    return all_valid_urls_by_date


def scrap_legacy_stats_tables(urls_by_dates):
    length = len(urls_by_dates)
    counter = 1
    for (date, url) in urls_by_dates.items():
        stats_df = get_coronavirus_cases_table(url, legacy=True)

        valid_date_for_path = datetime.strptime(date, '%Y%m%d').strftime('%d.%m.%Y')
        json_save_path = f'{configs.json_save_path}\coronavirus_stats-{valid_date_for_path}.json'
        save_df_to_json_file(stats_df, json_save_path)

        print(f'{counter}/{length} ---- json file created for date {valid_date_for_path} - {url}')
        counter += 1
        sleep(0.2)
    print('saving legacy stats json files finished.')


if __name__ == '__main__':
    timestamps_df = build_timestamps_dataframe_from_web_archive()
    urls_by_dates_for_scarp_tables = get_valid_urls_by_dates_from_timestamps_dataframe(timestamps_df)
    scrap_legacy_stats_tables(urls_by_dates_for_scarp_tables)



