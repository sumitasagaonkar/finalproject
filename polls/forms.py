from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *



class contactUsForm(ModelForm):
	class Meta:
		model = contactUs
		fields = '__all__'
		
class AskQuaForm(ModelForm):
	class Meta:
		model = AskQua
		fields = '__all__'

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'











