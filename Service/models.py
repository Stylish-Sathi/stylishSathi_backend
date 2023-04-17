from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=255, blank= False, null=False)
    detail = models.TextField(max_length=1023, blank= True)
    