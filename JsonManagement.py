import json
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(SCRIPT_DIR, 'Data')
DATA_FILE = os.path.join(DATA_DIR, 'data.json')


def Add(data):
    os.makedirs(DATA_DIR, exist_ok=True)

    # Load existing data
    try:
        with open(DATA_FILE, "r") as file:
            ex_data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        ex_data = []

    # Insert data in date order
    inserted = False
    datadate = list(map(int, data.get("date").split("-")))  # [day, month, year]

    for i, entry in enumerate(ex_data):
        date = list(map(int, entry.get("date").split("-")))  # [day, month, year]
        # Compare year, then month, then day
        if (datadate[2] < date[2] or
                (datadate[2] == date[2] and datadate[1] < date[1]) or
                (datadate[2] == date[2] and datadate[1] == date[1] and datadate[0] < date[0])):
            ex_data.insert(i, data)
            inserted = True
            break

    # If not inserted, add to the end
    if not inserted:
        ex_data.append(data)

    # Save the updated data
    with open(DATA_FILE, "w") as file:
        json.dump(ex_data, file, indent=4)


def Find(keys, values):
    try:
        with open(DATA_FILE, 'r') as file:
            ex_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        ex_data = []

    results = []
    for entry in ex_data:
        if all(key in entry and entry[key] == value for key, value in zip(keys, values)):
            results.append(entry)

    if results:
        return results
    return None


def Fetch():
    os.makedirs(DATA_DIR, exist_ok=True)

    try:
        with open(DATA_FILE, 'r') as file:
            ex_data = json.load(file)
    except FileNotFoundError:
        ex_data = []
        with open(DATA_FILE, 'w') as file:
            json.dump(ex_data, file)
    except json.JSONDecodeError:
        ex_data = []

    return ex_data


def Remove(key, value):
    try:
        with open(DATA_FILE, 'r') as file:
            ex_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        ex_data = []

    new_data = [entry for entry in ex_data if not (key in entry and entry[key] == value)]
    with open(DATA_FILE, 'w') as file:
        json.dump(new_data, file, indent=4)


def ListValue(keys):
    try:
        with open(DATA_FILE, 'r') as file:
            ex_data = json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        ex_data = []

    values = set()
    for entry in ex_data:
        for key in keys:
            if key in entry:
                values.add(entry[key])

    if values:
        return list(values)
    return None