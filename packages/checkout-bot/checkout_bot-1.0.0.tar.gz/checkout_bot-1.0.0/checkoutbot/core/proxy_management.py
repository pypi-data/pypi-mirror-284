def get_proxies(api_url):
    """
    Fetch proxies from a given API.

    Args:
        api_url (str): The API URL to fetch proxies from.

    Returns:
        list: A list of proxy addresses.
    """
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        proxies = response.json().get('proxies', [])
        return proxies
    except requests.RequestException as e:
        print(f"Error fetching proxies: {e}")
        return []

def set_proxy(driver, proxy):
    """
    Set proxy for Selenium WebDriver.

    Args:
        driver (webdriver): The Selenium WebDriver instance.
        proxy (str): The proxy address to use.

    Returns:
        None
    """
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": proxy,
        "ftpProxy": proxy,
        "sslProxy": proxy,
        "proxyType": "MANUAL",
    }
    driver.start_session(webdriver.DesiredCapabilities.CHROME)
