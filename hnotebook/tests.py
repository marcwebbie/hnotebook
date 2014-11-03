from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_returns_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_has_hnotebook_in_title(self):
        response = self.client.get('/')
        self.assertIn("hnotebook", str(response.content).lower())

    def test_homepage_has_login_string(self):
        response = self.client.get('/')
        self.assertIn("login", str(response.content).lower())
