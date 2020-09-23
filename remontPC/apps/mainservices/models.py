from django.db import models
from django.conf import settings


class MainService(models.Model):
    mainservice_name = models.CharField('Название раздела', max_length= 200)
    mainservice_description = models.TextField('Описание раздела')
    mainservice_images = models.ImageField(null = True)
    def __str__(self):
        return self.mainservice_name
    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'

# Create your models here.
