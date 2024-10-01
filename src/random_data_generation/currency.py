import random
from .constants import (
    ARABIC_DIGITS,
    THAI_DIGITS,
    CURRENCIES,
    CURRENCY_MAX_AMOUNT,
    CURRENCY_CHOICES,
    CURRENCY_WEIGHTS,
    CURRENCY_USE_DASH_WEIGHTS,
    CURRENCY_USE_THAI_NUMERAL_WEIGHTS,
    CURRENCY_USE_SUFFIX_WEIGHTS,
    CURRENCY_SUFFIX_TH_WEIGHTS,
)
from .generate_weighted_list import generate_weighted_list

# Pre-compute translation table
THAI_TRANSLATION_TABLE = str.maketrans(ARABIC_DIGITS, THAI_DIGITS)


def format_currency(
    amount,
    currency,
    use_symbol=False,
    use_comma=False,
    show_cents=False,
    use_dash=False,
    use_space=False,
    use_thai_numeral=False,
    use_suffix=False,
    suffix_th=False,
):
    """
    Formats a given amount of money according to specified currency formatting options.

    Args:
        amount (float): The amount of money to format.
        currency (str): The currency code (e.g., "USD", "THB").
        use_symbol (bool): Whether to use the currency symbol instead of the code.
        use_comma (bool): Whether to use commas for thousands separators.
        show_cents (bool): Whether to show decimal places (cents).
        use_dash (bool): Whether to append a dash after the amount.
        use_space (bool): Whether to include a space between the amount and the currency.
        use_thai_numeral (bool): Whether to use Thai numerals (only applies to THB).
        use_suffix (bool): Whether to add a currency suffix (e.g., "Baht").
        suffix_th (bool): Whether to use the Thai suffix ("บาท") instead of the English suffix ("Baht").

    Returns:
        str: The formatted currency string.
    """

    # Retrieve the currency symbol and code from the CURRENCIES dictionary
    symbol, code = CURRENCIES[currency]

    # Determine if the currency prefix should be a symbol or code, and skip for THB with suffix
    prefix = ""
    if not (use_suffix and currency == "THB"):
        prefix = symbol if use_symbol else code

    # Set decimal places (cents) based on currency, with 0 decimals for JPY
    decimals = 0 if currency == "JPY" else (2 if show_cents else 0)

    # Format the amount with or without commas for thousands separators
    amount_str = f"{amount:,.{decimals}f}" if use_comma else f"{amount:.{decimals}f}"

    # Convert digits to Thai numerals if applicable
    if use_thai_numeral and currency == "THB":
        amount_str = amount_str.translate(THAI_TRANSLATION_TABLE)

    if use_dash:
        amount_str += ".-"

    # Determine the suffix for THB currency, either in English or Thai
    suffix = ""
    if use_suffix and currency == "THB":
        suffix = "บาท" if suffix_th else "Baht"

    if use_space:
        return f"{prefix} {amount_str} {suffix}".strip()
    return f"{prefix}{amount_str}{suffix}".strip()


def generate_single_currency_sample(
    currency_weighted,
    use_dash_weighted,
    use_thai_numeral_weighted,
    use_suffix_weighted,
    suffix_th_weighted,
):
    """
    Generates a single formatted currency sample with random values.

    Args:
        currency_weighted (list): A list of currency codes, weighted by their probabilities.
        use_dash_weighted (list): A list of boolean values indicating whether to use a dash, weighted by their probabilities.
        use_thai_numeral_weighted (list): A list of boolean values indicating whether to use Thai numerals, weighted by their probabilities.
        use_suffix_weighted (list): A list of boolean values indicating whether to use a currency suffix, weighted by their probabilities.
        suffix_th_weighted (list): A list of boolean values indicating whether to use the Thai suffix ("บาท") instead of the English suffix ("Baht"), weighted by their probabilities.

    Returns:
        str: A randomly generated formatted currency string based on the given weights and random selections.
    """

    # Randomly select currency and generate random formatting options
    currency = currency_weighted[int(random.random() * len(currency_weighted))]
    amount = random.random() * CURRENCY_MAX_AMOUNT
    use_symbol = random.random() < 0.5
    use_comma = random.random() < 0.5
    show_cents = random.random() < 0.5
    use_dash = use_dash_weighted[int(random.random() * len(use_dash_weighted))]
    use_space = random.random() < 0.5

    # Specific random options for THB currency
    use_thai_numeral = (
        use_thai_numeral_weighted[int(random.random() * len(use_thai_numeral_weighted))]
        if currency == "THB"
        else False
    )
    use_suffix = (
        use_suffix_weighted[int(random.random() * len(use_suffix_weighted))]
        if currency == "THB"
        else False
    )
    suffix_th = (
        suffix_th_weighted[int(random.random() * len(suffix_th_weighted))]
        if currency == "THB"
        else False
    )

    # Generate formatted currency
    formatted_currency = format_currency(
        amount,
        currency,
        use_symbol,
        use_comma,
        show_cents,
        use_dash,
        use_space,
        use_thai_numeral,
        use_suffix,
        suffix_th,
    )
    return formatted_currency


def generate_currencies(number_of_generated_sample):
    """
    Generates a specified number of currency samples and writes them to a file.

    Args:
        number_of_generated_sample (int): The number of currency samples to generate.

    Returns:
        set: A set containing unique generated currency samples.
    """

    # Precompute weighted lists for efficient sampling
    currency_weighted = generate_weighted_list(CURRENCY_CHOICES, CURRENCY_WEIGHTS)
    use_dash_weighted = generate_weighted_list([True, False], CURRENCY_USE_DASH_WEIGHTS)
    use_thai_numeral_weighted = generate_weighted_list(
        [True, False], CURRENCY_USE_THAI_NUMERAL_WEIGHTS
    )
    use_suffix_weighted = generate_weighted_list(
        [True, False], CURRENCY_USE_SUFFIX_WEIGHTS
    )
    suffix_th_weighted = generate_weighted_list(
        [True, False], CURRENCY_SUFFIX_TH_WEIGHTS
    )

    # Generate unique currency samples
    output = set()
    while len(output) < number_of_generated_sample:
        output.add(
            generate_single_currency_sample(
                currency_weighted,
                use_dash_weighted,
                use_thai_numeral_weighted,
                use_suffix_weighted,
                suffix_th_weighted,
            )
        )

    return output
