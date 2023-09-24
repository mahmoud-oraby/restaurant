from django.db import models
from order.models import Order
# Create your models here.


class Cart(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.order.customer.username
