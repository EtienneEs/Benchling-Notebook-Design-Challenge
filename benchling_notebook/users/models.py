from datetime import timedelta, date
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(_("Name of User"), blank=False, max_length=255)
    email = models.EmailField(_('email address'), unique=True, null=True)
    password_set_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def password_expiration_date(self):
        if self.password_set_date:
            return self.password_set_date + timedelta(days=90)

    def set_password(self, *args, **kwargs):
        self.password_set_date = date.today()
        super(User, self).set_password(*args, **kwargs)

    @property
    def is_password_expired(self):
        if self.password_expiration_date:
            return self.password_expiration_date < date.today()
        else:
            return False
