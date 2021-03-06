from django.db import models

# Create your models here.

class Profile(models.Model):
	email=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
	password=models.CharField(max_length=20)
	gender=models.CharField(max_length=50)
	country=models.CharField(max_length=50)
	city=models.CharField(max_length=50)
	phone=models.BigIntegerField()

class dataForward(models.Model):
	yourname=models.CharField(max_length=50)
	youremail=models.CharField(max_length=50)
	websitename=models.CharField(max_length=50)
	yourmessage=models.CharField(max_length=100)

class blogTemplate(models.Model):
	templatename=models.CharField(max_length=200)
	templateimg=models.ImageField(upload_to="profiles")


