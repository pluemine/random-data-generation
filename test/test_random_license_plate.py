# Unit tests
import unittest
import re

from random_data_generation.license_plate import (
    format_license_plate,
    generate_weighted_list,
    generate_single_license_plate_sample,
)


class TestFormatLicensePlate(unittest.TestCase):

    def test_format_a(self):
        result = format_license_plate(
            prefix_type="a",
            prefix_num=9,
            prefix_alphabet="กก",
            number=1234,
            separator="",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "ก1234")

    def test_format_aa_space(self):
        result = format_license_plate(
            prefix_type="aa",
            prefix_num=9,
            prefix_alphabet="กก",
            number=1234,
            separator=" ",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "กก 1234")

    def test_format_1a_hyphen(self):
        result = format_license_plate(
            prefix_type="1a",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator="-",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "9ก-123")

    def test_format_1aa_no_space(self):
        result = format_license_plate(
            prefix_type="1aa",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator="",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "9กก123")

    def test_format_1aa_no_space_thai(self):
        result = format_license_plate(
            prefix_type="1aa",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator="",
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๙กก๑๒๓")

    def test_format_1a_hyphen_thai(self):
        result = format_license_plate(
            prefix_type="1a",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator="-",
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๙ก-๑๒๓")

    def test_format_aa_space_thai(self):
        result = format_license_plate(
            prefix_type="aa",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator=" ",
            use_thai_numeral=True,
        )
        self.assertEqual(result, "กก ๑๒๓")

    def test_format_a_space_thai(self):
        result = format_license_plate(
            prefix_type="a",
            prefix_num=9,
            prefix_alphabet="กก",
            number=123,
            separator=" ",
            use_thai_numeral=True,
        )
        self.assertEqual(result, "ก ๑๒๓")

    def test_weighted_list(self):
        result = generate_weighted_list(["A", "B", "C"], [3, 1, 2])
        self.assertEqual(result, ["A", "A", "A", "B", "C", "C"])

    def test_generate_single_license_plate_sample(self):
        result = generate_single_license_plate_sample(
            prefix_type_weighted=generate_weighted_list(
                ["a", "aa", "1a", "1aa"], [1, 0, 0, 0]
            ),
            separator_weighted=generate_weighted_list(["-", " ", ""], [1, 0, 0]),
            use_thai_numeral_weighted=generate_weighted_list([True, False], [0, 1]),
        )
        thai_alphabet_regex = re.compile(r"[ก-ฮ]")
        thai_alphabets = thai_alphabet_regex.findall(result)
        self.assertEqual(
            len(thai_alphabets),
            1,
            "Result should contain exactly one Thai alphabet character.",
        )

        num_part = result.split("-")[-1]  # Get the part after the separator
        arabic_numerals_regex = re.compile(r"^[0-9]{1,4}$")
        self.assertTrue(
            arabic_numerals_regex.match(num_part),
            "The part after the separator should be a number with 1 to 4 Arabic digits.",
        )

        self.assertLessEqual(
            len(result), 6, "The length of the result should be less than 6 characters."
        )


if __name__ == "__main__":
    unittest.main()
