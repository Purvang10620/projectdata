from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	email=models.CharField(max_length=50)
	name=models.CharField(max_length=50)
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

	def __str__(self):
		return self.templatename

class blogDetails(models.Model):
	blogName=models.CharField(max_length=200)
	blogTitle=models.CharField(max_length=200)
	blogCatagories=models.CharField(max_length=100)
	blogAuthor=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	template=models.ForeignKey(blogTemplate,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.blogTitle