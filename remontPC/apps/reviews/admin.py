from django.contrib import admin

from .models import Review, ReviewAnswer

admin.site.register(Review)
admin.site.register(ReviewAnswer)