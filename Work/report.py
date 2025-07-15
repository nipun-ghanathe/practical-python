# report.py
#
# Exercise 2.4

import csv
from pathlib import Path
from typing import TypedDict, cast


class Stock(TypedDict):
    name: str
    shares: int
    price: float


def read_portfolio(filename: str) -> list[Stock]:
    with Path(filename).open("rt", encoding="utf-8", newline="\n") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        type_map = {
            "shares": int,
            "price": float,
        }
        return [
            cast(
                "Stock",
                {
                    key: type_map.get(key, lambda x: x)(value)
                    for key, value in row.items()
                },
            )
            for row in csv_reader
        ]


def read_prices(filename: str) -> dict[str, float]:
    with Path(filename).open("rt", encoding="utf-8", newline="\n") as csv_file:
        csv_reader = csv.reader(csv_file)
        return {row[0]: float(row[1]) for row in csv_reader if len(row) != 0}


def make_report(
    portfolio: list[Stock],
    prices: dict[str, float],
) -> list[tuple[str, int, float, float]]:
    report = []
    for stock in portfolio:
        name = stock["name"]
        nshares = stock["shares"]
        purchase_price = stock["price"]
        current_price = prices[name]
        price_change = current_price - purchase_price
        report.append((name, nshares, current_price, price_change))
    return report


def main():
    portfolio = read_portfolio("Data/portfolio.csv")
    prices = read_prices("Data/prices.csv")
    report = make_report(portfolio, prices)

    headers = ("Name", "Shares", "Price", "Change")

    print(" ".join(f"{header:>10s}" for header in headers))
    print(" ".join("-" * 10 for _ in range(4)))

    for name, shares, price, change in report:
        print(
            f"{name:>10s} {shares:>10d} {('$' + f'{price:.2f}'):>10s} {change:>10.2f}",
        )


if __name__ == "__main__":
    main()
