# fileparse.py
#
# Exercise 3.3

import csv
from collections.abc import Iterable
from typing import Any


def convert_types(
    types: list, rows: Iterable, *, silence_errors: bool = False
) -> list[list[Any]]:
    converted = []
    for rowno, row in enumerate(rows):
        try:
            converted.append([func(val) for func, val in zip(types, row)])
        except ValueError as e:  # noqa: PERF203
            if not silence_errors:
                print(f"Row {rowno}: Couldn't convert {row}")
                print(f"Row {rowno}: Reason {e}")
    return converted


def parse_csv(  # noqa: PLR0913
    rows: Iterable,
    select: list | None = None,
    types: list | None = None,
    delimiter: str = ",",
    *,
    has_headers: bool = True,
    silence_errors: bool = False,
) -> list:
    """Parse a CSV into a list of records with type conversion."""
    csv_reader = csv.reader(rows, delimiter=delimiter)
    rows = [row for row in csv_reader if row]

    if not has_headers:
        if select:
            message = "select argument requires column headers"
            raise RuntimeError(message)
        if types:
            rows = convert_types(types, rows, silence_errors=silence_errors)
        return list(map(tuple, rows))

    headers = rows.pop(0)
    if select:
        indices = [headers.index(header) for header in select]
        headers = select
        rows = [[row[i] for i in indices] for row in rows]
    if types:
        rows = convert_types(types, rows, silence_errors=silence_errors)
    return [dict(zip(headers, row)) for row in rows]
