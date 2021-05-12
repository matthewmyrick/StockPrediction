from request import Request
from model import LSTMModel
import matplotlib.pyplot as plt
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        self.L1 = tk.Label(self.master, text="Input Ticker Symbol")
        self.L1.pack(side=tk.LEFT)

        self.E1 = tk.Entry(self.master, bd=5)
        self.E1.pack(side=tk.RIGHT)

        self.B1 = tk.Button(self.master, text="Submit", command=lambda: self.runModel())
        self.B1.pack(side=tk.BOTTOM)

    def say_hi(self):
        print(str(self.E1.get()).upper())

    def runModel(self):
        # get data
        Req = Request()
        data = Req.StockPrices(str(self.E1.get()).upper())
        # print(data)

        # put data into model
        model = LSTMModel()
        result = model.trainData(data, 5)

        print(result)
        # result.to_csv(index=True, archive_name='output.csv')

        predictions = result['Predictions'].to_list()
        closes = result['Close'].to_list()
        dates = result.index.to_list()

        plt.plot(dates, predictions, label="predictions")
        plt.plot(dates, closes, label="price")
        plt.legend()
        plt.show()

    def downloadCsv(self):
        return

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()