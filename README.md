# CoronaVirus_Stats_API
Flask RESTful API for CoronaVirus Stats.

For recevieng history stats by country, by date or by date range.

### Depencies:
1. pandas
2. Flask

#### Web scrapping data from https://www.worldometers.info/coronavirus/

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
