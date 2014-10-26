from django.test import TestCase
from .models import Profile

class ProfileTestCases(TestCase):
    def setUp(self):
        self.new_profile = Profile.objects.create(first_name="John", last_name="Doe")

    def test_new_profile_has_no_notebook(self):
        self.assertEqual(self.new_profile.notebooks.count(), 0)

    def test_new_profile_has_zero_bookmarks(self):
        self.assertEqual(self.new_profile.bookmarks.count(), 0)
