import json

from ..http import fetch


class VndApi:
    def __init__(self):
        self.url = "https://finfoapi-hn.vndirect.com.vn"

    def adPrice(self, tickers, fields, fromDate=None, toDate=None, **kwargs):
        """
        Get the historical price of tickers
        """
        api = "stocks/adPrice"

        # Putting it all together
        params = {"symbols": tickers, "fromDate": fromDate, "toDate": toDate}

        # Getting data as json
        data = fetch(f"{self.url}/{api}", params=params)
        content = data["data"]

        # Only return selected fields
        # must-have fields: symbol, tradingDate
        selectedFields = set(["symbol", "tradingDate", *fields])
        newContent = []
        for cell in content:
            newCell = {}
            for key, value in cell.items():
                if key in selectedFields:
                    newCell[key] = value
            newContent.append(newCell)

        # TODO: handle exception and errors
        # TODO: handle pagination

        return newContent
