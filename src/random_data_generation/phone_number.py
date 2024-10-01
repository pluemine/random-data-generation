import random
from .constants import (
    ARABIC_DIGITS,
    THAI_DIGITS,
    PHONE_NUMBER_MAX_LENGTH,
    PHONE_MIN_DIGIT,
    PHONE_MAX_DIGIT,
    PHONE_CHOICES,
    PHONE_WEIGHTS,
    PHONE_HOME_PREFIX_CHOICES,
    PHONE_HOME_PREFIX_WEIGHTS,
    PHONE_MOBILE_PREFIX_CHOICES,
    PHONE_MOBILE_PREFIX_WEIGHTS,
    PHONE_INTER_PREFIX_WEIGHTS,
    PHONE_SEPARATOR_CHOICES,
    PHONE_SEPARATOR_WEIGHTS,
    PHONE_FORMAT_CHOICES,
    PHONE_FORMAT_WEIGHTS,
    PHONE_USE_THAI_NUMERAL_WEIGHTS,
)
from .generate_weighted_list import generate_weighted_list

# Pre-compute translation table
THAI_TRANSLATION_TABLE = str.maketrans(ARABIC_DIGITS, THAI_DIGITS)


def format_phone_number(
    phone_type,
    home_prefix,
    mobile_prefix,
    number,
    international_prefix=False,
    separator="",
    format="xxx-xxx-xxxx",
    use_thai_numeral=False,
):
    """
    Formats a phone number according to specified options.

    Args:
        phone_type (str): Type of phone number, (e.g., "home" or "mobile").
        home_prefix (str): Prefix for home phone numbers.
        mobile_prefix (str): Prefix for mobile phone numbers.
        number (str): The numeric part of the phone number.
        international_prefix (bool): Whether to include the international dialing code.
        separator (str): Separator character(s) between number groups.
        format (str): The format of the phone number.
        use_thai_numeral (bool): Whether to use Thai numerals.

    Returns:
        str: The formatted phone number string.
    """

    if international_prefix:
        inter_prefix = "+66"
    else:
        inter_prefix = "0"

    if phone_type == "home":
        phone_prefix_1 = f"{home_prefix}"
        phone_prefix_2 = ""
        number_group1 = number[:3]
        number_group2 = number[3:7]
    else:
        phone_prefix_1 = f"{mobile_prefix}"
        phone_prefix_2 = f"{number[0]}"
        number_group1 = number[1:4]
        number_group2 = number[4:8]

    if format == "xxx-xxx-xxxx":
        phone_format = f"{inter_prefix}{phone_prefix_1}{phone_prefix_2}{separator}{number_group1}{separator}{number_group2}"
    elif format == "xxxxxx-xxxx":
        phone_format = f"{inter_prefix}{phone_prefix_1}{phone_prefix_2}{number_group1}{separator}{number_group2}"
    else:
        phone_format = f"{inter_prefix}{phone_prefix_1}{separator}{phone_prefix_2}{number_group1}{separator}{number_group2}"

    # Convert digits to Thai numerals if applicable
    if use_thai_numeral:
        phone_format = phone_format.translate(THAI_TRANSLATION_TABLE)

    return phone_format


def generate_single_phone_number_sample(
    phone_type_weighted,
    home_prefix_weighted,
    mobile_prefix_weighted,
    international_prefix_weighted,
    separator_weighted,
    format_weighted,
    use_thai_numeral_weighted,
):
    """
    Generates a single formatted phone number sample with random values for options.

    Args:
        phone_type_weighted (list): A list of phone type choices, weighted by their probabilities.
        home_prefix_weighted (list): A list of home prefix choices, weighted by their probabilities.
        mobile_prefix_weighted (list): A list of mobile prefix choices, weighted by their probabilities.
        international_prefix_weighted (list): A list of boolean values indicating whether to include an international prefix, weighted by their probabilities.
        separator_weighted (list): A list of separator choices, weighted by their probabilities.
        format_weighted (list): A list of phone number format choices, weighted by their probabilities.
        use_thai_numeral_weighted (list): A list of boolean values indicating whether to use Thai numerals, weighted by their probabilities.

    Returns:
        str: A randomly generated formatted phone number based on the given weights and random selections.
    """

    # Randomly select number and generate random formatting options
    phone_type = phone_type_weighted[int(random.random() * len(phone_type_weighted))]
    home_prefix = home_prefix_weighted[int(random.random() * len(home_prefix_weighted))]
    mobile_prefix = mobile_prefix_weighted[
        int(random.random() * len(mobile_prefix_weighted))
    ]
    number_length = PHONE_NUMBER_MAX_LENGTH
    number = "".join(
        [
            str(
                int(random.random() * (PHONE_MAX_DIGIT - PHONE_MIN_DIGIT + 1))
                + PHONE_MIN_DIGIT
            )
            for _ in range(number_length)
        ]
    )
    international_prefix = international_prefix_weighted[
        int(random.random() * len(international_prefix_weighted))
    ]
    separator = separator_weighted[int(random.random() * len(separator_weighted))]
    format = format_weighted[int(random.random() * len(format_weighted))]
    use_thai_numeral = use_thai_numeral_weighted[
        int(random.random() * len(use_thai_numeral_weighted))
    ]

    # Generate formatted phone number
    formatted_phone_number = format_phone_number(
        phone_type,
        home_prefix,
        mobile_prefix,
        number,
        international_prefix,
        separator,
        format,
        use_thai_numeral,
    )

    return formatted_phone_number


def generate_phone_numbers(number_of_generated_sample):
    """
    Generates a specified number of phone number samples.

    Args:
        number_of_generated_sample (int): The number of phone number samples to generate.

    Returns:
        set: A set containing unique generated phone number samples.
    """

    # Precompute weighted lists for efficient sampling
    phone_type_weighted = generate_weighted_list(PHONE_CHOICES, PHONE_WEIGHTS)
    home_prefix_weighted = generate_weighted_list(
        PHONE_HOME_PREFIX_CHOICES, PHONE_HOME_PREFIX_WEIGHTS
    )
    mobile_prefix_weighted = generate_weighted_list(
        PHONE_MOBILE_PREFIX_CHOICES, PHONE_MOBILE_PREFIX_WEIGHTS
    )
    international_prefix_weighted = generate_weighted_list(
        [True, False], PHONE_INTER_PREFIX_WEIGHTS
    )
    separator_weighted = generate_weighted_list(
        PHONE_SEPARATOR_CHOICES, PHONE_SEPARATOR_WEIGHTS
    )
    format_weighted = generate_weighted_list(PHONE_FORMAT_CHOICES, PHONE_FORMAT_WEIGHTS)
    use_thai_numeral_weighted = generate_weighted_list(
        [True, False], PHONE_USE_THAI_NUMERAL_WEIGHTS
    )

    # Generate unique phone number samples
    output = set()
    while len(output) < number_of_generated_sample:
        output.add(
            generate_single_phone_number_sample(
                phone_type_weighted,
                home_prefix_weighted,
                mobile_prefix_weighted,
                international_prefix_weighted,
                separator_weighted,
                format_weighted,
                use_thai_numeral_weighted,
            )
        )

    return output
