#Response Time is Present in This
from api.api_client import APIClient
from utils.logger import get_logger

logger = get_logger(__name__)

def test_get_notes():

    logger.info("Starting API GET notes test")

    api = APIClient()

    login_response = api.login()
    logger.info("API login completed")

    assert login_response.status_code == 200

    response = api.get_notes()
    logger.info("GET notes API called")

    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2 #This

    notes = response.json()["data"]

    assert isinstance(notes, list)

    logger.info("API GET notes test completed successfully")