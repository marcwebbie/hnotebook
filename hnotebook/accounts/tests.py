from django.test import TestCase
from .models import Profile

class ProfileTestCases(TestCase):
    def setUp(self):
        pass

    def test_new_profile_has_no_notebook(self):
        profile = Profile.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(profile.notebooks.count(), 0)

    def test_new_profile_has_zero_bookmarks(self):
        profile = Profile.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(profile.bookmarks.count(), 0)
