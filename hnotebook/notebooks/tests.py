from django.test import TestCase

class ProfileTestCases(TestCase):
    def setUp(self):
        pass

    def test_new_profile_has_no_notebook(self):
        profile = Profile.objects.create(first_name="John", last_name="Doe")
        self.assertEqual(profile.notebooks.count(), 0)
