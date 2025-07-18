# ticker.py
#
# Exercise 6.10

import csv
from collections.abc import Generator, Iterable
from typing import Any, cast

from porty import tableformat
from porty.follow import follow
from porty.report import read_portfolio


def select_columns(rows: Iterable[list], indices: Iterable[int]) -> Generator[list]:
    return ([row[index] for index in indices] for row in rows)


def convert_types(rows: Iterable[list], types: Iterable) -> Generator[list]:
    return ([func(val) for func, val in zip(types, row)] for row in rows)


def make_dicts(
    rows: Iterable[list], headers: Iterable[str]
) -> Generator[dict[str, Any]]:
    return (dict(zip(headers, row)) for row in rows)


def filter_symbols(
    rows: Iterable[dict[str, Any]], names: Iterable[str]
) -> Generator[dict[str, Any]]:
    return (row for row in rows if row["name"] in names)


def parse_stock_data(lines: Iterable[str]) -> Generator[dict]:
    rows = csv.reader(lines)
    rows = select_columns(rows, [0, 1, 4])  # type: ignore[assignment]
    rows = convert_types(rows, [str, float, float])  # type: ignore[assignment]
    rows = make_dicts(rows, ["name", "price", "change"])  # type: ignore[assignment]
    return rows  # type: ignore[return-value]  # noqa: RET504


def ticker(portfile: str, logfile: str, fmt: str = "txt") -> None:
    portfolio = cast("Iterable[str]", read_portfolio(portfile))
    lines = follow(logfile)
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    formatter = tableformat.create_formatter(fmt)
    formatter.headings(["Name", "Price", "Change"])
    for row in rows:
        formatter.row(map(str, row.values()))


if __name__ == "__main__":
    portfolio = cast("Iterable[str]", read_portfolio("Data/portfolio.csv"))
    lines = follow("Data/stocklog.csv")
    rows = parse_stock_data(lines)
    rows = filter_symbols(rows, portfolio)
    for row in rows:
        print(row)
