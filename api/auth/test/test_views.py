import json
import unittest

import be

be.app.testing = True


class TestLogin(unittest.TestCase):
    with app.test_client() as client:
        post_body = {
            'email': 'user@test.com',
            'password': 'an_incorrect_password',
        }
        result = client.post(
            'api/v1/login',
            data=post_body
        )

        self.assertEqual(result.status_code, 401)
