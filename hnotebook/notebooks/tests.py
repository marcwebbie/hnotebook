from django.test import TestCase

from .factories import NotebookFactory
from .models import Notebook, Housing

class NotebookModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_notebook_private_field_is_false_as_default(self):
        notebook = Notebook.objects.create(name='testnotebook')
        self.assertEqual(notebook.private, False)

    def test_notebook_string_representation_shows_name(self):
        notebook = Notebook.objects.create(name='testnotebook')
        self.assertIn("testnotebook", str(notebook))

class HousingModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_housing_instantiation(self):
        notebook = NotebookFactory()
        housing = Housing(
            notebook=notebook,
            category=Housing.RENT,
            property_type=Housing.FLAT,
            description="example description",
            town="Some city",
            address="Some address",
            price="700",
            currency="$",
            surface=50,
            num_rooms=2,
        )

        self.assertIn("Rent", str(housing))
        self.assertIn("Flat", str(housing))
        self.assertIn("$", str(housing))
        self.assertIn("700", str(housing))
