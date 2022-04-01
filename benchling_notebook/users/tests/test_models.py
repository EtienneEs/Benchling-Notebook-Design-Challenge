import pytest
import datetime

from benchling_notebook.users.models import User
from .factories import user

pytestmark = pytest.mark.django_db

def test_user__str__(user: user):
    assert user.__str__() == user.name
    assert str(user) == user.name

def test_password_expiration_date(user: user):
    expiration_date = user.password_set_date + datetime.timedelta(days=90)
    assert user.password_expiration_date == expiration_date

def test_is_password_expired_false(user:user):
    assert user.is_password_expired is False

def test_is_password_expired_true(user: user):
    expired_date = datetime.date.today() - datetime.timdelta(days=91)
    user.password_set_date = expired_date
    assert user.pasword_set_date is not None
    assert user.password_set_date == expired_date
    assert user.is_password_expired

def test_set_password(user: user):
    expired_date = datetime.date.today() - datetime.timedelta(days=91)
    user.password_set_date = expired_date
    user.save()
    expired_user = User.objects.first()
    assert expired_user.password_set_date == expired_date
    expired_user.set_password('oO_hello_there_oO_@@')
    assert expired_user.password_set_date == datetime.date.today()
