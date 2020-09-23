from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect # Add this
from django.core.mail import *
from users.models import *
from orders.models import *
from .forms import ContactForm 
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User, Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import datetime

def registration(request):
	if request.method == 'POST':
		name = request.POST.get('name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		newuser = User.objects.create_user(username = name, email = email, password = password)
		newuser.save()
		client = Client.create(userobj = newuser, name = newuser.username, email = newuser.email)
		client.save()
		return HttpResponseRedirect('/accounts/login')
	return render(request, 'registration/registration.html')

def contacts(request):
	return render(request, 'contacts/contacts.html')

def writeus(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			sender_name = form.cleaned_data['name']
			sender_email = form.cleaned_data['email']

			message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
			send_mail('New Enquiry', message, sender_email, ['example@example.com'])
			return render(request, 'contacts/rewrite.html')
	else:
		form = ContactForm()

	return render(request, 'contacts/writeus.html', {'form':form})

def workers(request):
	workers_list = Worker.objects.all()
	paginator = Paginator(workers_list, 3)
	page = request.GET.get('page')  
	try:
		workers = paginator.page(page) 
	except PageNotAnInteger:
	 	workers = paginator.page(1)  
	except EmptyPage: 
		workers = paginator.page(paginator.num_pages)  
	return render(request, 'workers/workers.html', {'workers_list':workers_list,'page':page, 'workers':workers})


def client(request, user_id):
	us = User.objects.get(id = user_id)
	cl = Client.objects.get ( user = us)
	order_list = cl.order_set.all()	
	paginator = Paginator(order_list, 2)
	page = request.GET.get('page')  
	try:
		client = paginator.page(page) 
	except PageNotAnInteger:
	 	client = paginator.page(1)  
	except EmptyPage: 
		client = paginator.page(paginator.num_pages)  
	return render(request, 'client/profile.html', {'us':us,'cl':cl,'page':page, 'client':client})

def clientedit(request, client_id):
	cl = Client.objects.get(id = client_id)
	user = cl.user
	userid = str(user.id)
	if request.method == "POST":
		cl.client_name = request.POST.get('clientname')
		cl.client_telephonenumber = request.POST.get('clientphone')
		cl.client_email = request.POST.get('clientemail')
		cl.client_birthdaydate = request.POST.get('clientbd')
		cl.save()
		return redirect('/users/' + userid)
	return render(request, 'client/profileedit.html', {'cl': cl, 'user':user})
