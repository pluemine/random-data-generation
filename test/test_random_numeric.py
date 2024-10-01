# Unit tests
import unittest
import re

from random_data_generation.numeric import (
    format_numeric,
    generate_weighted_list,
    generate_single_numeric_sample,
)


class TestFormatNumeric(unittest.TestCase):

    def test_format_comma(self):
        result = format_numeric(
            1234.56,
            use_comma=True,
            show_decimal=True,
            use_thai_numeral=False,
        )
        self.assertEqual(result, "1,234.56")

    def test_format_no_comma(self):
        result = format_numeric(
            1234.56,
            use_comma=False,
            show_decimal=True,
            use_thai_numeral=False,
        )
        self.assertEqual(result, "1234.56")

    def test_format_no_decimal(self):
        result = format_numeric(
            1234.56,
            use_comma=False,
            show_decimal=False,
            use_thai_numeral=False,
        )
        self.assertEqual(result, "1235")

    def test_format_thai_numeral(self):
        result = format_numeric(
            1234.56,
            use_comma=False,
            show_decimal=False,
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๑๒๓๕")

    def test_format_thai_numeral_comma_no_decimal(self):
        result = format_numeric(
            1234.56,
            use_comma=True,
            show_decimal=False,
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๑,๒๓๕")

    def test_format_thai_numeral_comma_decimal(self):
        result = format_numeric(
            1234.56,
            use_comma=True,
            show_decimal=True,
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๑,๒๓๔.๕๖")

    def test_weighted_list(self):
        result = generate_weighted_list(["A", "B", "C"], [3, 1, 2])
        self.assertEqual(result, ["A", "A", "A", "B", "C", "C"])

    def test_generate_single_numeric_sample(self):
        result = generate_single_numeric_sample(
            use_thai_numeral_weighted=generate_weighted_list([True, False], [0, 1]),
        )
        self.assertIsNotNone(result, "The result is None")
        self.assertNotEqual(result, "", "The result is an empty string")
        arabic_numerals_pattern = re.compile(r"[0123456789]")
        self.assertTrue(
            arabic_numerals_pattern.search(result),
            "The result does not contain Arabic numerals",
        )

    def test_generate_single_numeric_sample_thai_numeral(self):
        result = generate_single_numeric_sample(
            use_thai_numeral_weighted=generate_weighted_list([True, False], [1, 0]),
        )
        self.assertIsNotNone(result, "The result is None")
        self.assertNotEqual(result, "", "The result is an empty string")
        thai_numerals_pattern = re.compile(r"[๐๑๒๓๔๕๖๗๘๙]")
        self.assertTrue(
            thai_numerals_pattern.search(result),
            "The result does not contain Thai numerals",
        )


if __name__ == "__main__":
    unittest.main()
