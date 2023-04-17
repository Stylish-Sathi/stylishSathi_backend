from django.db import models

# Create your models here.
class Log(models.Model):
    title = models.CharField(max_length=255, blank=False)
    details = models.TextField(max_length= 1023, blank=False)