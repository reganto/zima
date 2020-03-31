from unittest import TestCase
from zima import create_app


class AppModeTestCase(TestCase):
    def setUp(self):
        self.first_app = create_app("testing")
        self.second_app = create_app("development")
        self.third_app = create_app("production")

    def test_app_in_testing(self):
        self.assertTrue(self.first_app.settings["testing"])
      
    def test_app_in_developemt(self):
        self.assertTrue(self.second_app.settings["development"])

    def test_app_in_production(self):
        self.assertTrue(self.third_app.settings["production"])

