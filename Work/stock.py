# stock.py
#
# Exercise 4.1


class Stock:
    """Object representing a stock."""

    __slots__ = ("_shares", "name", "price")

    def __init__(self, name: str, shares: int, price: float) -> None:
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self) -> str:
        return f"Stock({self.name}, {self.shares}, {self.price})"

    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            message = "Expected int"
            raise TypeError(message)
        self._shares = value

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: int) -> None:
        """Adjust the number of shares based on sold shares."""
        self.shares -= nshares
