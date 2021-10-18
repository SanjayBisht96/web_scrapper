from bs4 import BeautifulSoup


def find_in_soup(soup, tag, attr=None, value=None):
    if attr and value:
        return soup.find_all(tag, {attr: value})
    else:
        return soup.find_all(tag)


def create_soup(response, parser='html.parser'):
    return BeautifulSoup(response, parser)
