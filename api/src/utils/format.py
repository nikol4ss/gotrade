def format_money(value: float) -> str:
    """Format to US dollar currency format.

    Parameters:
        value (float): Numeric value to be formatted.

    Returns:
        str: Formatted string (e.g., 1234.5 -> '$1,234.50').
    """
    return f"${value:,.2f}"


def format_number_short(number: float) -> str:
    """Format the number into a short sequence of values.

    Parameters:
        number (float): Float value for format.

    Returns:
        str: Short string (e.g., 1500 -> '$1.50K').
    """
    if number >= 1_000_000_000:
        return f"${number/1_000_000_000:.2f}B"
    elif number >= 1_000_000:
        return f"${number/1_000_000:.2f}M"
    elif number >= 1_000:
        return f"${number/1_000:.2f}K"
    else:
        return str(number)


def format_dollar_invert(value: str) -> str:
    """Invert dollar sign and negative sign.

    Parameters:
        value (str): Dollar string (e.g., '$-123.45' or '-$123.45').

    Returns:
        str: Inverted string (e.g., '$-123.45' -> '-$123.45').
    """
    if value.startswith("$-"):
        return "-$" + value[2:]
    elif value.startswith("-$"):
        return "$-" + value[2:]
    return value


def format_porcent(value: float) -> str:
    """Format a float as a percentage string.

    Parameters:
        value (float): Numeric value to format.

    Returns:
        str: Percentage string (e.g., 12.345 -> '%12.35').
    """
    return f"%{value:.2f}"
