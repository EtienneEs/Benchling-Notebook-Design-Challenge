import pytest
from .factories import project

pytestmark = pytest.mark.django_db

def test_project__str__(project: project):
    assert project.__str__() == project.name
    assert str(project) == project.name

def test_project_get_absolute_url(project: project):
    assert project.get_absolute_url() == f'/projects/{project.id}/'
