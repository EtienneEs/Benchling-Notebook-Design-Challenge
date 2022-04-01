import pytest
from typing import Any, Sequence

from django.contrib.auth import get_user_model
import django.contrib.auth.models as auth_models
from django.contrib.auth.models import Permission
from factory.django import DjangoModelFactory
from factory import Faker, post_generation


pytestmark = pytest.mark.django_db

@pytest.fixture
def user():
    return UserFactory



class UserFactory(DjangoModelFactory):

    username = Faker("user_name")
    email = Faker("email")
    name = Faker("name")

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True
                ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)
    
    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
    
    @post_generation
    def groups(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for group in extracted:
                self.groups.add(group)

    @post_generation
    def perms(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            perms = [
                Permission.objects.get(
                    content_type__app_label=p.split(".")[0], codename=p.split(".")[1]
                )
                for p in extracted
            ]
            self.user_permissions.add(*perms)