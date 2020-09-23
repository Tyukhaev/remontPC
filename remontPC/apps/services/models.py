from django.db import models
from django.conf import settings
from mainservices.models import MainService

class Service(models.Model):
    service_name = models.CharField('Название услуги', max_length = 200)
    service_mainservice = models.ForeignKey(MainService, on_delete = models.CASCADE, null =True)
    service_price = models.FloatField('Цена услуги')
    service_description = models.TextField('Описание услуги')
    service_averagetime = models.IntegerField('Среднее время')
    service_images = models.ImageField(null = True)
    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'