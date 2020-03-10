from flask import Flask
from flask_restful import Resource, Api, abort

from read_stats_from_database import search_json_by_date


app = Flask(__name__)
api = Api(app)


def get_records_from_database(country=None, timestamp=None):
    
    return records


def abort_if_country_doesnt_exist(country):
    if country not in get_records_from_jsons(country):
        abort(404, message=f"Country {country} doesn't exist")


class GetStatsRecordsByCountry(Resource):
    def get(self, country):
        abort_if_country_doesnt_exist(country)

        return


api.add_resource(GetStatsRecordsByCountry, '/records_by_country/<country>')

if __name__ == '__main__':
    app.run(debug=True)
