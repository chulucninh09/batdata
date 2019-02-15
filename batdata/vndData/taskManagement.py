"""
To create a uniform API based on many REST API route getting different fields in just api command, 
we need to map each field into the function to get the field's data
"""

from .vndApi import VndApi
from .funcLookup import fieldLookup
from ..exceptions import FieldError


def createTasks(dataType, tickers, fields, *args, **kwargs):
    """
    Generate the tasks to get fields' data from many different REST API routes
    """
    tasks = {}
    for field in fields:
        try:
            function = fieldLookup[dataType][field]
        except KeyError as e:
            raise FieldError(f"Invalid field: {e.args} of function {dataType}")
        if function not in tasks:
            tasks[function] = {
                "tickers": tickers,
                "fields": [field],
                "args": args,
                "kwargs": kwargs,
            }
        else:
            tasks[function]["fields"].append(field)

    return tasks


def runTasks(tasks):
    """
    Run the generated tasks
    """

    api = VndApi()
    data = []
    for func, inputs in tasks.items():
        result = getattr(api, func)(
            inputs["tickers"], inputs["fields"], *inputs["args"], **inputs["kwargs"]
        )
        data = [*data, *result]

    # TODO: use threading/multiprocess to boost performance
    return data
