pytest_plugins = ["fixtures.browser_fixture"]

from pages.login_page import LoginPage
from config.environment import config

def test_login(driver):
    login_page = LoginPage(driver)

    login_page.login(config["email"], config["password"])

    assert "Notes" in driver.page_source