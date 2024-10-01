import random
from datetime import datetime, timedelta
from .constants import (
    ARABIC_DIGITS,
    THAI_DIGITS,
    MONTH_NAMES_TH,
    MONTH_ABBRS_TH,
    MONTH_NAMES_EN,
    MONTH_ABBRS_EN,
    DATE_START_DATE,
    DATE_END_DATE,
    DATE_FORMAT_CHOICES,
    DATE_FORMAT_WEIGHTS,
    DATE_YEAR_TYPE_CHOICES,
    DATE_YEAR_TYPE_WEIGHTS,
    DATE_YEAR_DIGIT_CHOICES,
    DATE_YEAR_DIGIT_WEIGHTS,
    DATE_MONTH_LANG_THAI_WEIGHTS,
    DATE_FULL_MONTH_WEIGHTS,
    DATE_DATE_FORMAT_CHOICES,
    DATE_DATE_FORMAT_WEIGHTS,
    DATE_SEPARATOR_CHOICES,
    DATE_SEPARATOR_WEIGHTS,
    DATE_USE_THAI_NUMERAL_WEIGHTS,
)
from .generate_weighted_list import generate_weighted_list

# Pre-compute translation table
THAI_TRANSLATION_TABLE = str.maketrans(ARABIC_DIGITS, THAI_DIGITS)


def format_date(
    date,
    format="DD/MM/YYYY",
    year_type="ad",
    year_digit=4,
    month_lang_thai=False,
    full_month=False,
    date_format=2,
    separator="/",
    use_thai_numeral=False,
):
    """
    Formats a date according to specified formatting options.

    Args:
        date (datetime): The datetime object to format.
        format (str): The format of the date string.
        year_type (str): The year type (e.g., "ad" or "be").
        year_digit (int): Number of digits to show for the year.
        month_lang_thai (bool): Whether to use Thai month names.
        full_month (bool): Whether to use full month names or abbreviations.
        date_format (int): The format of day and month (e.g., 1 for single digit, 2 for double digit).
        separator (str): The separator between date components.
        use_thai_numeral (bool): Whether to use Thai numerals.

    Returns:
        str: The formatted date string.
    """

    # Select month names and abbreviations based on language preference
    month_name = (
        MONTH_NAMES_TH[date.month - 1]
        if month_lang_thai
        else MONTH_NAMES_EN[date.month - 1]
    )
    month_abbr = (
        MONTH_ABBRS_TH[date.month - 1]
        if month_lang_thai
        else MONTH_ABBRS_EN[date.month - 1]
    )
    month_name_thai = MONTH_NAMES_TH[date.month - 1]

    # Determine the year format
    year = date.year + 543 if year_type == "be" else date.year
    year_str = str(year)[-year_digit:]  # Get last `year_digit` digits
    year_type_abbr = "พ.ศ." if year_type == "be" else "ค.ศ."

    # Format day and month
    day = f"{date.day:02}" if date_format == 2 else str(date.day)
    month = f"{date.month:02}" if date_format == 2 else str(date.month)
    month_name_display = month_name if full_month else month_abbr

    # Format the date according to the specified format
    if format == "DD/MM/YYYY":
        formatted_date = f"{day}{separator}{month}{separator}{year_str}"
    elif format == "MM/DD/YYYY":
        formatted_date = f"{month}{separator}{day}{separator}{year_str}"
    elif format == "YYYY/MM/DD":
        formatted_date = f"{year_str}{separator}{month}{separator}{day}"
    elif format == "YYYY/DD/MM":
        formatted_date = f"{year_str}{separator}{day}{separator}{month}"
    elif format == "DD/Month/YYYY":
        formatted_date = f"{day}{separator}{month_name_display}{separator}{year_str}"
    elif format == "Month DD, YYYY":
        formatted_date = f"{month_name_display} {day}, {year_str}"
    else:
        formatted_date = f"{day} {month_name_thai} {year_type_abbr} {year_str}"

    # Convert digits to Thai numerals if needed
    if use_thai_numeral:
        formatted_date = formatted_date.translate(THAI_TRANSLATION_TABLE)

    return formatted_date


