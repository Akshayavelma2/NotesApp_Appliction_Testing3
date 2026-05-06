pytest_plugins = ["fixtures.browser_fixture"]

from pages.login_page import LoginPage
from pages.home_page import HomePage
from api.api_client import APIClient
from config.environment import config

def test_create_note_ui_to_api(driver):

    title = "Automation Note"
    description = "Created using Selenium and verified using API"

    login_page = LoginPage(driver)
    login_page.login(config["email"], config["password"])

    home_page = HomePage(driver)
    home_page.create_note(title, description)

    assert home_page.is_note_visible(title)

    api = APIClient()
    api.login()

    response = api.get_notes()

    assert response.status_code == 200

    notes = response.json()["data"]

    note_found = False

    for note in notes:
        if note["title"] == title and note["description"] == description:
            note_found = True
            break

    assert note_found