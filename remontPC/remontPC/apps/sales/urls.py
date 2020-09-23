from django.urls import path

from . import views

app_name = 'sales'

urlpatterns = [
	path('', views.sales, name = 'sales'),
	path('<int:sale_id>/', views.saledetail, name = 'saledetail'),
]