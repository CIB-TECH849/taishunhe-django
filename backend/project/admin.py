from django.contrib import admin
from project.products.models import Product
from project.orders.models import Order, OrderItem

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
