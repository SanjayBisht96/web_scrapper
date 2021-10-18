from utils import validate_url


def go_to_url(driver, url):
    if validate_url(url):
        driver.get(url)
    else:
        raise


def fetch_url_content(driver, url):
    if validate_url(url):
        return driver.get(url)
    else:
        raise
