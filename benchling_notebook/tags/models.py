from django.conf import settings
from django.db import models

from ..utils.models import BaseModel

class Tag(BaseModel):
    """
    Tag Table
    Tags can be used to classify and label projects.
    Tags can be used for newsfeeds/notifications for users with
    interestes in specific topics.
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
    # to allow users to follow specific project types associated with this tag.
    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to=Q(
            groups_permissions__codename="can_follow_tags",
        ) | Q(user_permissions__codename="can_follow_tags") | Q(is_superuser=True),
        verbose_name="Users",
        related_name="users",
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
