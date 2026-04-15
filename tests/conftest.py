import pytest

@pytest.fixture
def client():
    return {"status": "ok"}