def random_date(start, end):
    """
    Generates a random date between start and end dates.

    Args:
        start (datetime): The start date.
        end (datetime): The end date.

    Returns:
        datetime: A randomly generated date between start and end dates.
    """

    return start + timedelta(days=random.randint(0, (end - start).days))


def generate_single_date_sample(
    format_weighted,
    year_type_weighted,
    year_digit_weighted,
    month_lang_thai_weighted,
    full_month_weighted,
    date_format_weighted,
    separator_weighted,
    use_thai_numeral_weighted,
):
    """
    Generates a single formatted date sample with random values for formatting options.

    Args:
        format_weighted (list): A list of date formats, weighted by their probabilities.
        year_type_weighted (list): A list of year types, weighted by their probabilities.
        year_digit_weighted (list): A list of year digit options, weighted by their probabilities.
        month_lang_thai_weighted (list): A list of boolean values indicating whether to use Thai month names, weighted by their probabilities.
        full_month_weighted (list): A list of boolean values indicating whether to use full month names, weighted by their probabilities.
        date_format_weighted (list): A list of date formats for day and month, weighted by their probabilities.
        separator_weighted (list): A list of separators, weighted by their probabilities.
        use_thai_numeral_weighted (list): A list of boolean values indicating whether to use Thai numerals, weighted by their probabilities.

    Returns:
        str: A randomly generated formatted date string based on the given weights and random selections.
    """

    start_date = datetime(*DATE_START_DATE)
    end_date = datetime(*DATE_END_DATE)
    date = random_date(start_date, end_date)
    format = format_weighted[int(random.random() * len(format_weighted))]
    year_type = year_type_weighted[int(random.random() * len(year_type_weighted))]
    year_digit = year_digit_weighted[int(random.random() * len(year_digit_weighted))]
    month_lang_thai = month_lang_thai_weighted[
        int(random.random() * len(month_lang_thai_weighted))
    ]
    full_month = full_month_weighted[int(random.random() * len(full_month_weighted))]
    date_format = date_format_weighted[int(random.random() * len(date_format_weighted))]
    separator = separator_weighted[int(random.random() * len(separator_weighted))]
    use_thai_numeral = use_thai_numeral_weighted[
        int(random.random() * len(use_thai_numeral_weighted))
    ]

    # Generate formatted date
    formatted_date = format_date(
        date,
        format,
        year_type,
        year_digit,
        month_lang_thai,
        full_month,
        date_format,
        separator,
        use_thai_numeral,
    )

    return formatted_date


def generate_dates(number_of_generated_sample):
    """
    Generates a specified number of date samples and writes them to a file.

    Args:
        number_of_generated_sample (int): The number of date samples to generate.

    Returns:
        set: A set containing unique generated date samples.
    """

    # Precompute weighted lists for efficient sampling
    format_weighted = generate_weighted_list(DATE_FORMAT_CHOICES, DATE_FORMAT_WEIGHTS)
    year_type_weighted = generate_weighted_list(
        DATE_YEAR_TYPE_CHOICES, DATE_YEAR_TYPE_WEIGHTS
    )
    year_digit_weighted = generate_weighted_list(
        DATE_YEAR_DIGIT_CHOICES, DATE_YEAR_DIGIT_WEIGHTS
    )
    month_lang_thai_weighted = generate_weighted_list(
        [True, False], DATE_MONTH_LANG_THAI_WEIGHTS
    )
    full_month_weighted = generate_weighted_list([True, False], DATE_FULL_MONTH_WEIGHTS)
    date_format_weighted = generate_weighted_list(
        DATE_DATE_FORMAT_CHOICES, DATE_DATE_FORMAT_WEIGHTS
    )
    separator_weighted = generate_weighted_list(
        DATE_SEPARATOR_CHOICES, DATE_SEPARATOR_WEIGHTS
    )
    use_thai_numeral_weighted = generate_weighted_list(
        [True, False], DATE_USE_THAI_NUMERAL_WEIGHTS
    )

    # Generate unique date samples
    output = set()
    while len(output) < number_of_generated_sample:
        output.add(
            generate_single_date_sample(
                format_weighted,
                year_type_weighted,
                year_digit_weighted,
                month_lang_thai_weighted,
                full_month_weighted,
                date_format_weighted,
                separator_weighted,
                use_thai_numeral_weighted,
            )
        )

    return output
