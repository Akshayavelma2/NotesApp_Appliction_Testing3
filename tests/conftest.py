import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.environment import config


@pytest.fixture
def driver():

    chrome_options = Options()

    if os.getenv("GRID") == "true":

        driver = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            options=chrome_options
        )

    else:

        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(config["url"])

    yield driver

    driver.quit()