from django.test import TestCase
from .models import Profile
from .factories import UserFactory

class ProfileTestCases(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.new_profile = Profile.objects.create(user=self.user)

    def test_new_profile_has_zero_notebooks(self):
        self.assertEqual(self.new_profile.notebooks.count(), 0)

    def test_new_profile_has_zero_bookmarks(self):
        self.assertEqual(self.new_profile.bookmarks.count(), 0)

    def test_new_profile_has_default_picture(self):
        self.assertEqual(self.new_profile.picture, Profile.DEFAULT_PICTURE)

    def test_profile_is_associated_with_user(self):
        self.assertIsInstance(self.new_profile.user, type(self.user))
