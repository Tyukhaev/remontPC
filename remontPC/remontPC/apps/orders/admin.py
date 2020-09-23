from django.contrib import admin
from .models import Order, OrderItem
from users.models import Client, Worker


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['service']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'order_date','order_time', 'order_client', 'order_name',
                    'order_email', 'order_telephonenumber', 'order_worker', 'order_state',
                    'order_address', 'created', 'updated', 'paid', 'CashOrCard']
    list_filter = ['paid', 'created', 'updated', 'order_date', 'CashOrCard', 'order_state']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)