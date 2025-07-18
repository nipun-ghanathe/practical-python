#!/usr/bin/python3
# report.py
#
# Exercise 2.4

import sys
from pathlib import Path
from typing import Any

from porty import tableformat
from porty.fileparse import parse_csv
from porty.portfolio import Portfolio


def read_portfolio(filename: str, **opts: Any) -> Portfolio:  # noqa: ANN401, ARG001
    lines = Path(filename).read_text().splitlines()
    return Portfolio.from_csv(lines)


def read_prices(filename: str) -> dict:
    lines = Path(filename).read_text().splitlines()
    return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(
    portfolio: Portfolio, prices: dict
) -> list[tuple[str, int, float, float]]:
    return [
        (
            stock.name,  # name
            stock.shares,  # nshares
            prices[stock.name],  # current price
            prices[stock.name] - stock.price,  # change in price
        )
        for stock in portfolio
    ]


def print_report(
    report: list[tuple[str, int, float, float]], formatter: tableformat.TableFormatter
) -> None:
    formatter.headings(["Name", "Shares", "Price", "Change"])
    for name, shares, price, change in report:
        rowdata = [name, str(shares), f"{price:.2f}", f"{change:.2f}"]
        formatter.row(rowdata)


def portfolio_report(portfolio_file: str, prices_file: str, fmt: str = "txt") -> None:
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)

    report = make_report(portfolio, prices)

    formatter = tableformat.create_formatter(fmt)
    print_report(report, formatter)


def main(argv: list) -> None:
    if len(argv) < 3:  # noqa: PLR2004
        message = f"Usage: {argv[0]} portfile pricefile [format]"
        raise SystemExit(message)
    portfile = argv[1]
    pricefile = argv[2]
    fmt = argv[3] if len(argv) > 3 else "txt"  # noqa: PLR2004
    portfolio_report(portfile, pricefile, fmt=fmt)


if __name__ == "__main__":
    from porty import logging_setup  # noqa: F401

    args = (
        sys.argv
        if len(sys.argv) > 1
        else ["report.py", "Data/portfolio.csv", "Data/prices.csv"]
    )
    main(args)
