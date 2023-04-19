from django.db import models
from django.contrib.postgres.fields import ArrayField
from Salon.models import Salon
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.

GENDERS = (
    ("MALE", _("Male")),
    ("FEMALE", _("Female")),
    ("OTHER", _("Other")),
)

PHONE_REGEX = RegexValidator(
    regex=r"^\+?1?\d{9,15}$",
    message=_("Phone number must be in international format."),
)

class Staff(models.Model):
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null = False)
    phoneNumbers = ArrayField(
        models.CharField(max_length=15, validators=[PHONE_REGEX]),
        blank=False,
        null=False,
    )
    email = models.EmailField(max_length=200, blank =True)
    gender = models.CharField(
            choices =  GENDERS,
            max_length = 10,
            blank=False
            )
    salon = models.ForeignKey(Salon, related_name='staffOfSalon',on_delete=models.CASCADE)
    reg_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/')
    # workDays = (
    #     "Sunday", "Monday", "Tuesday", 
    #     "Wednesday", "Thursday", "Friday", 
    #     "Saturday"
    # )

    def __str__(self):
        id = self.id
        return f"{self.firstName} {self.lastName}({id})"
    