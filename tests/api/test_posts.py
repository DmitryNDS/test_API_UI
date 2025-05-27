import pytest
import allure
from utils.api_client import APIClient
from tests.api.models import Post, ErrorResponse
from faker import Faker

fake = Faker()

# Define maximum acceptable response times (in seconds)
MAX_GET_TIME = 1.0
MAX_POST_TIME = 2.0
MAX_PUT_TIME = 2.0
MAX_DELETE_TIME = 1.0

@pytest.fixture
def api_client():
    return APIClient("https://jsonplaceholder.typicode.com")

@pytest.fixture
def test_post():
    return {
        "title": fake.sentence(),
        "content": fake.paragraph(),
        "user_id": 1
    }

@allure.feature("Post API")
@allure.story("Post Management")
class TestPostAPI:
    
    @allure.title("Get all posts")
    def test_get_posts(self, api_client):
        with allure.step("Get all posts"):
            response = api_client.get("/posts")
            assert response.status_code == 200
            posts = response.json()
            assert isinstance(posts, list)
            assert len(posts) > 0
            assert api_client.check_response_time(response, MAX_GET_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_GET_TIME}s"

    @allure.title("Get post by ID")
    def test_get_post_by_id(self, api_client):
        with allure.step("Get post with ID 1"):
            response = api_client.get("/posts/1")
            assert response.status_code == 200
            post = Post(**response.json())
            assert post.id == 1
            assert api_client.check_response_time(response, MAX_GET_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_GET_TIME}s"

    @allure.title("Get posts by user ID")
    def test_get_posts_by_user(self, api_client):
        with allure.step("Get posts for user ID 1"):
            response = api_client.get("/posts", params={"userId": 1})
            assert response.status_code == 200
            posts = response.json()
            assert isinstance(posts, list)
            assert all(post["userId"] == 1 for post in posts)
            assert api_client.check_response_time(response, MAX_GET_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_GET_TIME}s"

    @allure.title("Create new post")
    def test_create_post(self, api_client, test_post):
        with allure.step("Create new post"):
            response = api_client.post("/posts", json=test_post)
            assert response.status_code == 201
            created_post = Post(**response.json())
            assert created_post.title == test_post["title"]
            assert created_post.content == test_post["content"]
            assert created_post.user_id == test_post["user_id"]
            assert api_client.check_response_time(response, MAX_POST_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_POST_TIME}s"

    @allure.title("Update post")
    def test_update_post(self, api_client, test_post):
        with allure.step("Update post with ID 1"):
            response = api_client.put("/posts/1", json=test_post)
            assert response.status_code == 200
            updated_post = Post(**response.json())
            assert updated_post.title == test_post["title"]
            assert updated_post.content == test_post["content"]
            assert api_client.check_response_time(response, MAX_PUT_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_PUT_TIME}s"

    @allure.title("Delete post")
    def test_delete_post(self, api_client):
        with allure.step("Delete post with ID 1"):
            response = api_client.delete("/posts/1")
            assert response.status_code == 200
            assert api_client.check_response_time(response, MAX_DELETE_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_DELETE_TIME}s"

    @allure.title("Get non-existent post")
    def test_get_nonexistent_post(self, api_client):
        with allure.step("Try to get post with non-existent ID"):
            response = api_client.get("/posts/999")
            assert response.status_code == 404
            error = ErrorResponse(**response.json())
            assert error.status_code == 404
            assert api_client.check_response_time(response, MAX_GET_TIME), \
                f"Response time {response.elapsed_time:.2f}s exceeded maximum {MAX_GET_TIME}s" 