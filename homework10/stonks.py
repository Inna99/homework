import json
import logging
from collections import defaultdict
from itertools import chain
from multiprocessing import Pool

from bs4 import BeautifulSoup  # type: ignore

from .parse_classes import ParsingCompanyPage, ParsingMainPage

# logging.basicConfig(level=logging.DEBUG)


def get_all_main_links():
    return [
        f"https://markets.businessinsider.com/index/components/s&p_500?p={i}"
        for i in range(1, 12)
    ]


def make_all_on_main(main_url):
    parsing_main_paige = ParsingMainPage(main_url)
    return parsing_main_paige.get_growth_decline_and_current_value()


def get_all_comp_links(d):
    return [[name, values["company_url"]] for name, values in d.items()]


def make_all_comp(tmp):
    name, company_url = tmp
    parsing_company_page = ParsingCompanyPage(company_url, name)
    return parsing_company_page.info_about_company()


def parse_business_insider():
    """"""
    first_part_dict = {}
    second_part_dict = {}
    all_links = get_all_main_links()
    with Pool(32) as p:
        x = p.map(make_all_on_main, all_links)
    for i in x:
        first_part_dict.update(i)
    print(first_part_dict)
    all_links_comp = get_all_comp_links(first_part_dict)
    with Pool(32) as p:
        y = p.map(make_all_comp, all_links_comp)

    for i in y:
        second_part_dict.update(i)
    print(second_part_dict)

    for k, v in chain(first_part_dict.items(), second_part_dict.items()):
        all_information_companies[k].update(v)

    logging.debug(f"{len(all_information_companies)}, {all_information_companies}")


def save_the_final_information():
    """Сохранить итоговую информацию в 4 JSON файла"""
    with open("the most expensive shares in rubles.json", "w") as fp:
        a = sorted(
            all_information_companies.values(),
            key=lambda x: x["current_value"],
            reverse=True,
        )
        json.dump(a[:10], fp)
    with open("the lowest p_e index.json", "w") as fp:
        a = sorted(all_information_companies.values(), key=lambda x: x["p_e_ratio"])
        json.dump(a[:10], fp)
    with open("which showed the highest growth over the past year.json", "w") as fp:
        a = sorted(
            all_information_companies.values(),
            key=lambda x: x["growth_decline"],
            reverse=True,
        )
        json.dump(a[:10], fp)
    with open("which would bring the greatest profit.json", "w") as fp:
        a = sorted(
            all_information_companies.values(),
            key=lambda x: x["percent_sale_from_high"] + x["percent_buy_from_low"],
            reverse=True,
        )
        json.dump(a[:10], fp)


if __name__ == "__main__":  # pragma: no cover
    all_information_companies: defaultdict = defaultdict(dict)
    parse_business_insider()
    save_the_final_information()
    logging.debug(f"{len(all_information_companies)}, {all_information_companies}")
