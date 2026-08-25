import json
from datetime import datetime
from pathlib import Path

from utils.constants import DB_DATE_FORMAT

DATA_DIR = Path(__file__).parent
DATA_DIR.mkdir(exist_ok=True)
JSON_FILE = DATA_DIR / "data.json"

data_template = {
    "lastrowid": 0,
    "users": {},
    "clients": {},
    "books": {},
    "loans": {}
}

def initialize_db():
    try:
        read()
    except FileNotFoundError:
        with open(JSON_FILE, "w", encoding="utf-8") as file:
            json.dump(data_template, file, ensure_ascii=False, indent=4)

def write(key: str, value: dict) -> None:
    data = read()

    data["lastrowid"] += 1
    data[key][data["lastrowid"]] = value
    data[key][data["lastrowid"]]["id"] = data["lastrowid"]
    #data[key][data["lastrowid"]]["created_at"] = datetime.now().strftime(DB_DATE_FORMAT)
    
    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return data["lastrowid"]

def update(key: str, id: int, value: dict) -> None:
    data = read()

    #created_at = data[key][str(id)]["created_at"]
    data[key][str(id)] = value
    data[key][str(id)]["id"] = id
    #data[key][str(id)]["created_at"] = created_at
    data[key][str(id)]["updated_at"] = datetime.now().strftime(DB_DATE_FORMAT)

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def delete(key: str, id: int) -> None:
    data = read()

    data[key][str(id)] = None

    with open(JSON_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def read():
    with open(JSON_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

def get(key: str, id: int) -> dict | None:
    data = read()
    try:
        return data[key][str(id)]
    except KeyError:
        return None