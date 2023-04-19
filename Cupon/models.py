from django.db import models

# Create your models here.

from django.db import models
from Service.models import serviceOffered

class Cupon(models.Model):
    PERCENT = 'percent'
    AMOUNT = 'amount'
    DISCOUNT_TYPE_CHOICES = [
        (PERCENT, 'Percent'),
        (AMOUNT, 'Amount'),
    ]

    cuponCode = models.CharField(max_length=20, unique=True)
    description = models.TextField()
    servicesOffered = models.ManyToManyField(serviceOffered, related_name='couponOnServices')
    createdAt = models.DateTimeField(auto_now_add=True)
    startAt = models.DateTimeField()
    expiredAt = models.DateTimeField()
    minimumSpend = models.DecimalField(max_digits=10, decimal_places=2)
    discountType = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discountAmount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Coupon {self.code}: {self.description}"
