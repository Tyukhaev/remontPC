from django.urls import path

from . import views

app_name = 'services'

urlpatterns = [
	path('<int:service_id>/', views.servicedetail, name = 'servicedetail'),
]