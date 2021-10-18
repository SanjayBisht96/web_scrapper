import re
import os
from soup_utils import create_soup, find_in_soup
from utils import download_file, fetch_url_content

# page link
cmo_page_url = 'https://cms.math.ca/competitions/cmo/'
dest = os.path.dirname(os.path.abspath("__file__")) +"/Math Problems"


def task1():
    response = fetch_url_content(cmo_page_url)
    soup = create_soup(response.content)
    regex = re.compile(r'.pdf$')
    html_content = find_in_soup(soup, 'a', 'href', regex)
    for html in html_content:
        url = html.get('href')
        download_file(dest, url)


task1()