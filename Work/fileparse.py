# fileparse.py
#
# Exercise 3.3

import csv
from pathlib import Path


def parse_csv(
    filename: str,
    select: list | None = None,
    types: list | None = None,
    delimiter: str = ",",
    *,
    has_headers: bool = True,
) -> list:
    with Path(filename).open("rt", encoding="utf-8", newline="\n") as csv_file:
        if not has_headers:
            if select:
                message = "select argument requires column headers"
                raise RuntimeError(message)

            csv_reader = csv.reader(csv_file, delimiter=delimiter)
            if types:
                return [
                    tuple(func(val) for val, func in zip(row, types))
                    for row in csv_reader
                    if row
                ]
            return list(map(tuple, csv_reader))

        rows = csv.DictReader(csv_file, delimiter=delimiter)

        if select and types:
            return [
                {key: func(row[key]) for key, func in zip(select, types)}
                for row in rows
            ]
        if select:
            return [{key: row[key] for key in select} for row in rows]
        if types:
            return [
                {
                    key: func(value)
                    for key, value, func in zip(row.keys(), row.values(), types)
                }
                for row in rows
            ]
        return list(rows)
