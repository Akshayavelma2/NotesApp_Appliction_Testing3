import time
from pages.login_page import LoginPage
from pages.home_page import HomePage
from api.api_client import APIClient
from config.environment import config


def test_delete_note_api_to_ui(driver):

    unique = str(int(time.time()))

    title = "Delete E2E Note " + unique
    description = "This note will be deleted using API"

    api = APIClient()
    api.login()

    create_response = api.create_note(title, description, "Home")
    assert create_response.status_code == 200

    note_id = create_response.json()["data"]["id"]

    notes_response = api.get_notes()
    notes = notes_response.json()["data"]

    created_note_found = False

    for note in notes:
        if note["id"] == note_id:
            created_note_found = True
            break

    assert created_note_found

    delete_response = api.delete_note(note_id)
    assert delete_response.status_code == 200

    after_delete_response = api.get_notes()
    after_delete_notes = after_delete_response.json()["data"]

    deleted_note_found = False

    for note in after_delete_notes:
        if note["id"] == note_id:
            deleted_note_found = True
            break

    assert deleted_note_found == False

    login_page = LoginPage(driver)
    login_page.login(config["email"], config["password"])

    home_page = HomePage(driver)

    driver.refresh()
    time.sleep(3)

    assert home_page.is_note_not_visible(title)