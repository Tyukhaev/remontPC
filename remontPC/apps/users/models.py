from django.db import models
from django.contrib.auth.models import User
import datetime
from django.contrib.auth.views import *
# Create your models here.

class Worker(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	worker_name = models.CharField('ФИО Работника', max_length = 100)
	worker_telephonenumber = models.CharField('Номер телефона', max_length = 11)
	worker_password = models.CharField('Пароль Работника', max_length = 200)
	worker_email = models.EmailField('E-mail')
	worker_birthdaydate = models.DateField('Дата рождения')
	worker_image = models.ImageField()
	def __str__(self):
		return self.worker_name

	class Meta:
		verbose_name = 'Работник'
		verbose_name_plural = 'Работники'


class Client(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
	client_name = models.CharField('ФИО', max_length = 100)
	client_password = models.CharField('Пароль клиента', max_length = 200)
	client_telephonenumber = models.CharField('Номер телефона', max_length = 11, null = True , blank = True)
	client_email = models.EmailField('E-mail')
	client_birthdaydate = models.DateField('Дата рождения', null = True , blank = True)

	def __str__(self):
		return self.client_name
	@classmethod
	def create(cls,userobj, passwd, name,email):
		client = cls(user = userobj, client_name = name, client_password = passwd, client_email = email)
		return client		

	class Meta:
		verbose_name = 'Клиент'
		verbose_name_plural = 'Клиенты'		
		