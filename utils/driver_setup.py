from selenium import webdriver


def create_driver(headless=True):
    chrome_options = webdriver.ChromeOptions()

    if headless:
        chrome_options.add_argument("--headless=new")

    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    return driver