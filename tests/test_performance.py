import time
from api.api_client import APIClient
from config.environment import config


def test_api_response_time():

    api = APIClient()
    api.login()

    response = api.get_notes()

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2


def test_ui_page_load_time(driver):

    start_time = time.time()

    driver.get(config["url"])

    end_time = time.time()

    load_time = end_time - start_time

    assert load_time < 5