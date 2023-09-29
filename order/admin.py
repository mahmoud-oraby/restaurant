from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_filter = ["completed",]


class OrderItemAdmin(admin.ModelAdmin):
    list_filter = ["date_added",]
    list_display = ["order", "product", "quantity", "date_added"]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
