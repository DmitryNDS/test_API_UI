import pytest
import allure
from utils.api_client import APIClient
from tests.api.models import User, ErrorResponse
from faker import Faker

fake = Faker()

@pytest.fixture
def api_client():
    return APIClient("https://jsonplaceholder.typicode.com")  # Using JSONPlaceholder as example API

@pytest.fixture
def test_user():
    return {
        "name": fake.name(),
        "email": fake.email(),
        "status": "active"
    }

@allure.feature("User API")
@allure.story("User Management")
class TestUserAPI:
    
    @allure.title("Get all users")
    def test_get_users(self, api_client):
        with allure.step("Get all users"):
            response = api_client.get("/users")
            assert response.status_code == 200
            users = response.json()
            assert isinstance(users, list)
            assert len(users) > 0

    @allure.title("Get user by ID")
    def test_get_user_by_id(self, api_client):
        with allure.step("Get user with ID 1"):
            response = api_client.get("/users/1")
            assert response.status_code == 200
            user = User(**response.json())
            assert user.id == 1

    @allure.title("Create new user")
    def test_create_user(self, api_client, test_user):
        with allure.step("Create new user"):
            response = api_client.post("/users", json=test_user)
            assert response.status_code == 201
            created_user = User(**response.json())
            assert created_user.name == test_user["name"]
            assert created_user.email == test_user["email"]

    @allure.title("Update user")
    def test_update_user(self, api_client, test_user):
        with allure.step("Update user with ID 1"):
            response = api_client.put("/users/1", json=test_user)
            assert response.status_code == 200
            updated_user = User(**response.json())
            assert updated_user.name == test_user["name"]
            assert updated_user.email == test_user["email"]

    @allure.title("Delete user")
    def test_delete_user(self, api_client):
        with allure.step("Delete user with ID 1"):
            response = api_client.delete("/users/1")
            assert response.status_code == 200

    @allure.title("Get non-existent user")
    def test_get_nonexistent_user(self, api_client):
        with allure.step("Try to get user with non-existent ID"):
            response = api_client.get("/users/999")
            assert response.status_code == 404
            error = ErrorResponse(**response.json())
            assert error.status_code == 404 