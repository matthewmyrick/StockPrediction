import pandas_datareader as web
from pandas_datareader._utils import RemoteDataError
from datetime import date, datetime, timedelta
import matplotlib.pyplot as plt
import requests


class Request:
    def StockPrices(self, symbol):
        error = "ERROR"
        # get current day and stuff
        today = date.today()
        # get the exact dat 10 years ago
        ten_year = str(today.year - 10) + '-' + str(today.month) + '-' + str(today.day)
        try:
            df = web.DataReader(str(symbol), data_source='yahoo', start=ten_year, end=today)
            return df
        except RemoteDataError:
            return error
        except KeyError:
            return error

    def ListedStocks(self):
        response = requests.get(
            "https://pkgstore.datahub.io/core/nyse-other-listings/nyse-listed_json/data"
            "/e8ad01974d4110e790b227dc1541b193/nyse-listed_json.json "
        )
        symbols = []
        for stock in response.json():
            symbols.append(str(stock["ACT Symbol"]))
        return symbols
