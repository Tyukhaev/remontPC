from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.db import models
from django.conf import settings
from sales.models import Sale
from django.core.paginator import *

def sales(request):
	sales_list = Sale.objects.all()
	paginator = Paginator(sales_list, 4)
	page = request.GET.get('page')
	try: 
		sales = paginator.page(page)
	except PageNotAnInteger:
		sales = paginator.page(1)
	except EmptyPage:
		sales = paginator.page(paginator.num_pages)
	return render(request, 'sales/sales.html',{'sales_list':sales_list, 'page':page, 'sales':sales})

def saledetail(request, sale_id):
	try:
		s = Sale.objects.get( id = sale_id )
		service_list = s.sale_service.all()
		paginator = Paginator(service_list, 3)
		page = request.GET.get('page')
		try: 
			salesservice = paginator.page(page)
		except PageNotAnInteger:
			salesservice = paginator.page(1)
		except EmptyPage:
			salesservice = paginator.page(paginator.num_pages)		
		return render(request, 'sales/sale.html',{'s':s, 'service_list':service_list, 'salesservice':salesservice})
	except:
		raise Http404("Акция не найдена!")

