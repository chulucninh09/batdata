import datetime as dt


class VndDate:
    """
    A model to adapt VND REST API date format
    """

    def __init__(self, dateInput):

        if isinstance(dateInput, str):
            self.date = dt.datetime.strptime(dateInput, "%Y%m%d")
        elif isinstance(dateInput, dt.datetime):
            self.date = dateInput
        else:
            raise TypeError(dateInput)

    @property
    def text(self):
        return self.date.strftime("%Y-%m-%d")

    def __repr__(self):
        return self.date.strftime("%Y-%m-%d")

    def __add__(self, other):
        return self.date + other

    def __sub__(self, other):
        return self.date - other


def tickersConversion(tickers):
    """
    Convert tickers from string or list format to string format to adapt with VND REST API
    """
    if isinstance(tickers, str):
        return tickers

    elif isinstance(tickers, list):
        for ticker in tickers:
            assert isinstance(ticker, str)
        return ",".join(tickers)

    else:
        raise TypeError("tickers should be string or list of string")


def fieldsConversion(fields):
    """
    Convert fields to list of fields to filter
    """
    if isinstance(fields, str):
        return [fields]

    elif isinstance(fields, list):
        for field in fields:
            assert isinstance(field, str)
        return fields

    else:
        raise TypeError("fields should be string or list of string")
