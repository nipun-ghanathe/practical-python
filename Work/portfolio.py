# portfolio.py
#
# Exercise 6.2

from collections import Counter
from collections.abc import Iterator

from stock import Stock


class Portfolio:
    def __init__(self, holdings: list[Stock]) -> None:
        self._holdings = holdings

    def __iter__(self) -> Iterator[Stock]:
        return self._holdings.__iter__()

    def __len__(self) -> int:
        return len(self._holdings)

    def __getitem__(self, index: int) -> Stock:
        return self._holdings[index]

    def __contains__(self, name: str) -> bool:
        return any(stock.name == name for stock in self._holdings)

    @property
    def total_cost(self) -> float:
        return sum(stock.cost for stock in self._holdings)

    def tabulate_shares(self) -> Counter:
        total_shares = Counter()  # type: ignore[var-annotated]
        for stock in self._holdings:
            total_shares[stock.name] += stock.shares
        return total_shares
