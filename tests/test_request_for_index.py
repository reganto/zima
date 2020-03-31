from tornado.testing import AsyncHTTPTestCase
from zima import create_app


class IndexTestCase(AsyncHTTPTestCase):
    def get_app(self):
        return create_app("testing")

    def test_homepage(self):
        response = self.fetch("/")
        self.assertEqual(response.code, 200)
        self.assertIn("success", response.body.decode())

