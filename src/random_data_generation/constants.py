ARABIC_DIGITS = "0123456789"
THAI_DIGITS = "๐๑๒๓๔๕๖๗๘๙"
THAI_ALPHABETS = "กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรฤลฦวศษสหฬอฮ"

CURRENCIES = {
    "USD": ("$", "USD"),
    "EUR": ("€", "EUR"),
    "GBP": ("£", "GBP"),
    "THB": ("฿", "THB"),
    "JPY": ("¥", "JPY"),
}
CURRENCY_MAX_AMOUNT = 100000000
CURRENCY_CHOICES = ["USD", "EUR", "GBP", "THB", "JPY"]
CURRENCY_WEIGHTS = [1, 1, 1, 6, 1]
CURRENCY_USE_DASH_WEIGHTS = [1, 5]
CURRENCY_USE_THAI_NUMERAL_WEIGHTS = [2, 1]
CURRENCY_USE_SUFFIX_WEIGHTS = [3, 1]
CURRENCY_SUFFIX_TH_WEIGHTS = [4, 1]

NUMERIC_MAX_AMOUNT = 100000000
NUMERIC_USE_THAI_NUMERAL_WEIGHTS = [1, 1]

PHONE_NUMBER_MAX_LENGTH = 10
PHONE_MIN_DIGIT = 0
PHONE_MAX_DIGIT = 9
PHONE_CHOICES = ["home", "mobile"]
PHONE_WEIGHTS = [1, 4]
PHONE_HOME_PREFIX_CHOICES = [2, 3, 4, 5, 7]
PHONE_HOME_PREFIX_WEIGHTS = [10, 1, 1, 2, 1]
PHONE_MOBILE_PREFIX_CHOICES = [6, 8, 9]
PHONE_MOBILE_PREFIX_WEIGHTS = [2, 3, 5]
PHONE_INTER_PREFIX_WEIGHTS = [1, 3]
PHONE_SEPARATOR_CHOICES = ["-", " ", ""]
PHONE_SEPARATOR_WEIGHTS = [8, 2, 5]
PHONE_FORMAT_CHOICES = ["xxx-xxx-xxxx", "xxxxxx-xxxx", "xx-xxxx-xxxx"]
PHONE_FORMAT_WEIGHTS = [10, 2, 3]
PHONE_USE_THAI_NUMERAL_WEIGHTS = [1, 1]

LICENSE_CHOICES = ["a", "aa", "1a", "1aa"]
LICENSE_WEIGHTS = [1, 8, 1, 4]
LICENSE_MIN_PREFIX_NUM = 1
LICENSE_MAX_PREFIX_NUM = 9
LICENSE_MIN_NUMBER = 1
LICENSE_MAX_NUMBER = 9999
LICENSE_SEPARATOR_CHOICES = ["-", " ", ""]
LICENSE_SEPARATOR_WEIGHTS = [1, 1, 1]
LICENSE_USE_THAI_NUMERAL_WEIGHTS = [1, 3]

MONTH_NAMES_TH = [
    "มกราคม",
    "กุมภาพันธ์",
    "มีนาคม",
    "เมษายน",
    "พฤษภาคม",
    "มิถุนายน",
    "กรกฎาคม",
    "สิงหาคม",
    "กันยายน",
    "ตุลาคม",
    "พฤศจิกายน",
    "ธันวาคม",
]
MONTH_ABBRS_TH = [
    "ม.ค.",
    "ก.พ.",
    "มี.ค.",
    "เม.ย.",
    "พ.ค.",
    "มิ.ย.",
    "ก.ค.",
    "ส.ค.",
    "ก.ย.",
    "ต.ค.",
    "พ.ย.",
    "ธ.ค.",
]

MONTH_NAMES_EN = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

MONTH_ABBRS_EN = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
DATE_START_DATE = (1900, 1, 1)
DATE_END_DATE = (2100, 12, 31)
DATE_FORMAT_CHOICES = [
    "DD/MM/YYYY",
    "MM/DD/YYYY",
    "YYYY/MM/DD",
    "YYYY/DD/MM",
    "DD/Month/YYYY",
    "Month DD, YYYY",
    "DD Month Year_type YYYY",
]
DATE_FORMAT_WEIGHTS = [4, 2, 1, 1, 3, 2, 2]
DATE_YEAR_TYPE_CHOICES = ["ad", "be"]
DATE_YEAR_TYPE_WEIGHTS = [1, 1]
DATE_YEAR_DIGIT_CHOICES = [2, 4]
DATE_YEAR_DIGIT_WEIGHTS = [1, 4]
DATE_MONTH_LANG_THAI_WEIGHTS = [1, 2]
DATE_FULL_MONTH_WEIGHTS = [1, 1]
DATE_DATE_FORMAT_CHOICES = [1, 2]
DATE_DATE_FORMAT_WEIGHTS = [1, 1]
DATE_SEPARATOR_CHOICES = ["-", "/", " "]
DATE_SEPARATOR_WEIGHTS = [3, 3, 1]
DATE_USE_THAI_NUMERAL_WEIGHTS = [1, 2]
