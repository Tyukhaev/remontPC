from django.urls import path

from . import views

app_name = 'mainservices'

urlpatterns = [
	path('', views.index, name = 'index'),
	path('<int:mainservice_id>/', views.mainservicedetail, name = 'mainservicedetail'),
]