from django.urls import path
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User, Group
from django.contrib.auth import views
from django.contrib.auth.views import *


from users import views

app_name = 'users'

urlpatterns = [
	path('', views.workers, name = 'workers'),
	path('registration', views.registration, name='registration'),
	path('contacts', views.contacts, name='contacts'),
	path('writeus', views.writeus, name='writeus'),
	path('<int:user_id>/', views.client, name='client'),
	path('<int:client_id>/edit/', views.clientedit, name='clientedit'),
	path('password-change/', views.PasswordChangeView.as_view(), name='password_change'),
	path('password-change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),	
	path('password-reset/', views.PasswordResetView.as_view(), name='password_reset'),
	path('password-reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]