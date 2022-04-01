import pytest
from factory.django import DjangoModelFactory
from factory import Faker, post_generation

from ..models import Project
from ..tags.test.factories import Tagfactory

def project():
    return ProjectFactory()

class ProjectFactory(DjangoModelFactory):
    """
    Creates a Project.
    In order to link users or tags to this Project:
    ProjectFactory.create(users=(user1, user2, user3))
    """
    class Meta:
        model = Project

    name = Faker('sentence', nb_words=10)
    description = Faker('sentence', nb_words=50)
    # decomment if all factory projects should have tags by default
    #tags = factory.RelatedFactoryList(
    #    TagFactory,
    #    size=4,
    #)

    @post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of users was provided
            for user in extracted:
                self.users.add(user)
    
    @post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            # A list of tags was provided
            for tag in extracted:
                self.tags.add(tag)
