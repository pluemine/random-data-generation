# Unit tests
import unittest
import re
from datetime import datetime, timedelta
from unittest.mock import patch

from random_data_generation.date import (
    format_date,
    generate_weighted_list,
    random_date,
    generate_single_date_sample,
)


class TestFormatDate(unittest.TestCase):

    def test_default(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="DD/MM/YYYY",
            year_type="ad",
            year_digit=4,
            month_lang_thai=False,
            full_month=False,
            date_format=2,
            separator="/",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "01/08/2024")

    def test_format_2_be(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="MM/DD/YYYY",
            year_type="be",
            year_digit=4,
            month_lang_thai=False,
            full_month=False,
            date_format=2,
            separator="/",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "08/01/2567")

    def test_format_3_be_year_2(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="YYYY/MM/DD",
            year_type="be",
            year_digit=2,
            month_lang_thai=False,
            full_month=False,
            date_format=2,
            separator="/",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "67/08/01")

    def test_format_4_be_year_2_date_1_sep(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="YYYY/DD/MM",
            year_type="be",
            year_digit=2,
            month_lang_thai=False,
            full_month=False,
            date_format=1,
            separator="-",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "67-1-8")

    def test_format_5_be_month_short_en(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="DD/Month/YYYY",
            year_type="be",
            year_digit=4,
            month_lang_thai=False,
            full_month=False,
            date_format=2,
            separator="/",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "01/Aug/2567")

    def test_format_5_be_month_long_en_sep(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="DD/Month/YYYY",
            year_type="be",
            year_digit=4,
            month_lang_thai=False,
            full_month=True,
            date_format=2,
            separator="-",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "01-August-2567")

    def test_format_5_ad_month_long_th_space(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="DD/Month/YYYY",
            year_type="ad",
            year_digit=4,
            month_lang_thai=True,
            full_month=True,
            date_format=2,
            separator=" ",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "01 สิงหาคม 2024")

    def test_format_6_ad_month_short_th(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="Month DD, YYYY",
            year_type="ad",
            year_digit=4,
            month_lang_thai=True,
            full_month=False,
            date_format=2,
            separator=" ",
            use_thai_numeral=False,
        )
        self.assertEqual(result, "ส.ค. 01, 2024")

    def test_format_7_be_month_thai_numeral(self):
        result = format_date(
            date=datetime(2024, 8, 1),
            format="DD Month Year_type YYYY",
            year_type="be",
            year_digit=4,
            month_lang_thai=False,  # Should not change to English even False
            date_format=2,
            use_thai_numeral=True,
        )
        self.assertEqual(result, "๐๑ สิงหาคม พ.ศ. ๒๕๖๗")

    def test_weighted_list(self):
        result = generate_weighted_list(["A", "B", "C"], [3, 1, 2])
        self.assertEqual(result, ["A", "A", "A", "B", "C", "C"])

    def test_random_date_within_range(self):
        start_date = datetime(2023, 1, 1)
        end_date = datetime(2023, 1, 10)
        generated_date = random_date(start_date, end_date)
        self.assertTrue(
            start_date <= generated_date <= end_date, "Generated date is out of range"
        )

    def test_random_date_edge_case_same_dates(self):
        start_date = end_date = datetime(2023, 1, 1)
        generated_date = random_date(start_date, end_date)
        self.assertEqual(
            generated_date,
            start_date,
            "Generated date should be the same as the start/end date",
        )

    def test_random_date_large_range(self):
        start_date = datetime(2000, 1, 1)
        end_date = datetime(2100, 1, 1)
        generated_date = random_date(start_date, end_date)
        self.assertTrue(
            start_date <= generated_date <= end_date, "Generated date is out of range"
        )

    def test_random_date_reverse_range(self):
        start_date = datetime(2023, 1, 10)
        end_date = datetime(2023, 1, 1)
        with self.assertRaises(ValueError):
            random_date(start_date, end_date)

    @patch("random_data_generation.date.random_date")
    @patch("random_data_generation.date.random.randint", return_value=0.5)
    def test_generate_single_date_sample(self, mock_rand, mock_random_date):
        # Setup controlled random date
        mock_random_date.return_value = datetime(2023, 7, 15)

        # Define weighted lists
        format_weighted = generate_weighted_list(["DD/MM/YYYY", "MM/DD/YYYY"], [1, 0])
        year_type_weighted = generate_weighted_list(["ad", "be"], [1, 0])
        year_digit_weighted = generate_weighted_list([2, 4], [0, 1])
        month_lang_thai_weighted = generate_weighted_list([True, False], [1, 0])
        full_month_weighted = generate_weighted_list([True, False], [1, 0])
        date_format_weighted = generate_weighted_list([1, 2], [1, 0])
        separator_weighted = generate_weighted_list(["-", "/", " "], [1, 0, 0])
        use_thai_numeral_weighted = generate_weighted_list([True, False], [0, 1])

        # Generate the sample date
        result = generate_single_date_sample(
            format_weighted=format_weighted,
            year_type_weighted=year_type_weighted,
            year_digit_weighted=year_digit_weighted,
            month_lang_thai_weighted=month_lang_thai_weighted,
            full_month_weighted=full_month_weighted,
            date_format_weighted=date_format_weighted,
            separator_weighted=separator_weighted,
            use_thai_numeral_weighted=use_thai_numeral_weighted,
        )

        expected_date = "15-7-2023"
        self.assertEqual(result, expected_date)


if __name__ == "__main__":
    unittest.main()
