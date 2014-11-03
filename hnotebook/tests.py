from django.core.urlresolvers import resolve
from django.test import TestCase, Client

from . import views


class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_returns_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_has_hnotebook_in_title(self):
        response = self.client.get('/')
        self.assertIn("homepage", str(response.content).lower())

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, views.homepage)

    def test_homepage_has_login_string(self):
        response = self.client.get('/')
        self.assertIn("login", str(response.content).lower())

    def test_homepage_has_login_string(self):
        response = self.client.get('/')
        self.assertIn("sign up", str(response.content).lower())
