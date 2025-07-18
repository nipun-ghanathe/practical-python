# ruff: noqa: PLE0237

# stock.py
#
# Exercise 4.1

from porty.typedproperty import Float, Integer, String


class Stock:
    """Object representing a stock."""

    __slots__ = ("_name", "_price", "_shares")

    name = String("name")
    shares = Integer("shares")
    price = Float("price")

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"

    @property
    def cost(self) -> float:
        return self.shares * self.price

    def sell(self, nshares: int) -> None:
        """Adjust the number of shares based on sold shares."""
        self.shares -= nshares
