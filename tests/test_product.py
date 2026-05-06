from pages.login_page import LoginPage
from config.environment import config

def test_notes_page_loaded(driver):
    login = LoginPage(driver)

    login.login(config["email"], config["password"])

    assert "Notes" in driver.page_source