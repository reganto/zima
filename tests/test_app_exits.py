from unittest import TestCase
from anorc import create_app


class AppExistTestCase(TestCase):
    def setUp(self):
        self.app = create_app("testing")

    def test_app_exists(self):
        self.assertIsNotNone(self.app)

    def tearDown(seld):
        pass 

