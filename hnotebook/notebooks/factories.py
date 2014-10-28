import random
import factory

from .models import Notebook, Housing

class NotebookFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Notebook

    @factory.Sequence
    def name(n):
        return 'notebook{}'.format(n)

    @factory.Sequence
    def description(n):
        return 'description notebook{}'.format(n)

    private = False

class HousingFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Housing

    notebook          = factory.SubFactory(NotebookFactory)
    category          = random.choice([Housing.RENT, Housing.BUY])
    property_type     = random.choice([Housing.HOUSE, Housing.FLAT])
    description       = "Example description"
    town              = random.choice(
        ["London", 'Tokyo', 'Dakar', 'Casablanca' 'Moscow', 'Quito']
    )
    address           = "123, street example"
    price             = random.randint(500, 10000)
    currency          = "$"
    caution           = random.randint(500, 10000)
    guarantee         = random.randint(500, 10000)
    maintenance_fee   = random.randint(50, 500)
    surface           = random.randint(50, 300)
    floor             = random.randint(1, 40)
    elevator          = random.choice([True, False])
    num_rooms         = 3
    num_bedroom       = 1
    num_restroom      = 1
    num_living_room   = 0
    num_dining_room   = 0
    num_balcony       = random.randint(0, 2)
    num_car_park_slot = random.randint(0, 2)
    kitchen           = 0
    offer_url         = 'http://www.example.com/offer/123'
