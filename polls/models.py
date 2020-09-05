from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Customer(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200,blank=True, null=True)
	phone = models.CharField(max_length=200,blank=True, null=True)
	email = models.CharField(max_length=200,blank=True, null=True)
	adress = models.CharField(max_length=1000,blank=True, null=True)
	#profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name



class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			) 

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	

	def __str__(self):
		return self.name


class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name

class contactUs(models.Model):
	STATUS = (
			('help', 'help'),
			('call', 'call'),
			('to join', 'to join'),
			)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return str(self.customer.name)

class AskQua(models.Model):
	STATUS = (
			('imp', 'imp'),
			('spirua', 'spirua'),
			('to join', 'to join'),
			)
	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	qua = models.CharField(max_length=1000,blank=True, null=True)
	ans = models.CharField(max_length=1000,blank=True, null=True)

	def __str__(self):
		return str(self.customer.name)