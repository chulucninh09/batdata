import datetime as dt

from ..models import CurrDataModel, HistDataModel
from .taskManagement import createTasks, runTasks
from .utils import fieldsConversion, tickersConversion, VndDate


class Vnd:
    """
    Wrapper class to handle inputs and present output
    """

    def __init__(self, defaultFormat="df"):
        self.defaultFormat = defaultFormat

    def hist(self, tickers, fields, fromDate=None, toDate=None, **overrides):
        """
        Getting historical data.
        :tickers: string or list of string
        :fields: string or list of string
        :fromDate: 'yyyymmdd' string or python datetime object, default value is 20 days prior toTime
        :toDate: 'yyyymmdd' string or python datetime object, default value is today
        """

        tickers = tickersConversion(tickers)  # convert tickers to string
        fields = fieldsConversion(fields)  # convert fields to list of fields

        # Handle date format and generate default date
        if toDate is None:
            toDate = dt.datetime.today()
        toDate = VndDate(toDate)

        if fromDate is None:
            fromDate = toDate - dt.timedelta(days=20)
        fromDate = VndDate(fromDate)

        tasks = createTasks("hist", tickers, fields, fromDate, toDate, **overrides)
        data = runTasks(tasks)

        # TODO: implement overrides

        return HistDataModel(data)

    def curr(self, tickers, fields, **overrides):
        """
        Getting historical data.
        :tickers: string or list of string
        :fields: string or list of string
        """

        tickers = tickersConversion(tickers)  # convert tickers to string
        fields = fieldsConversion(fields)  # convert fields to list of fields

        tasks = createTasks("current", tickers, fields, **overrides)
        data = runTasks(tasks)

        # TODO: implement overrides

        return CurrDataModel(data)
