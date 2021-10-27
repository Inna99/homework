import logging
import re

import requests
from bs4 import BeautifulSoup  # type: ignore

from homework10 import cbr  # type: ignore


class ParsingMainPage:
    def __init__(self, url):
        request = requests.get(url)
        html_doc = request.text
        self.soup = BeautifulSoup(html_doc, "html.parser")

    def get_growth_decline_and_current_value(self):
        """Annual growth/decline of the company as a percentage
        Годовой рост/падение компании в процентах
        (current_value, growth_decline, name)
        """
        name_dict = {}
        current_tag = self.soup.find("tbody", {"class": "table__tbody"})
        company_name, growth_decline, current_value = (0, 0, 0)
        curse_usd = float((cbr.get_valute()).replace(",", ""))

        for k, i in enumerate(current_tag.childGenerator(), 0):
            if k % 2:
                d0 = i.text
                d1 = re.sub("[\r\t]", "", d0).split()
                growth_decline = d1[-1][:-1]
                current_value = float(d1[-18].replace(",", ""))
                company_name = " ".join(d1[-19::-1][::-1])
                logging.debug(f"{growth_decline}, {current_value}, {company_name}")
                current_value_rub = curse_usd * current_value
                name_dict.update(
                    {
                        company_name: {
                            "growth_decline": growth_decline,
                            "current_value": current_value_rub,
                            "company_url": self.get_url_company(company_name),
                        }
                    }
                )
        return name_dict

    def get_url_company(self, name):
        """"""
        current_tag = self.soup.find("a", {"title": name})
        company_url = f"https://markets.businessinsider.com{current_tag['href']}"
        return company_url


class ParsingCompanyPage:
    def __init__(self, url):
        request = requests.get(url)
        html_doc = request.text
        self.soup = BeautifulSoup(html_doc, "html.parser")

    def get_company_code(self):
        """Код компании (справа от названия компании на странице компании)"""
        company_code = self.soup.find("title").text.split()[0]
        logging.debug(company_code)
        return company_code

    def get_profit(self):
        """what profit would the company's shares bring
        Высчитать какую прибыль принесли бы акции компании (в процентах),
        если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High"""
        current_tag = self.soup.find_all("div", {"class": "snapshot__highlow"})
        if len(current_tag) == 0:
            return 0, 0

        try:
            current_tag = current_tag[1].text.split()
        except IndexError:
            current_tag = current_tag[0].text.split()
        except TypeError as ex:
            logging.info(f"no week_low and week_high, with {ex}")
            return 0, 0
        week_low = float(current_tag[0].replace(",", ""))
        week_high = float(current_tag[4].replace(",", ""))

        logging.debug(f"week_low={week_low}, week_high={week_high}")
        # current value
        current_tag = self.soup.find("div", {"class": "snapshot"}).find_all(
            "div", {"class": "snapshot__data-item"}
        )
        d0 = current_tag[0].text
        prev_close = float(re.sub("[\r\n]", "", d0).split()[0].replace(",", ""))

        logging.debug(f"prev_close = {prev_close}")
        what_profit_buy = prev_close - week_low
        what_profit_sale = week_high - prev_close
        logging.debug(f"{what_profit_buy}, {what_profit_sale}")
        percent_sale_from_high = ((100 * what_profit_sale) / week_high)
        percent_buy_from_low = ((100 * what_profit_buy) / week_low)
        logging.debug(
            f"percent_sale_from_high={percent_sale_from_high}, percent_buy_from_low={percent_buy_from_low}"
        )
        return percent_sale_from_high, percent_buy_from_low

    def get_p_e_ratio(self):
        """P/E компании (информация находится справа от графика на странице компании)"""
        try:
            current_tag = self.soup.find("div", {"class": "snapshot"}).find_all(
                "div", {"class": "snapshot__data-item"}
            )
            d0 = current_tag[6].text
            p_e_ratio = float(re.sub("[\r\n]", "", d0).split()[0].replace(",", ""))
            return p_e_ratio
        except AttributeError:
            logging.info("no info about company ")
            return 0
