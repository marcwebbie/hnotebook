from django.core.urlresolvers import resolve, reverse
from django.test import TestCase, Client

from . import views


class HomePageTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_root_url_returns_home_page(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

    def test_homepage_has_hnotebook_in_title(self):
        response = self.client.get(reverse('homepage'))
        self.assertIn("homepage", str(response.content).lower())

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve(reverse('homepage'))
        self.assertEqual(found.func, views.homepage)

    def test_homepage_has_login_string(self):
        response = self.client.get(reverse('homepage'))
        self.assertIn("login", str(response.content).lower())

    def test_homepage_has_login_string(self):
        response = self.client.get(reverse('homepage'))
        self.assertIn("sign up", str(response.content).lower())

    def test_login_url_renders_login_template(self):
        found = resolve(reverse('login'))
        self.assertEqual(found.kwargs['template_name'], 'login.html')

    def test_homepage_has_login_string(self):
        response = self.client.get(reverse('signup'))
        self.assertIn("sign up", str(response.content).lower())
