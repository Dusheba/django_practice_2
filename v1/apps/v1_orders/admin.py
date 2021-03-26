from django.contrib import admin

# Register your models here.
from v1.apps.v1_orders.models import Order

admin.site.register(Order)
