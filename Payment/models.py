from django.db import models

from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from Order.models import Order
from Cupon.models import Cupon

class Payment(models.Model):
    CASH = 'cash'
    EWALLET = 'ewallet'
    FONEPAY = 'fonepay'
    CARD = 'card'
    PAYMENT_CHOICES = [
        (CASH, _('Cash')),
        (EWALLET, _('E-Wallet')),
        (FONEPAY, _('Fonepay')),
        (CARD, _('Card')),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    order = models.ForeignKey(Order,related_name='paymentForOrder' , on_delete=models.CASCADE)
    coupon = models.ForeignKey(Cupon, related_name='paymentCupon', null=True, blank=True, on_delete=models.SET_NULL)
    payment_gateway = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    payment_key = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.id}: {self.payment_gateway} - {self.order} - {self.payment_key}"
