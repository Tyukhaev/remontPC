from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.db import models
from django.conf import settings
from services.models import Service
from reviews.models import Review
from mainservices.models import MainService
from sales.models import Sale
from django.core.paginator import *
from cart.forms import CartAddServiceForm

def servicedetail(request, service_id):	
    s = Service.objects.get( id = service_id )	
    mainserviceservices_list = Service.objects.filter( service_mainservice = s.service_mainservice )
    salesserviceservices_list = Sale.objects.filter( sale_service = s )
    servicereviews_list = Review.objects.filter(review_service = s)  
    service_list = get_object_or_404(Service, id=service_id)    
    cartservice_form = CartAddServiceForm()
    paginator = Paginator(servicereviews_list, 2)
    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)
    return render(request, 'services/service.html', {'s':s, 'servicereviews_list':servicereviews_list, 'mainserviceservices_list':mainserviceservices_list, 'salesserviceservices_list':salesserviceservices_list,'cartservice_form':cartservice_form, 'reviews': reviews, 'service_list':service_list})
