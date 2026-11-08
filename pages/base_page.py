from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url):
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, value, timeout=10):
        element = self.find(locator, timeout)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator, timeout=10):
        return self.find(locator, timeout).text

    def is_displayed(self, locator, timeout=10):
        try:
            return self.find(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    def get_title(self):
        return self.driver.title
