from django.http import HttpResponse, HttpResponseRedirect 
from django.shortcuts import render, redirect
from mainservices.models import *
from sales.models import *
from reviews.models import *




def index(request):
    mainservices_list = MainService.objects.all()
    last_sales_list = Sale.objects.order_by('id')[:4]
    last_reviews_list = Review.objects.order_by('id')[: 2]
    return render(request, 'index.html', {'mainservices_list':mainservices_list, 'last_sales_list':last_sales_list, 'last_reviews_list':last_reviews_list})