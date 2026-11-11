import pytest

@pytest.fixture
def test_normal_signup():
    return {
        "email": "test@example.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "TestPassword123!"
    }