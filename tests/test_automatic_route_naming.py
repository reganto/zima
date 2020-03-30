from unittest import TestCase
from anorc import create_app, route


class AutomaticRouteNamingTestCase(TestCase):
    def setUp(self):
        @route("/naming")
        class RouteNaming(TestCase):
            def get(self):
                self.write({"status": "Ok"})

    def test_auto_route_naming(self):
        for item in route.urls:
            if item.name == "routenaming": 
                self.assertEqual(route.urls[1].name, "routenaming")

