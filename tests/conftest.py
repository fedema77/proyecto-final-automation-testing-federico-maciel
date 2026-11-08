import pytest

from utils.driver_setup import create_driver
from utils.screenshot_utils import capture_screenshot


@pytest.fixture
def driver():
    driver = create_driver(headless=True)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed and "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        capture_screenshot(driver, item.name)
