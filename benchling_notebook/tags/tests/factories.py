import pytest
from factory.django import DjangoModelFactory
from factory import Faker, post_generation

from ..models import Tag

def tag():
    return TagFactory()

class TagFactory(DjangoModelFactory):
    """
    Creates a Tag
    """

    class Meta:
        model = Tag
    
    name = Faker('sentence', nb_words=10)
    description = Faker('sentence', nb_words=50)

    @post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of users was provided
            for user in extracted:
                self.users.add(user)