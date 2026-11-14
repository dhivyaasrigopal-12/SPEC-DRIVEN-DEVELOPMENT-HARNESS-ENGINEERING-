from decimal import Decimal, ROUND_HALF_UP


VALID_DISCOUNTS = {
    "SAVE10": Decimal("0.10"),
    "VIP15": Decimal("0.15"),
}


def _round_money(value: Decimal) -> Decimal:
    return value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def calculate_quote(subtotal: float, tax_rate: float, discount_code: str | None = None, shipping_option: str | None = None) -> dict:
    """Return a deterministic invoice quote based on the specification."""
    subtotal_decimal = Decimal(str(subtotal))
    tax_decimal = Decimal(str(tax_rate))

    if subtotal_decimal < 0:
        raise ValueError("subtotal must be non-negative")
    if tax_decimal < 0 or tax_decimal > 1:
        raise ValueError("tax_rate must be between 0 and 1 inclusive")

    discount_rate = Decimal("0")
    if discount_code:
        normalized = discount_code.strip().upper()
        discount_rate = VALID_DISCOUNTS.get(normalized, Decimal("0"))

    discount_amount = subtotal_decimal * discount_rate
    discounted_subtotal = subtotal_decimal - discount_amount
    tax_amount = discounted_subtotal * tax_decimal

    if shipping_option and shipping_option.strip().lower() == "free":
        shipping_amount = Decimal("0")
    elif subtotal_decimal >= Decimal("100"):
        shipping_amount = Decimal("0")
    else:
        shipping_amount = Decimal("10")

    total = discounted_subtotal + tax_amount + shipping_amount

    return {
        "subtotal": float(_round_money(subtotal_decimal)),
        "discount_rate": float(_round_money(discount_rate)),
        "discount_amount": float(_round_money(discount_amount)),
        "tax_amount": float(_round_money(tax_amount)),
        "shipping_amount": float(_round_money(shipping_amount)),
        "total": float(_round_money(total)),
    }


if __name__ == "__main__":
    print(calculate_quote(120, 0.1, "SAVE10", "standard"))
