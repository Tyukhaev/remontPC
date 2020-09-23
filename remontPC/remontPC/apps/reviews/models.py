from django.db import models
from users.models import Client, Worker
from services.models import Service


class Review(models.Model):
	review_pubdate = models.DateTimeField('Дата публикации')
	review_service = models.ForeignKey(Service, on_delete = models.CASCADE)
	review_worker = models.ForeignKey(Worker, on_delete = models.CASCADE)
	review_client = models.ForeignKey(Client, on_delete = models.CASCADE, null = True, blank = True)
	review_name = models.CharField('Имя(если не зарегстрирован)', max_length = 50, null = True, blank = True)
	review_telephonenumber = models.CharField('Номер телефона', max_length = 11)
	review_email = models.EmailField('E-mail')
	review_text = models.TextField('Текст отзыва')
	review_screenshot = models.FileField('Скриншот')
	class Meta:
		verbose_name = 'Отзыв'
		verbose_name_plural = 'Отзывы'		

class ReviewAnswer(models.Model):
	reviewanswer_author = models.ForeignKey(Worker, on_delete = models.CASCADE)
	reviewanswer_review = models.ForeignKey(Review, on_delete = models.CASCADE)
	reviewanswer_text = models.TextField('Текст')

	class Meta:
		verbose_name = 'Ответ'
		verbose_name_plural = 'Ответы'	