from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(label='Телефон', max_length=100)
    message = forms.CharField(label='Сообщение', widget=forms.Textarea)

class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')