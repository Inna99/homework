import os.path
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch

import requests

from homework10.parse_classes import ParsingCompanyPage, ParsingMainPage

# logging.basicConfig(level=logging.DEBUG)


class MockResponse(TestCase):
    def __init__(self, file):
        super().__init__()
        cur_dir = os.path.join(Path(__file__).parent, file)
        with open(cur_dir, "r", encoding="utf-8") as html_file:
            self.text = html_file.read()


def test_get_url_company_saved_html():
    """returns address using saved html"""
    main_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("main_for_test.html")
        parsing_main_paige = ParsingMainPage(main_url)
        assert (
            parsing_main_paige.get_url_company("Abbott Laboratories")
            == "https://markets.businessinsider.com/stocks/abt-stock"
        )


def test_get_url_company_external_resource():
    """returns address using external resource"""
    main_url = f"https://markets.businessinsider.com/index/components/s&p_500?p={1}"
    parsing_main_paige = ParsingMainPage(main_url)
    assert (
        parsing_main_paige.get_url_company("Abbott Laboratories")
        == "https://markets.businessinsider.com/stocks/abt-stock"
    )


def test_get_growth_decline_and_current_value():
    """checking the collection of all information from the main page to the dictionary"""
    main_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("main_for_test.html")
        parsing_main_paige = ParsingMainPage(main_url)
        with open(
            os.path.join(
                Path(__file__).parent, "get_growth_decline_and_current_value.txt"
            ),
            "r",
        ) as f:
            return_values = f.read()
            assert (
                str(parsing_main_paige.get_growth_decline_and_current_value())
                == return_values
            )


def test_get_growth_decline_and_current_value_mock():
    """checking the collection of all information from the main page to the dictionary"""
    main_url = f"https://markets.businessinsider.com/index/components/s&p_500?p={1}"
    parsing_main_paige = ParsingMainPage(main_url)
    with open(
        os.path.join(Path(__file__).parent, "get_growth_decline_and_current_value.txt"),
        "r",
    ) as f:
        return_values = f.read()
        assert (
            str(parsing_main_paige.get_growth_decline_and_current_value())
            == return_values
        )


def test_get_company_code():
    """checks the company code from the company page to the right of the name"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.get_company_code() == "ABT"


def test_week_low_high():
    """checks the value of shares bought at 52 Week Low and sold at 52 Week High"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.week_low_high() == (103.16, 129.68)


def test_previous_closure():
    """checks the value at the last close of trading"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.previous_closure() == 128.94


def test_get_profit():
    """check what profit would the company's shares bring"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.get_profit() == (0.57, 24.99)


def test_get_p_e_ratio():
    """P/E компании"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.get_p_e_ratio() == 103.16


def test_info_about_company():
    """check collects all the information from the company's page"""
    comp_url = ""
    with patch.object(requests, "get") as mock_method:
        mock_method.return_value = MockResponse("company_for_test.html")
        parsing_company_paige = ParsingCompanyPage(comp_url, "Abbott Laboratories")
        assert parsing_company_paige.info_about_company() == {
            "Abbott Laboratories": {
                "p_e_ratio": 103.16,
                "company_code": "ABT",
                "percent_sale_from_high": 0.57,
                "percent_buy_from_low": 24.99,
            }
        }
