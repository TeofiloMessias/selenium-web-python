import pytest
from selenium import webdriver

driver: webdriver.Remote

@pytest.fixture()
def setup_teardown():
    #Setup
    global driver
    driver = webdriver.Chrome()
    driver.implicity_wait(5)
    driver.maximize_window()
    driver.get("https://saucedemo.com/")

    # run test
    yield

    # teardown
    driver.quit()