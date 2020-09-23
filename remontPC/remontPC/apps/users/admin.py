from django.contrib import admin

from .models import Worker, Client

admin.site.register(Worker)
admin.site.register(Client)
