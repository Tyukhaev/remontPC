from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime
from django.utils import timezone
from django.conf import settings
from django.db import models
from reviews.models import *
from services.models import *
from users.models import *
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User, Group
from django.core.paginator import *


def reviews(request):
	reviews_list = Review.objects.all()
	search_query = request.GET.get('searchservice', '')
	search_worker = request.GET.get('searchworker', '')
	#servicelist = Service.objects.all()	
	if (search_query) and (search_worker):
		reviews_list = Review.objects.filter(review_service__service_name__icontains = search_query, review_worker__worker_name__icontains = search_worker)		
	elif search_query:
		reviews_list = Review.objects.filter(review_service__service_name__icontains=search_query)
	elif search_worker:
		reviews_list = Review.objects.filter(review_worker__worker_name__icontains = search_worker)						
	paginator = Paginator(reviews_list, 2)
	try: 
		page = int(request.GET.get('page', 1))
	except:
		page = 1
	try:
		reviews = paginator.page(page)
	except(EmptyPage, InvalidPage):
		reviews = paginator.page(paginator.num_pages)
	return render(request, 'reviews/reviews.html', {'reviews_list':reviews_list,'reviews':reviews})

def newreview(request):
	service_list = Service.objects.all()
	workers_list = Worker.objects.all()
	if request.user.is_authenticated:
		try:
			client = Client.objects.get(user = request.user)
			client_name = client.client_name
			email = client.client_email
			telnum = client.client_telephonenumber
			
			if request.method == 'POST':
				client = Client.objects.get(user = request.user)
				client_name = client.client_name
				email = client.client_email
				telnum = client.client_telephonenumber
				wname = request.POST.get('worker')
				worker = Worker.objects.get(worker_name = wname)
				service = Service.objects.get(service_name = request.POST.get('service'))
				text = request.POST.get('comment')
				newreview = Review.objects.create(review_pubdate = datetime.datetime.today(), review_service = service, review_worker = worker, review_client = client, review_telephonenumber = telnum, review_email = email, review_text = text, review_screenshot = 'comments.png')
				newreview.save()
				return HttpResponseRedirect('/reviews')
			return render(request, 'reviews/newreview.html', {'workers_list': workers_list, 'service_list':service_list, 'client_name':client_name, 'email':email, 'telnum':telnum})
		except:
			if request.method == 'POST':
				name = request.POST.get('name')
				email = request.POST.get('email')
				telnum = request.POST.get('telnum')
				wname = request.POST.get('worker')
				worker = Worker.objects.get(worker_name = wname)
				service = Service.objects.get(service_name = request.POST.get('service'))
				text = request.POST.get('comment')
				newreview = Review.objects.create(review_pubdate = datetime.datetime.today(), review_service = service, review_worker = worker, review_name = name, review_telephonenumber = telnum, review_email = email, review_text = text, review_screenshot = 'comments.png')
				newreview.save()
				return HttpResponseRedirect('/reviews')
			return render(request, 'reviews/newreview.html', {'workers_list': workers_list, 'service_list':service_list})
	else:
		if request.method == 'POST':
			if request.method == 'POST':
				name = request.POST.get('name')
				email = request.POST.get('email')
				telnum = request.POST.get('telnum')
				wname = request.POST.get('worker')
				worker = Worker.objects.get(worker_name = wname)
				service = Service.objects.get(service_name = request.POST.get('service'))
				text = request.POST.get('comment')
				newreview = Review.objects.create(review_pubdate = datetime.datetime.today(), review_service = service, review_worker = worker, review_name = name, review_telephonenumber = telnum, review_email = email, review_text = text, review_screenshot = 'comments.png')
				newreview.save()
				return HttpResponseRedirect('/reviews')
	return render(request, 'reviews/newreview.html', {'workers_list': workers_list, 'service_list':service_list})
	