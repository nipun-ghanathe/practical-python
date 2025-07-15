#!/usr/bin/python3
# report.py
#
# Exercise 2.4

import sys
from pathlib import Path

from fileparse import parse_csv


def read_portfolio(filename: str) -> list:
    lines = Path(filename).read_text().splitlines()
    return parse_csv(lines, select=["name", "shares", "price"], types=[str, int, float])


def read_prices(filename: str) -> dict:
    lines = Path(filename).read_text().splitlines()
    return dict(parse_csv(lines, types=[str, float], has_headers=False))


def make_report(portfolio: list, prices: dict) -> list[tuple[str, int, float, float]]:
    return [
        (
            stock["name"],
            stock["shares"],
            prices[stock["name"]],
            prices[stock["name"]] - stock["price"],
        )
        for stock in portfolio
    ]


def print_report(report: list[tuple[str, int, float, float]]):
    headers = ("Name", "Shares", "Price", "Change")
    print(" ".join(f"{header:>10s}" for header in headers))
    print(" ".join("-" * 10 for _ in range(4)))
    for name, shares, price, change in report:
        print(f"{name:>10s} {shares:>10d} {price:>10.2f} {change:>10.2f}")


def portfolio_report(portfolio_file: str, prices_file: str) -> None:
    portfolio = read_portfolio(portfolio_file)
    prices = read_prices(prices_file)
    report = make_report(portfolio, prices)
    print_report(report)


def main(argv):
    if len(argv) != 3:  # noqa: PLR2004
        message = f"Usage: {argv[0]} portfile pricefile"
        raise SystemExit(message)
    portfile = argv[1]
    pricefile = argv[2]
    portfolio_report(portfile, pricefile)


if __name__ == "__main__":
    args = (
        sys.argv
        if len(sys.argv) > 1
        else ["report.py", "Data/portfolio.csv", "Data/prices.csv"]
    )
    main(args)
