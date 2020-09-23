from django.db import models
from django.conf import settings
from services.models import Service

class Sale(models.Model):
	sale_name = models.CharField('Название акции', max_length = 100)
	sale_datestart = models.DateTimeField('Дата начала')
	sale_dateend = models.DateTimeField('Дата конца')
	sale_description = models.TextField('Описание')
	sale_image = models.ImageField()
	sale_service = models.ManyToManyField(Service)
	def __str__(self):
		return self.sale_name

	class Meta:
		verbose_name = 'Акция'
		verbose_name_plural = 'Акции'		

