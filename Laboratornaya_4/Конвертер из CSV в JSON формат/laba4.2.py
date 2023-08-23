# TODO импортировать необходимые молули
import csv

import json

from collections import OrderedDict

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"



def task() -> None:
    with open(INPUT_FILENAME) as file:                  # TODO считать содержимое csv файла
        lines = [line for line in csv.DictReader(file)]

        with open(OUTPUT_FILENAME, "w") as file:
            json.dump(lines, file, indent=4)       # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")


