from django.test import TestCase, Client

class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_returns_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
