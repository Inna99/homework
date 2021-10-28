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
        # company_name, growth_decline, current_value = (0, 0, 0)
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
                url_company = self.get_url_company(company_name)
                if 'stocks' in url_company:
                    name_dict.update(
                        {
                            company_name: {
                                "growth_decline": growth_decline,
                                "current_value": current_value_rub,
                                "company_url": url_company,
                            }
                        }
                    )
        return name_dict

    def get_url_company(self, name):
        """returns url by company name"""
        current_tag = self.soup.find("a", {"title": name})
        company_url = f"https://markets.businessinsider.com{current_tag['href']}"
        return company_url


class ParsingCompanyPage:
    def __init__(self, url, name):
        self.name = name
        request = requests.get(url)
        html_doc = request.text
        self.soup = BeautifulSoup(html_doc, "html.parser")

    def get_company_code(self):
        """Код компании (справа от названия компании на странице компании)"""
        company_code = self.soup.find("main").find('span', {'class': 'price-section__category'}).find('span').text.split()[1]
        logging.debug(company_code)
        return company_code

    def week_low_high(self):
        """52 Week Low and 52 Week High"""
        current_tag = self.soup.find('main').find('div', {'class': 'snapshot__highlow-container'}).find_all('div', {'class': 'snapshot__highlow'})
        if current_tag is not None:
            tag = current_tag[0].text.split()
            if 'Week' not in current_tag:
                try:
                    tag = current_tag[1].text.split()
                except IndexError:
                    return 0, 0
            week_low = float(tag[0].replace(",", ""))
            week_high = float(tag[4].replace(",", ""))
            return week_low, week_high
        else:
            return 0, 0

    def previous_closure(self):
        """cost at the time of the previous closing"""
        current_tag = self.soup.find('div', {'class': 'snapshot'}).find('div').text.split()[0]
        prev_close = float(current_tag.replace(",", ""))
        return prev_close

    def get_profit(self):
        """what profit would the company's shares bring
        Высчитать какую прибыль принесли бы акции компании (в процентах),
        если бы они были куплены на уровне 52 Week Low и проданы на уровне 52 Week High"""
        week_low, week_high = self.week_low_high()
        prev_close = self.previous_closure()

        logging.debug(f"week_low={week_low}, week_high={week_high}")
        logging.debug(f"prev_close = {prev_close}")

        what_profit_buy = prev_close - week_low
        what_profit_sale = week_high - prev_close

        try:
            percent_sale_from_high = round((100 * what_profit_sale) / week_high, 2)
            percent_buy_from_low = round((100 * what_profit_buy) / week_low, 2)
            return percent_sale_from_high, percent_buy_from_low
        except ZeroDivisionError:
            return 0, 0

    def get_p_e_ratio(self):
        """P/E компании (информация находится справа от графика на странице компании)"""
        try:
            current_tag = self.soup.find('main').find_all('div', {'class': 'snapshot__data-item'})[6].text.split()[0]
            p_e_ratio = float(current_tag.replace(",", ""))
            logging.debug(f'p_e_ratio={p_e_ratio}')
            return p_e_ratio
        except AttributeError:
            logging.info("no info about company ")
            return 0

    def info_about_company(self):
        """collects all the information from the company's page and returns the dictionary"""
        percent_sale_from_high, percent_buy_from_low = self.get_profit()
        comp_dict = {
                self.name: {
                    "p_e_ratio": self.get_p_e_ratio(),
                    "company_code": self.get_company_code(),
                    "percent_sale_from_high": percent_sale_from_high,
                    "percent_buy_from_low": percent_buy_from_low,
                }
            }
        return comp_dict
