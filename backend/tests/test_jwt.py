from core.security import create_access_token


def test_create_access_token():
    data = {"sub": "somemail@gmail.com"}
    assert create_access_token(data) is not None
    print(create_access_token(data))
