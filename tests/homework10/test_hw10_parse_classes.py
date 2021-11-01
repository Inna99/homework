from pathlib import Path
from unittest import TestCase

import requests
from bs4 import BeautifulSoup  # type: ignore

from homework10.parse_classes import ParsingMainPage

main_url = f"https://markets.businessinsider.com/index/components/s&p_500?p={1}"
request = requests.get(main_url)
html_doc = request.text
soup = BeautifulSoup(html_doc, "html.parser")


class MockResponse(TestCase):
    def __init__(self, file):
        super().__init__()
        with open(file, "r") as f:
            self.text = f.read()


cur_dir = Path("main_for_test.html")
print(cur_dir)


def test_get_url_company_external_resource():
    """returns address using external resource"""
    main_url = f"https://markets.businessinsider.com/index/components/s&p_500?p=1"
    parsing_main_paige = ParsingMainPage(main_url)
    assert (
        parsing_main_paige.get_url_company("Abbott Laboratories")
        == "https://markets.businessinsider.com/stocks/abt-stock"
    )


# def test_get_url_company_saved_html():
#     """returns address using saved html"""
#     with patch.object(requests, "get") as mock_method:
#
#     mock_method.return_value = MockResponse(cur_dir)
#     parsing_main_paige = ParsingMainPage(main_url)
#     print(parsing_main_paige)
#     assert parsing_main_paige.get_url_company('Abbott Laboratories') == 'https://markets.businessinsider.com/stocks/abt-stock'
#
#
# def test_get_url_company_mock_html():
#     """returns address using with mock"""


# def test_get_growth_decline_and_current_value():
#     """checking the collection of all information from the main page to the dictionary"""
#
# class TestParsingCompanyPage:
#     def __init__(self):
#         pass
#
#     def test_get_company_code(self):
#         """checks the company code from the company page to the right of the name"""
#
#     def test_week_low_high(self):
#         """checks the value of shares bought at 52 Week Low and sold at 52 Week High"""
#
#
#     def test_previous_closure(self):
#         """checks the value at the last close of trading"""
#
#     def test_get_profit(self):
#         """check what profit would the company's shares bring"""
#
#     def test_get_p_e_ratio(self):
#         """P/E компании"""
#
#     def test_info_about_company(self):
#         """"""
