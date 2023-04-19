from django.db import models
from Client.models import Client
from Service.models import serviceOffered
# Create your models here.

class Order(models.Model):
    STATUS_CHOICES = [
        ("BOOKED",'Booked'),
        ("ARRIVED",'Arrived'),
        ("ONGOING",'Ongoing'),
        ("COMPLETED",'Completed'),
    ]
    service_offered = models.ManyToManyField(serviceOffered, related_name='servicesOrdered')
    order_created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client, related_name='orderByClient' ,on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="BOOKED")
    start_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id}: {', '.join(str(service) for service in self.service_offered.all())}"