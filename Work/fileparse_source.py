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
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        if not has_headers:
            if select:
                message = "select argument requires column headers"
                raise RuntimeError(message)

            if types:
                rows = [
                    [func(val) for func, val in zip(types, row)]
                    for row in csv_reader
                    if row
                ]
            else:
                rows = [row for row in csv_reader if row]
            return list(map(tuple, rows))

        headers = next(csv_reader)

        if select:
            indices = [headers.index(header) for header in select]
            headers = select
            rows = [[row[i] for i in indices] for row in csv_reader if row]
        else:
            rows = [row for row in csv_reader if row]

        if types:
            rows = [[func(val) for func, val in zip(types, row)] for row in rows if row]

        return [dict(zip(headers, row)) for row in rows]
