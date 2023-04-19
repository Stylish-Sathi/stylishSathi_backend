from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

GENDERS = (
    ("MALE", _("Male")),
    ("FEMALE", _("Female")),
    ("OTHER", _("Other")),
)

PHONE_REGEX = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message=_("Phone number must be in international format."),
)


class Client(models.Model):
    firstName = models.CharField(max_length=127)
    lastName = models.CharField(max_length=127)
    phoneNumbers = ArrayField(
        models.CharField(max_length=15, validators=[PHONE_REGEX]),
        blank=False,
        null=False,
    )
    email = models.EmailField(max_length=200)
    gender = models.CharField(choices=GENDERS, max_length=10)
    reg_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.firstName} {self.lastName} ({self.id})"
