# ruff: noqa: PT009,PT027

import unittest

from stock import Stock


class TestStock(unittest.TestCase):
    def test_basic(self):
        s = Stock("GOOG", 100, 490.1)
        self.assertEqual(s.name, "GOOG")
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        self.assertEqual(s.cost, 49010.0)
        s.sell(50)
        self.assertEqual(s.shares, 50)
        # self.assertRaises(TypeError, setattr, s, "shares", "50")
        # self.assertRaises(TypeError, setattr, s, "shares", 50.0)
        with self.assertRaises(TypeError):
            s.shares = "50"
        with self.assertRaises(TypeError):
            s.shares = 50.0


if __name__ == "__main__":
    unittest.main()
