from django.test import TestCase

from .factories import NotebookFactory
from .models import Notebook

class NotebookModelTestCase(TestCase):
    def setUp(self):
        pass

    def test_notebook_private_field_is_false_as_default(self):
        notebook = Notebook.objects.create(name='testnotebook')
        self.assertEqual(notebook.private, False)

    # test notebook names shouldnt contain spaces
