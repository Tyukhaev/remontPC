from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
	path('', views.workers, name = 'workers'),
	path('registration', views.registration, name='registration'),
	path('contacts', views.contacts, name='contacts'),
	path('writeus', views.writeus, name='writeus'),
	path('<int:user_id>/', views.client, name='client'),
	path('<int:client_id>/edit/', views.clientedit, name='clientedit'),
]