from request import Request
from model import LSTMModel

req = Request()
lstm = LSTMModel()

df = req.StockPrices('aapl')

data = lstm.trainData(df, 1)
datesList = (data.index).to_list()
predictions = data['Predictions'].to_list()
closes = data['Close'].to_list()
dates = []
for d in datesList:
    day = str(d.day)
    month = str(d.month)
    year = str(d.year)
    date = month + "/" + day + "/" + year
    dates.append(date)
print("dates length: " + str(len(dates)))
print("predictions length: " + str(len(predictions)))
print("closes length: " + str(len(closes)))


print(dates)
print(predictions)
print(closes)