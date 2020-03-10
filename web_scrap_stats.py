from datetime import datetime

import pandas as pd

import configs


def get_coronavirus_cases_table(url=None, legacy=None):
    if not url:
        url = 'https://www.worldometers.info/coronavirus/'
    dfs = pd.read_html(url)
    if legacy:
        coronavirus_cases_df = dfs[2]
    else:
        coronavirus_cases_df = dfs[0]
    return coronavirus_cases_df


def save_df_to_json_file(dataframe, path=None):
    if not path:
        date = datetime.now().strftime('%d.%m.%Y')
        path = f'{configs.json_save_path}\coronavirus_stats-{date}.json'
    dataframe.to_json(path, indent=4)
    print('saving json file finished.')


if __name__ == '__main__':
    df = get_coronavirus_cases_table()
    save_df_to_json_file(df)
