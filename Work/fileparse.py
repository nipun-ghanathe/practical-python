# fileparse.py
#
# Exercise 3.3

import csv
from pathlib import Path
from typing import Any


def convert_types(types: list, rows: list | Any, *, silence_errors: bool = False) -> list[list[Any]]:
    converted = []
    for rowno, row in enumerate(rows):
        if not row:
            continue
        try:
            converted.append([func(val) for func, val in zip(types, row)])
        except ValueError as e:
            if silence_errors:
                pass
            else:
                print(f"Row {rowno}: Couldn't convert {row}")
                print(f"Row {rowno}: Reason {e}")
    return converted


def parse_csv(  # noqa: PLR0913
    filename: str,
    select: list | None = None,
    types: list | None = None,
    delimiter: str = ",",
    *,
    has_headers: bool = True,
    silence_errors: bool = False,
) -> list:
    with Path(filename).open("rt", encoding="utf-8", newline="\n") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=delimiter)

        if not has_headers:
            if select:
                message = "select argument requires column headers"
                raise RuntimeError(message)

            if types:
                rows = convert_types(types, csv_reader, silence_errors=silence_errors)
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
            rows = convert_types(types, rows, silence_errors=silence_errors)

        return [dict(zip(headers, row)) for row in rows]
