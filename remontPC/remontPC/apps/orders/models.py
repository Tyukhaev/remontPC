from django.db import models
from services.models import Service
from users.models import Client, Worker
from django.conf import settings


class Order(models.Model):
    order_date = models.DateField('Дата заказа')
    order_time = models.TimeField('Время заказа')
    order_client = models.ForeignKey(Client, on_delete = models.CASCADE, null=True, blank=True)
    order_name = models.CharField('Имя(если не зарегстрирован)', max_length = 50, null = True, blank = True)
    order_email = models.CharField('E-mail(если не зарегстрирован)', max_length = 50, null = True, blank = True)
    order_telephonenumber = models.CharField('Телефон(если не зарегстрирован)', max_length = 50, null = True, blank = True)
    order_worker = models.ForeignKey(Worker, on_delete = models.CASCADE, null=True, blank=True)
    order_state = models.CharField('Статус заказа', max_length = 100)
    order_address = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    CashOrCard = models.BooleanField(blank=True, null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete = models.CASCADE, related_name='items')
    service = models.ForeignKey(Service,on_delete = models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity