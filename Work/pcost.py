#!/usr/bin/python3
# pcost.py
#
# Exercise 1.27

import sys

from report import read_portfolio


def portfolio_cost(filepath: str) -> float:
    portfolio = read_portfolio(filepath)
    return sum(record["shares"] * record["price"] for record in portfolio)


def main(argv):
    if len(argv) != 2:  # noqa: PLR2004
        message = f"Usage: {argv[0]} portfile"
        raise SystemExit(message)
    portfile = argv[1]
    pcost = portfolio_cost(portfile)
    print("Total cost:", pcost)


if __name__ == "__main__":
    args = (
        sys.argv
        if len(sys.argv) > 1
        else ["report.py", "Data/portfolio.csv", "Data/prices.csv"]
    )
    main(args)
