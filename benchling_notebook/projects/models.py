from django.conf import settings
from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.db import models

from ..utils.models import BaseModel
from ..tags.models import Tag

class Project(BaseModel):
    """
    Project Table
    Stores meta data about the project like name, description etc.
    """
    name = models.CharField(
        max_length=255,
        help_text="Please provide a concise and descriptive Project Name",
        null=False,
        blank=False
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to=Q(
            groups_permissions__codename="can_follow_projects",
        ) | Q(user_permissions__codename="can_follow_projects") | Q(is_superuser=True),
        verbose_name="Users",
        related_name="users",
        blank=True
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name="Tags",
        related_name="tags",
        blank=True
    )

def __str__(self):
    return f'{self.name}'

def get_absolute_url(self):
    return reverse('projects:project_detail', kwargs={'pk': self.pk})


