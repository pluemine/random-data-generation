import argparse
import os
import time

from random_data_generation.currency import generate_currencies
from random_data_generation.numeric import generate_numerics
from random_data_generation.date import generate_dates
from random_data_generation.phone_number import generate_phone_numbers
from random_data_generation.license_plate import generate_license_plates


def create_output_dir(base_path, data_type):
    """
    Creates an output directory and file path for saving generated data.

    Args:
        base_path (str): The base output directory path.
        data_type (str): The type of data being generated (e.g., "currency").

    Returns:
        str: The full path to the file where data will be saved.
    """

    filename = f"{data_type}.txt"
    output_path = os.path.join(base_path, filename)

    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    return output_path


def write_to_file(data, file_path):
    """
    Writes the generated data to a file.

    Args:
        data (list): The data to be written to the file.
        file_path (str): The path to the file where data will be written.
    """

    content = "\n".join(map(str, data))

    with open(file_path, "w") as f:
        f.write(content)


def main():
    """
    Main function to parse arguments, generate data, and save it to a file.
    """

    start_time = time.perf_counter()

    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Generate random formatted data such as currencies, numerics, dates, license plates, or phone numbers."
    )
    parser.add_argument(
        "--type",
        type=str,
        help="Type to execute (e.g., 'currency, numeric, date, license_plate, phone_number')",
    )
    parser.add_argument(
        "--number",
        type=int,
        default=250000,
        help="Number of entires to generate (default: 250000)",
    )
    parser.add_argument("--output", type=str, help="Path to the output directory")

    args = parser.parse_args()

    generated_type = args.type
    number_of_generated_sample = args.number
    output_path = args.output

    # Generate data based on specified type
    data_generators = {
        "currency": generate_currencies,
        "numeric": generate_numerics,
        "date": generate_dates,
        "phone_number": generate_phone_numbers,
        "license_plate": generate_license_plates,
    }

    # Validate arguments
    assert generated_type in data_generators, f"Unknown data type: {generated_type}"
    assert number_of_generated_sample >= 0, "Number of entries must be non-negative"

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)

    file_path = create_output_dir(output_path, generated_type)
    result = data_generators[generated_type](number_of_generated_sample)
    write_to_file(result, file_path)

    # Measure processing time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Processing completed in {elapsed_time:.2f} seconds.")


if __name__ == "__main__":
    main()
