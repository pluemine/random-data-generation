import random
from .constants import (
    ARABIC_DIGITS,
    THAI_DIGITS,
    NUMERIC_MAX_AMOUNT,
    NUMERIC_USE_THAI_NUMERAL_WEIGHTS,
)
from .generate_weighted_list import generate_weighted_list

# Pre-compute translation table
THAI_TRANSLATION_TABLE = str.maketrans(ARABIC_DIGITS, THAI_DIGITS)


def format_numeric(amount, use_comma=True, show_decimal=False, use_thai_numeral=False):
    """
    Formats a numeric amount according to specified formatting options.

    Args:
        amount (float): The numeric value to format.
        use_comma (bool): Whether to use commas for thousands separators.
        show_decimal (bool): Whether to show decimal places.
        use_thai_numeral (bool): Whether to use Thai numerals.

    Returns:
        str: The formatted numeric string.
    """

    # Set the number of decimal places based on whether to show decimal values
    decimals = 2 if show_decimal else 0

    # Format the amount with or without commas for thousands separators
    amount_str = f"{amount:,.{decimals}f}" if use_comma else f"{amount:.{decimals}f}"

    # Convert digits to Thai numerals if applicable
    if use_thai_numeral:
        amount_str = amount_str.translate(THAI_TRANSLATION_TABLE)

    return amount_str


def generate_single_numeric_sample(use_thai_numeral_weighted):
    """
    Generates a single formatted numeric sample with random values for formatting options.

    Args:
        use_thai_numeral_weighted (list): A list of boolean values indicating whether to use Thai numerals, weighted by their probabilities.

    Returns:
        str: A randomly generated formatted numeric string based on the given weights and random selections.
    """

    # Randomly select amount and generate random formatting options
    amount = random.random() * NUMERIC_MAX_AMOUNT
    use_comma = random.random() < 0.5
    show_decimal = random.random() < 0.5
    use_thai_numeral = use_thai_numeral_weighted[
        int(random.random() * len(use_thai_numeral_weighted))
    ]

    # Generate formatted numeric
    formatted_numeric = format_numeric(
        amount, use_comma, show_decimal, use_thai_numeral
    )
    return formatted_numeric


def generate_numerics(number_of_generated_sample):
    """
    Generates a specified number of numeric samples and writes them to a file.

    Args:
        number_of_generated_sample (int): The number of numeric samples to generate.

    Returns:
        set: A set containing unique generated numeric samples.
    """

    # Precompute weighted lists for efficient sampling
    use_thai_numeral_weighted = generate_weighted_list(
        [True, False], NUMERIC_USE_THAI_NUMERAL_WEIGHTS
    )

    # Generate unique numeric samples
    output = set()
    while len(output) < number_of_generated_sample:
        output.add(generate_single_numeric_sample(use_thai_numeral_weighted))

    return output
