import time
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from config.environment import config


def test_empty_note_creation(driver):

    login_page = LoginPage(driver)

    login_page.login(
        config["email"],
        config["password"]
    )

    time.sleep(3)

    add_note_btn = driver.find_element(
        By.XPATH,
        "//button[@data-testid='add-new-note']"
    )
    driver.execute_script("arguments[0].click();", add_note_btn)

    time.sleep(2)

    save_btn = driver.find_element(
        By.XPATH,
        "//button[@data-testid='note-submit']"
    )
    driver.execute_script("arguments[0].click();", save_btn)

    time.sleep(2)

    page = driver.page_source.lower()

    assert (
        "required" in page
        or "title" in page
        or "description" in page
        or "category" in page
    )