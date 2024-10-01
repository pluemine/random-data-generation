import random
from .constants import (
    ARABIC_DIGITS,
    THAI_DIGITS,
    THAI_ALPHABETS,
    LICENSE_CHOICES,
    LICENSE_WEIGHTS,
    LICENSE_MIN_PREFIX_NUM,
    LICENSE_MAX_PREFIX_NUM,
    LICENSE_MIN_NUMBER,
    LICENSE_MAX_NUMBER,
    LICENSE_SEPARATOR_CHOICES,
    LICENSE_SEPARATOR_WEIGHTS,
    LICENSE_USE_THAI_NUMERAL_WEIGHTS,
)
from .generate_weighted_list import generate_weighted_list

# Pre-compute translation table
THAI_TRANSLATION_TABLE = str.maketrans(ARABIC_DIGITS, THAI_DIGITS)


def format_license_plate(
    prefix_type,
    prefix_num,
    prefix_alphabet,
    number,
    separator="",
    use_thai_numeral=False,
):
    """
    Formats a license plate according to specified formatting options.

    Args:
        prefix_type (str): The type of prefix (e.g., "a", "aa", "1a").
        prefix_num (int): The numeric part of the prefix.
        prefix_alphabet (str): The alphabetic part of the prefix.
        number (int): The number to appear on the license plate.
        separator (str): The separator to use between the prefix and the number.
        use_thai_numeral (bool): Whether to use Thai numerals.

    Returns:
        str: The formatted license plate string.
    """

    if prefix_type == "a":
        prefix = f"{prefix_alphabet[0]}"
    elif prefix_type == "aa":
        prefix = prefix_alphabet
    elif prefix_type == "1a":
        if use_thai_numeral:
            prefix = f"{THAI_DIGITS[int(prefix_num)]}{prefix_alphabet[0]}"
        else:
            prefix = f"{prefix_num}{prefix_alphabet[0]}"
    else:
        if use_thai_numeral:
            prefix = f"{THAI_DIGITS[int(prefix_num)]}{prefix_alphabet}"
        else:
            prefix = f"{prefix_num}{prefix_alphabet}"

    number_str = f"{number}"

    # Convert digits to Thai numerals if applicable
    if use_thai_numeral:
        number_str = number_str.translate(THAI_TRANSLATION_TABLE)

    return f"{prefix}{separator}{number_str}"


def generate_single_license_plate_sample(
    prefix_type_weighted, separator_weighted, use_thai_numeral_weighted
):
    """
    Generates a single formatted license plate sample with random values for formatting options.

    Args:
        prefix_type_weighted (list): A list of prefix types, weighted by their probabilities.
        separator_weighted (list): A list of separators, weighted by their probabilities.
        use_thai_numeral_weighted (list): A list of boolean values indicating whether to use Thai numerals, weighted by their probabilities.

    Returns:
        str: A randomly generated formatted license plate string based on the given weights and random selections.
    """

    # Randomly select number and generate random formatting options
    prefix_type = prefix_type_weighted[int(random.random() * len(prefix_type_weighted))]
    prefix_num = (
        int(random.random() * (LICENSE_MAX_PREFIX_NUM - LICENSE_MIN_PREFIX_NUM + 1))
        + LICENSE_MIN_PREFIX_NUM
    )
    prefix_alphabet = "".join(random.sample(THAI_ALPHABETS, 2))
    number = (
        int(random.random() * (LICENSE_MAX_NUMBER - LICENSE_MIN_NUMBER + 1))
        + LICENSE_MIN_NUMBER
    )
    separator = separator_weighted[int(random.random() * len(separator_weighted))]
    use_thai_numeral = use_thai_numeral_weighted[
        int(random.random() * len(use_thai_numeral_weighted))
    ]

    # Generate formatted license plate
    formatted_license_plate = format_license_plate(
        prefix_type=prefix_type,
        prefix_num=prefix_num,
        prefix_alphabet=prefix_alphabet,
        number=number,
        separator=separator,
        use_thai_numeral=use_thai_numeral,
    )
    return formatted_license_plate


def generate_license_plates(number_of_generated_sample):
    """
    Generates a specified number of license plate samples.

    Args:
        number_of_generated_sample (int): The number of license plate samples to generate.

    Returns:
        set: A set containing unique generated license plate samples.
    """

    # Precompute weighted lists for efficient sampling
    prefix_type_weighted = generate_weighted_list(LICENSE_CHOICES, LICENSE_WEIGHTS)
    separator_weighted = generate_weighted_list(
        LICENSE_SEPARATOR_CHOICES, LICENSE_SEPARATOR_WEIGHTS
    )
    use_thai_numeral_weighted = generate_weighted_list(
        [True, False], LICENSE_USE_THAI_NUMERAL_WEIGHTS
    )

    # Generate unique license plates samples
    output = set()
    while len(output) < number_of_generated_sample:
        output.add(
            generate_single_license_plate_sample(
                prefix_type_weighted, separator_weighted, use_thai_numeral_weighted
            )
        )

    return output
