# pcost.py
#
# Exercise 1.27

import csv
import sys
from pathlib import Path


def portfolio_cost(filepath: str) -> float:
    with Path(filepath).open("r", encoding="utf-8", newline="\n") as csv_file:
        data = csv.reader(csv_file)
        headers = next(data)

        pcost: float = 0
        for rowno, row in enumerate(data, start=1):
            record = dict(zip(headers, row))
            try:
                nshares = int(record["shares"])
                price = float(record["price"])
                pcost += nshares * price
            except ValueError:
                print(f"Row {rowno}: Bad row: {row}")
    return pcost


def main():
    filepath = sys.argv[1] if len(sys.argv) == 2 else "Data/portfolio.csv"  # noqa: PLR2004

    cost = portfolio_cost(filepath)
    print("\nTotal cost", cost)


if __name__ == "__main__":
    main()
