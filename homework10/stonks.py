import logging
from collections import OrderedDict
from multiprocessing import Pool


from parse_classes import ParsingMainPage, ParsingCompanyPage


logging.basicConfig(level=logging.DEBUG)


def parse_business_insider():
    """"""
    # company_url = 'https://markets.businessinsider.com/stocks/wy-stock'
    # parsing_company_page = ParsingCompanyPage(company_url)
    # parsing_company_page.get_profit()
    # parsing_company_page.get_company_code()
    # parsing_company_page.get_p_e_ratio()
def get_all_main_links():
    for i in range(1, 12):
        return [f'https://markets.businessinsider.com/index/components/s&p_500?p={i}' for i in range(1, 12)]


def make_all_on_main(main_url):
    parsing_main_paige = ParsingMainPage(main_url)
    return parsing_main_paige.get_growth_decline_and_current_value(all_information_companies)

def get_all_comp_links():
    return [values['company_url'] for name, values in all_information_companies.items()]


def make_all_comp(main_url):


if __name__ == '__main__':
    all_information_companies = OrderedDict()
    all_links = get_all_main_links()
    with Pool(2) as p:
        x = p.map(make_all_on_main, all_links)
    for i in x:
        all_information_companies.update(i)

    # for i in range(1, 3):
    #     main_url = f'https://markets.businessinsider.com/index/components/s&p_500?p={i}'
    #     parsing_main_paige = ParsingMainPage(main_url)
    #     parsing_main_paige.get_growth_decline_and_current_value(all_information_companies)
    logging.debug(f'{len(all_information_companies)}, {all_information_companies}')
    for name, values in all_information_companies.items():
        company_url = values['company_url']
        parsing_company_page = ParsingCompanyPage(company_url)
        percent_sale_from_high, percent_buy_from_low = parsing_company_page.get_profit()
        company_code = parsing_company_page.get_company_code()
        p_e_ratio = parsing_company_page.get_p_e_ratio()
        all_information_companies.update({name: {
            'p_e_ratio': p_e_ratio,
            'company_code': company_code,
            'percent_sale_from_high': percent_sale_from_high,
            'percent_buy_from_low': percent_buy_from_low}
        })

    logging.debug(f'{len(all_information_companies)}, {all_information_companies}')
    print(f'{len(all_information_companies)}, {all_information_companies}')

