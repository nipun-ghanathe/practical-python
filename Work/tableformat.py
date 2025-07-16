# tableformat.py
#
# Exercise 4.5

from stock import Stock


class TableFormatter:
    def headings(self, headers):
        """Emit the table headings."""
        raise NotImplementedError

    def row(self, rowdaata):
        """Emit a single row of table data."""
        raise NotImplementedError


class TextTableFormatter(TableFormatter):
    """Emit a table in plain-text format."""

    def headings(self, headers: list[str]) -> None:
        print(" ".join(f"{header:>10s}" for header in headers))
        print(" ".join("-" * 10 for _ in headers))

    def row(self, rowdata: list[str]) -> None:
        print(" ".join(f"{value:>10s}" for value in rowdata))


class CSVTableFormatter(TableFormatter):
    """Emit a table in CSV format."""

    def headings(self, headers: list[str]) -> None:
        print(",".join(headers))

    def row(self, rowdata: list[str]) -> None:
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    """Emit a table in HTML format."""

    def headings(self, headers: list[str]) -> None:
        print("<tr><th>" + "</th><th>".join(headers) + "</th></tr>")

    def row(self, rowdata: list[str]) -> None:
        print("<tr><td>" + "</td><td>".join(rowdata) + "</td></tr>")


class FormatError(Exception):
    pass


def create_formatter(fmt: str = "txt") -> TableFormatter:
    """Return appropriate TableFormatter for given format."""
    match fmt.lower():
        case "txt":
            return TextTableFormatter()
        case "csv":
            return CSVTableFormatter()
        case "html":
            return HTMLTableFormatter()
        case _:
            message = f"Unknow table format: {fmt}"
            raise FormatError(message)


def print_table(
    portfolio: list[Stock],
    select: list[str],
    formatter: TableFormatter,
) -> None:
    formatter.headings(select)
    for stock in portfolio:
        formatter.row(map(str, (getattr(stock, attr) for attr in select)))
