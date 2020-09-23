from django import forms
from .models import Order
from users.models import Client
from django.conf import settings
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class OrderCreateForm(forms.ModelForm):
    order_name = forms.CharField(widget=forms.HiddenInput(),required = False)
    order_email = forms.CharField(widget=forms.HiddenInput(),required = False)
    order_telephonenumber = forms.CharField(widget=forms.HiddenInput(),required = False)
    order_address = forms.CharField(label = 'Адресс',max_length=250)
    order_date = forms.DateField(widget=forms.HiddenInput(),required = False)
    order_time = forms.TimeField(widget=forms.HiddenInput(), required = False)
    CashOrCard = forms.BooleanField(widget=forms.HiddenInput(),required = False)
    class Meta:
        model = Order
        fields =['order_name','order_email', 'order_telephonenumber','order_date','order_time',
                    'order_address', 'CashOrCard']
