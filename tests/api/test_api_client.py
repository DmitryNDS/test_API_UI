import pytest
from utils.api_client import APIClient

# Sample JSON schema for response validation
USER_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "email": {"type": "string", "format": "email"}
    },
    "required": ["id", "name", "email"]
}

@pytest.fixture
def api_client(api_base_url):
    return APIClient(api_base_url)

@pytest.mark.api
class TestAPIClient:
    def test_get_user(self, api_client):
        """Test getting user information."""
        response = api_client.get(
            endpoint="/users/1",
            json_schema=USER_SCHEMA
        )
        assert response.status_code == 200
        data = response.json()
        assert data["id"] == 1
        assert "name" in data
        assert "email" in data

    def test_create_user(self, api_client, faker):
        """Test creating a new user."""
        user_data = {
            "name": faker.name(),
            "email": faker.email()
        }
        response = api_client.post(
            endpoint="/users",
            data=user_data,
            json_schema=USER_SCHEMA
        )
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == user_data["name"]
        assert data["email"] == user_data["email"] 