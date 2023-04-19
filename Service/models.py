from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from Salon.models import Salon, SalonImage

from Staff.models import Staff

# Create your models here.
class Icon(models.Model):
    icon = models.ImageField(upload_to="icons/", blank=False)
    iconName = models.CharField(max_length=255, blank=False)

class Service(models.Model):
    title = models.CharField(max_length=255, blank= False, null=False)
    detail = models.TextField(blank= True)
    icon = models.OneToOneField(Icon, related_name="serviceIcon", blank=False, null=False, on_delete=models.CASCADE)

class serviceOffered(models.Model):
    service = models.ForeignKey(Service, related_name = 'servicesOffered', on_delete=models.CASCADE)
    detail = models.TextField(blank=True, null=True)
    serviceImage = models.ForeignKey(SalonImage, related_name='serviceImage', on_delete=models.CASCADE)
    salon = models.ForeignKey(Salon, related_name='serviceOfferedBySalon', on_delete= models.CASCADE)
    staff = models.ForeignKey(Staff, related_name='serviceOfferedByStaff', on_delete= models.CASCADE)
    estimated_time = models.DurationField(null=True, blank=True)