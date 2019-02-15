"""
To create a uniform API based on many REST API route getting different fields in just api command, 
we need to map each field into the function to get the field's data
"""


refFunc = {
    "hist": {
        "adPrice": [
            "open",
            "high",
            "low",
            "close",
            "average",
            "volume",
            "value",
            "ptVolume",
            "ptValue",
            "change",
            "percentage",
            "tradingDate",
        ]
    },
    "current": {
        "adPrice": [
            "open",
            "high",
            "low",
            "close",
            "average",
            "volume",
            "value",
            "ptVolume",
            "ptValue",
            "change",
            "percentage",
            "tradingDate",
        ]
    },
}

fieldLookup = {}
for dataType, fieldList in refFunc.items():
    fieldLookup[dataType] = {}
    for function, fields in fieldList.items():
        for field in fields:
            fieldLookup[dataType][field] = function
