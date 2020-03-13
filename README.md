# CoronaVirus_Stats_API
Flask RESTful API for CoronaVirus Stats, for receiving history stats by country and or by date.

```
{
    "Hello": "Welcome to CoronaVirus Stats RESTful API",
    "Latest Update Date": "13.03.2020",
    "Total Cases": {....}
    "Credits": "Ofek Saar, ofekip@gmail.com",
    "Powered By": "Flask and pandas"
}
```

### Dependencies:
1. pandas
2. Flask
3. Scrapping data from https://www.worldometers.info/coronavirus/

#### Available queries:
    GET
    
    http://localhost:5000/
    http://localhost:5000/all_records/
    http://localhost:5000/records_by_country/<country>
    http://localhost:5000/records_by_date_country/<date>/<country>
     

### First time usage:
1. Run `web_scarp_data/web_scrap_legacy_stats.py` for setting up history stats database with help of https://archive.org/web/
2. Run `web_scarp_stats.py` DAILY for keeping an updated database.


## Example of query:
```
http://localhost:5000/records_by_country/china

{
    "Country,Other": {
        "0": "China"
    },
    "TotalCases": {
        "0": 80761
    },
    "NewCases": {
        "0": 26.0
    },
    "TotalDeaths": {
        "0": 3136.0
    },
    "NewDeaths": {
        "0": 17.0
    },
    "TotalRecovered": {
        "0": 60113.0
    },
    "ActiveCases": {
        "0": 17512
    },
    "Serious,Critical": {
        "0": 4794.0
    },
    "Tot\u00a0Cases/1M pop": {
        "0": 56.1
    }
}
```
