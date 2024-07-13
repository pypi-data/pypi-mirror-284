"""

Customer module to get the cstomer details
Return Customer dictonary

"""

import json


def select_all(file_path,entity):
    """
    Read the json data from data/customer.json

    Return the json data
    """

    if entity:
        with open(file_path, 'r') as f:
            data=json.load(f)
    else:
        data=None

    return data
