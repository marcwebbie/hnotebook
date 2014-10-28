from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from .models import Profile

import factory

class UserFactory(factory.DjangoModelFactory):
    FACTORY_FOR = User
    FACTORY_DJANGO_GET_OR_CREATE = ('username',)

    first_name = factory.LazyAttribute(lambda o: 'John')
    last_name = factory.LazyAttribute(lambda o: 'Doe')
    password = make_password('password')

    @factory.Sequence
    def username(n):
        return 'user{}'.format(n)

    email = factory.LazyAttribute(lambda o: '{0.username}@example.com'.format(o))

class ProfileFactory(factory.DjangoModelFactory):
    FACTORY_FOR = Profile

    user = factory.SubFactory(UserFactory)
    picture = Profile.DEFAULT_PICTURE
