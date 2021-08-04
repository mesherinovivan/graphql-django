from django.db import models
from django.utils.translation import gettext_lazy as _
from core.models import BaseModel


class GenderEnum(models.TextChoices):
    male = "MALE", _("MALE")
    female = "FEMALE", _("FEMALE")
    transgender = "TRANSGENDER", _("TRANSGENDER")


class Contact(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(choices=GenderEnum.choices, default=GenderEnum.male, max_length=11)
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(null=True)
