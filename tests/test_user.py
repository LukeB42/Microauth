from microauth.resources.user import User


class TestUser(object):
    def test_jsonify(self):
        user = User("ayrx", "terrycwk1994@gmail.com", "Terry", "password")
        assert user.jsonify() == {
            "username": "ayrx",
            "name": "Terry",
            "email": "terrycwk1994@gmail.com"
        }
