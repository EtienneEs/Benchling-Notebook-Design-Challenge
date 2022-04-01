import pytest
from .factories import tag

pytestmark = pytest.mark.django_db

def test_tag__str__(tag: tag):
    assert tag.__str__() == tag.name
    assert str(tag) == tag.name

def test_tag_get_absolute_url(tag: tag):
    assert tag.get_absolute_url() == f'/tags/{tag.id}/'