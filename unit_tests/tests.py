import unittest

from api.read_stats_from_database import *


class MyTestCase(unittest.TestCase):
    def test_search_json_by_date(self):
        self.assertTrue(get_json_path_by_date(date=datetime.strptime('09.03.2020', '%d.%m.%Y')))

    def test_read_json_file_to_dataframe(self):
        path = get_latest_json_file_path
        self.assertIsNotNone(read_json_file_to_dataframe(path))

    def test_get_records_by_country_from_dataframe(self):
        path = get_latest_json_file_path
        df = read_json_file_to_dataframe(path)
        self.assertIsNotNone(get_records_by_country_from_dataframe(df, 'China'))

    def test_get_records_from_database(self):
        self.assertIsNotNone(get_records_from_database(specific_date=datetime.strptime('09.03.2020', '%d.%m.%Y'),
                                                       country='China'))

    def test_get_countries_in_last_json_file(self):
        path = get_latest_json_file_path()
        df = read_json_file_to_dataframe(path)
        self.assertIsNotNone(get_only_countries_from_dataframe(df))

    def test_get_current_total_cases(self):
        self.assertIsNotNone(get_current_total_cases())


if __name__ == '__main__':
    unittest.main()
