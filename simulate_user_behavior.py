import time
from selenium.webdriver.support.ui import Select


class Simulate:
    page_driver = None

    def __init__(self, page_driver):
        self.page_driver = page_driver


class SimulateSelection(Simulate):

    def select_to_option(self, css_selector, select_option):
        # get select options in the webpage pagination
        inputs = Select(self.page_driver.find_element_by_css_selector(css_selector))

        for option in inputs.options:
            # select oldest to newest sorting option
            if option.text == select_option:
                option.click()
        # give time to page to update page data
        time.sleep(2)
