"""CLI for deterministic invoice app."""

from apps.deterministic_invoice.service import calculate_quote


if __name__ == "__main__":
    quote = calculate_quote(120.0, 0.10, "SAVE10", "standard")
    print(quote)
