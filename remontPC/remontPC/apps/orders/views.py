from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from users.models import Client
from django.contrib.auth.models import User, Group


def order_create(request):
    cart = Cart(request)
    client_list = Client.objects.all()
    if request.user.is_superuser:
	    return HttpResponseRedirect('/admin/orders/order')
    if request.method == 'POST':
        client = Client.objects.get(user = request.user)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            order.order_client = client
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order, 
                                         service=item['service'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            # очистка корзины
            cart.clear()
            return render(request, 'orders/order/created.html',
                          {'order': order, 'client':client, 'client_list':client_list })
    else:
        form = OrderCreateForm
        client = Client.objects.get(user = request.user)
    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form, 'client':client,'client_list':client_list})