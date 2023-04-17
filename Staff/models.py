from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Staff(models.Model):
    firstName = models.CharField(max_length=255, blank=False, null=False)
    lastName = models.CharField(max_length=255, blank=False, null = False)
    genders = (
        ("MALE", "male"),
        ("FEMALE", "female"),
        ("OTHER", "other"),
    )
    phoneNumbers = ArrayField(models.CharField(max_length=15), blank=False, null= False)
    email = models.EmailField(max_length=200, blank =True)
    gender = models.CharField(
            choices =  genders,
            max_length = 10,
            blank=False
            )
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        id = self.id
        return f"{self.firstName} {self.lastName}({id})"
    