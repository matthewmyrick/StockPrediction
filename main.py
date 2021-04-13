from flask import Flask, render_template, request, redirect, url_for
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        symbol = request.form['symbol']
        return redirect(url_for('analysis', symbol=symbol))
    return render_template('home.html')

@app.route('/analysis/<symbol>', methods=['POST', 'GET'])
def analysis(symbol):
    from request import Request
    from model import LSTMModel
    req = Request()
    lstm = LSTMModel()
    try:
        df = req.StockPrices(str(symbol))
        data = lstm.trainData(df, 5)
        predictions = data['Predictions'].to_list()
        closes = data['Close'].to_list()
        datesList = (data.index).to_list()
        dates = []
        for d in datesList:
            day = str(d.day)
            month = str(d.month)
            year = str(d.year)
            date = month + "/" + day + "/" + year
            dates.append(date)
        return render_template("analysis.html", dates=list(dates), closes=closes, predictions=predictions)
    except AttributeError:
        print("Please check symbol input.")
        return render_template("analysis.html")

if __name__ == "__main__":
    app.run(debug=True)
