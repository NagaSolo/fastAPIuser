from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from app.core.config import settings
from app.tests.utils.address import create_random_address


def test_create_item(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    data = {"line": "Lot 000", "postcode": 1900, "city": "Pandan", "state": "Selangor"}
    response = client.post(
        f"{settings.API_V1_STR}/addresses/", headers=superuser_token_headers, json=data,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["line"] == data["title"]
    assert content["postcode"] == data["postcode"]
    assert content["city"] == data["city"]
    assert content["state"] == data["state"]
    assert "id" in content
    assert "user_id" in content


def test_read_item(
    client: TestClient, superuser_token_headers: dict, db: Session
) -> None:
    address = create_random_address(db)
    response = client.get(
        f"{settings.API_V1_STR}/addresses/{address.id}", headers=superuser_token_headers,
    )
    assert response.status_code == 200
    content = response.json()
    assert content["line"] == address.line
    assert content["postcode"] == address.postcode
    assert content["city"] == address.city
    assert content["state"] == address.state
    assert content["id"] == address.id
    assert content["user_id"] == address.user_id
