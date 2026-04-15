from src.db.core import DB

db = DB()


def test_total_users():
    assert db.get_total_users() == 4

def test_get_users():
    assert isinstance(db.get_users(), dict)