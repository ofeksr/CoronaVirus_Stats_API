from flask import Flask
from flask_restful import Resource, Api

from api.read_stats_from_database import get_records_from_database, get_latest_json_file_path, get_current_total_cases


app = Flask(__name__)
api = Api(app)


class Welcome(Resource):
    def get(self):
        return {
            'Hello': 'Welcome to CoronaVirus Stats RESTful API',
            'Latest Update Date': get_latest_json_file_path(only_file_date=True),
            'Total Cases': get_current_total_cases(),
            'Credits': 'Ofek Saar',
            'Powered By': 'Flask and pandas',
        }


class GetAllStatsRecords(Resource):
    def get(self):
        return get_records_from_database()


class GetStatsLatestRecordsByCountry(Resource):
    def get(self, country):
        return get_records_from_database(country=country)


class GetStatsRecordsByDateCountry(Resource):
    def get(self, date, country):
        return get_records_from_database(specific_date=date, country=country)


api.add_resource(Welcome, '/')
api.add_resource(GetAllStatsRecords, '/all_records/')
api.add_resource(GetStatsLatestRecordsByCountry, '/records_by_country/<country>')
api.add_resource(GetStatsRecordsByDateCountry, '/records_by_date_country/<date>/<country>')


if __name__ == '__main__':
    app.run(debug=True)
