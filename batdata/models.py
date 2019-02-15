import pandas as pd


class CurrDataModel:
    def __init__(self, data):
        self.data = data
        self.df = pd.DataFrame(self.data)
        self.json = data

    def __repr__(self):
        return repr(self.data)


class HistDataModel:
    def __init__(self, data):
        self.data = data
        self.df = pd.DataFrame(self.data)
        self.json = data

    def __repr__(self):
        return repr(self.data)

