"""Ипортируем модуль"""

import json

FILE_NAME = 'input.json'

def task() -> float:
    with open(FILE_NAME) as f:
        json_data = json.load(f)

    count_sum: int = sum([item["score"] * item["weight"] for item in json_data])
    return round(count_sum, 3)



print(task())

