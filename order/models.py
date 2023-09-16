from django.db import models
from django.contrib.auth.models import User
from main.models import Menu
import uuid


class Order(models.Model):
    customer = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.customer.username

    def save(self, *args, **kwargs):
        code = str(uuid.uuid4())[:8].replace('-', '').lower()
        print(code)
        self.transaction_id = code
        super(Order, self).save(*args, **kwargs)


class OrderItem(models.Model):
    product = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.order.customer.username}-{self.product.title}'
