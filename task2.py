import re
import os
from web_driver import ChromeDriver
from simulate_user_behavior import SimulateSelection
from driver_utils import fetch_url_content, go_to_url
from utils import download_file, delete_all_empty_dirs
from soup_utils import create_soup, find_in_soup

# page link
census_page_url = 'https://www.census.gov/library/publications.html'
census_folder = os.path.dirname(os.path.abspath("__file__")) + "/Census Publication"
css_selector = '[ng-model=sortBy]'
select_option = 'Oldest to Newest'
size_limit_in_byte = 5 * 1024 * 1024
driver_args = (
    '--ignore-certificate-errors',
    '--incognito',
    '--headless',
    '--no-sandbox',
    '--disable-dev-shm-usage',
)


def task2():
    chrome_driver = ChromeDriver(driver_args)
    go_to_url(chrome_driver.driver, census_page_url)
    SimulateSelection(chrome_driver.driver).select_to_option(css_selector, select_option)
    soup = create_soup(chrome_driver.driver.page_source)
    articles = find_in_soup(soup, 'div', 'class', 'article')
    for article in articles:
        anchors_tags = find_in_soup(article, 'a')
        title = (find_in_soup(article, 'a'))[0].get('title')
        link = anchors_tags[0].get('href')
        fetch_url_content(chrome_driver.driver, link)
        soup = create_soup(chrome_driver.driver.page_source)
        regex = re.compile(r'.pdf|.zip|.doc')
        file_anchor_tags = find_in_soup(soup, 'a', 'href', regex)
        title_folder = census_folder + '/' + title
        for file_anchor_tag in file_anchor_tags:
            url = file_anchor_tag.get('href')
            download_file(title_folder, url, size_limit_in_byte)
            break
    delete_all_empty_dirs(census_folder)

task2()