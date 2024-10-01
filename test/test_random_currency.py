# Unit tests
import unittest

from random_data_generation.currency import (
    format_currency,
    generate_weighted_list,
    generate_single_currency_sample,
)


class TestFormatCurrency(unittest.TestCase):

    def test_format_usd(self):
        result = format_currency(
            1234.56,
            "USD",
            use_symbol=True,
            use_comma=True,
            show_cents=True,
            use_dash=False,
            use_space=True,
        )
        self.assertEqual(result, "$ 1,234.56")

    def test_format_eur_no_comma(self):
        result = format_currency(
            1234.56,
            "EUR",
            use_symbol=False,
            use_comma=False,
            show_cents=True,
            use_dash=False,
            use_space=True,
        )
        self.assertEqual(result, "EUR 1234.56")

    def test_format_thb_thai_numeral(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=True,
            use_comma=True,
            show_cents=True,
            use_thai_numeral=True,
        )
        self.assertEqual(result, "฿๑,๒๓๔.๕๖")

    def test_format_jpy_no_cents(self):
        result = format_currency(
            1234.56, "JPY", use_symbol=True, use_comma=True, show_cents=False
        )
        self.assertEqual(result, "¥1,235")

    def test_format_thb_no_space(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=False,
            use_comma=True,
            show_cents=True,
        )
        self.assertEqual(result, "THB1,234.56")

    def test_format_thb_dash(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=False,
            use_comma=True,
            show_cents=True,
            use_dash=True,
        )
        self.assertEqual(result, "THB1,234.56.-")

    def test_format_thb_thai_word_no_space(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=False,
            use_comma=True,
            show_cents=True,
            use_suffix=True,
            suffix_th=True,
        )
        self.assertTrue(result.endswith("บาท"))

    def test_format_thb_thai_word_with_space(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=False,
            use_comma=True,
            show_cents=True,
            use_space=True,
            use_suffix=True,
            suffix_th=True,
        )
        self.assertTrue(result.endswith(" บาท"))

    def test_format_thb_thai_word_eng_suffix_with_space(self):
        result = format_currency(
            1234.56,
            "THB",
            use_symbol=False,
            use_comma=True,
            show_cents=True,
            use_space=True,
            use_suffix=True,
        )
        self.assertTrue(result.endswith(" Baht"))

    def test_weighted_list(self):
        result = generate_weighted_list(["A", "B", "C"], [3, 1, 2])
        self.assertEqual(result, ["A", "A", "A", "B", "C", "C"])

    def test_generate_single_currency_sample(self):
        result = generate_single_currency_sample(
            currency_weighted=generate_weighted_list(
                ["USD", "EUR", "THB", "JPY"], [1, 1, 6, 1]
            ),
            use_dash_weighted=generate_weighted_list([True, False], [1, 5]),
            use_thai_numeral_weighted=generate_weighted_list([True, False], [2, 1]),
            use_suffix_weighted=generate_weighted_list([True, False], [3, 1]),
            suffix_th_weighted=generate_weighted_list([True, False], [4, 1]),
        )
        self.assertIsNotNone(result, "The result is None")
        self.assertNotEqual(result, "", "The result is an empty string")


if __name__ == "__main__":
    unittest.main()
