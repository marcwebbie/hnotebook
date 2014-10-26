import factory
from .models import Notebook

class NotebookFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Notebook

    @factory.Sequence
    def name(n):
        return 'notebook{}'.format(n)

    @factory.Sequence
    def description(n):
        return 'description notebook{}'.format(n)
