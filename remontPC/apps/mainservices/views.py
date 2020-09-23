from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db import models
from django.conf import settings
from mainservices.models import *
from services.models import *
from django.core.paginator import *

def index(request):
    mainservices_list = MainService.objects.all()
    return render(request, 'mainservices/mainservices.html', {'mainservices_list': mainservices_list})

def mainservicedetail(request, mainservice_id):
    ara = MainService.objects.get ( id = mainservice_id)
    mainserviceser_list = ara.service_set.all()
    search_query = request.GET.get('searchservice', '')
    ascordesc = request.GET.get('searchpriceascdesc', 'По возрастанию')
    orderby = 'service_price'
    if ascordesc == 'по возрастанию':	   
        mainserviceser_list = Service.objects.filter(service_mainservice_id = mainservice_id).order_by(orderby)
    if ascordesc == 'по убыванию': 
        mainserviceser_list = Service.objects.filter(service_mainservice_id = mainservice_id).order_by('-service_price')
    if search_query:
	    mainserviceser_list = Service.objects.filter(service_mainservice_id = mainservice_id, service_name__icontains = search_query).order_by(orderby)
    # else:
	#     mainserviceser_list = MainService.objects.all()     
    paginator = Paginator(mainserviceser_list, 3)
    page = request.GET.get('page')
    try:
        mainservice = paginator.page(page)
    except PageNotAnInteger:
        mainservice = paginator.page(1)
    except EmptyPage:
        mainservice = paginator.page(paginator.num_pages)
    return render(request, 'mainservices/mainservice.html', {'ara':ara, 'mainservice':mainservice, 'ascordesc':ascordesc, 'search_query':search_query})