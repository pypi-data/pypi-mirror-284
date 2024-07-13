"""

Inserting data to customer.json

"""

import json
from jmdexcel.select import select_all

def insert_data(file_path, entity, **data):
    """
    adding new customer data
    """

    if entity and file_path:
        load_data = select_all(file_path, entity)

        for item in data["data"]:
            load_data["data"].append(item)

        with open(file_path, "w") as outfile:
            json.dump(load_data, outfile)

        return load_data    
    else:
        raise Exception(f"No entity {entity} found in {file_path}.")
