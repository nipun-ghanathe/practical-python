# portfolio.py
#
# Exercise 6.2

from collections import Counter
from collections.abc import Iterable, Iterator
from typing import Self

from porty.fileparse import parse_csv
from porty.stock import Stock


class Portfolio:
    def __init__(self) -> None:
        self.holdings: list[Stock] = []

    def append(self, holding: Stock) -> None:
        if not isinstance(holding, Stock):
            message = "Expected a Stock instance."
            raise TypeError(message)
        self.holdings.append(holding)

    @classmethod
    def from_csv(cls, lines: Iterable, **opts) -> Self:
        self = cls()
        portdicts = parse_csv(
            lines, select=["name", "shares", "price"], types=[str, int, float], **opts
        )
        for portdict in portdicts:
            self.append(Stock(**portdict))
        return self

    def __iter__(self) -> Iterator[Stock]:
        return self.holdings.__iter__()

    def __len__(self) -> int:
        return len(self.holdings)

    def __getitem__(self, index: int) -> Stock:
        return self.holdings[index]

    def __contains__(self, name: str) -> bool:
        return any(stock.name == name for stock in self.holdings)

    @property
    def total_cost(self) -> float:
        return sum(stock.cost for stock in self.holdings)

    def tabulate_shares(self) -> Counter:
        total_shares: Counter = Counter()
        for stock in self.holdings:
            total_shares[stock.name] += stock.shares
        return total_shares
