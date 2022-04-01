from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
from model_utils.models import TimeSTampedModel

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class BaseModel(TimeStampedModel):
    """
    BaseModel

    An abstract base class model that provides shared default fields and functionalities.
    The BaseModel provides is_active boolean flag for soft delete. It further provides
    created_by and modified_by fields as well as an auditrail by historical models.
    Comment out if an automated auditrail for all tables is not desired.
    """
    # default pk is an integer - overwrite here if required.
    # created is provided by TimeStampedModel
    # modified is provided by TimeStampedModel
    is_active = models.BooleanField(
        default=True,
        help_text='Deactivate to soft delete.'
    )
    created_by = models.Foreignkey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET(get_sentinel_user),
        null=False,
        blank=False,
        verbose_name="created_by",
        related_name="created_by"
    )
    modified_by = models.Foreignkey(
        settings.AUTH_USER_MODEL,
        on_delete = models.SET(get_sentinel_user),
        null=False,
        blank=False,
        verbose_name="last_modified_by",
        related_name="last_modified_by"
    )
    # provides Auditrail
    history = HistoricalRecords()

    class Meta:
        abstract = True