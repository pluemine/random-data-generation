# Unit tests
import unittest
import re

from random_data_generation.phone_number import (
    format_phone_number,
    generate_weighted_list,
    generate_single_phone_number_sample,
)


class TestFormatPhoneNumber(unittest.TestCase):

    def test_mobile_format_1(self):
        result = format_phone_number(
            phone_type="mobile",
            home_prefix="",
            mobile_prefix="9",
            number="0123456789",
            international_prefix=False,
            separator="-",
            format="xxx-xxx-xxxx",
        )
        self.assertEqual(result, "090-123-4567")

    def test_mobile_format_1_inter(self):
        result = format_phone_number(
            phone_type="mobile",
            home_prefix="",
            mobile_prefix="9",
            number="0123456789",
            international_prefix=True,
            separator="-",
            format="xxx-xxx-xxxx",
        )
        self.assertEqual(result, "+6690-123-4567")

    def test_mobile_format_1_space_inter(self):
        result = format_phone_number(
            phone_type="mobile",
            home_prefix="",
            mobile_prefix="9",
            number="0123456789",
            international_prefix=True,
            separator=" ",
            format="xxx-xxx-xxxx",
        )
        self.assertEqual(result, "+6690 123 4567")

    def test_mobile_format_2_space_inter(self):
        result = format_phone_number(
            phone_type="mobile",
            home_prefix="",
            mobile_prefix="9",
            number="0123456789",
            international_prefix=True,
            separator=" ",
            format="xxxxxx-xxxx",
        )
        self.assertEqual(result, "+6690123 4567")

    def test_mobile_format_3_space(self):
        result = format_phone_number(
            phone_type="mobile",
            home_prefix="",
            mobile_prefix="9",
            number="0123456789",
            international_prefix=False,
            separator=" ",
            format="xx-xxxx-xxxx",
        )
        self.assertEqual(result, "09 0123 4567")

    def test_home_format_1(self):
        result = format_phone_number(
            phone_type="home",
            home_prefix="2",
            mobile_prefix="",
            number="0123456789",
            international_prefix=False,
            separator=" ",
            format="xxx-xxx-xxxx",
        )
        self.assertEqual(result, "02 012 3456")

    def test_home_format_2_inter(self):
        result = format_phone_number(
            phone_type="home",
            home_prefix="2",
            mobile_prefix="",
            number="0123456789",
            international_prefix=True,
            separator="-",
            format="xxxxxx-xxxx",
        )
        self.assertEqual(result, "+662012-3456")

    def test_home_format_3_inter(self):
        result = format_phone_number(
            phone_type="home",
            home_prefix="2",
            mobile_prefix="",
            number="0123456789",
            international_prefix=True,
            separator="-",
            format="xx-xxxx-xxxx",
        )
        self.assertEqual(result, "+662-012-3456")

    def test_weighted_list(self):
        result = generate_weighted_list(["A", "B", "C"], [3, 1, 2])
        self.assertEqual(result, ["A", "A", "A", "B", "C", "C"])

    def test_generate_single_phone_number_sample(self):
        result = generate_single_phone_number_sample(
            phone_type_weighted=generate_weighted_list(["home", "mobile"], [1, 0]),
            home_prefix_weighted=generate_weighted_list(
                [2, 3, 4, 5, 7], [1, 0, 0, 0, 0]
            ),
            mobile_prefix_weighted=generate_weighted_list([6, 8, 9], [1, 0, 0]),
            international_prefix_weighted=generate_weighted_list([True, False], [1, 0]),
            separator_weighted=generate_weighted_list(["-", " ", ""], [1, 0, 0]),
            format_weighted=generate_weighted_list(
                ["xxx-xxx-xxxx", "xxxxxx-xxxx", "xx-xxxx-xxxx"], [1, 0, 0]
            ),
            use_thai_numeral_weighted=generate_weighted_list([True, False], [0, 1]),
        )
        self.assertTrue(
            result.startswith("+66"),
            f"Expected result to start with '+66', but got {result}",
        )

        format_pattern = r"\+66\d-\d{3}-\d{4}"
        self.assertTrue(
            re.match(format_pattern, result),
            f"Expected result to match pattern '+66x-xxx-xxxx', but got {result}",
        )
        self.assertTrue(
            re.fullmatch(format_pattern, result),
            f"Expected result to contain only Arabic numerals, but got {result}",
        )


if __name__ == "__main__":
    unittest.main()
