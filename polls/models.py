from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
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
	blogDate=models.DateField(default=timezone.now)
	def __str__(self):
		return self.blogTitle

class articleDetail(models.Model):
	articleName=models.CharField(max_length=200)
	article=models.TextField()
	articleCatagories=models.CharField(max_length=100)
	articleImage=models.ImageField(upload_to="profiles")
	articleKeyword=models.CharField(max_length=200)
	articleAuthor=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	blogAssociated=models.ForeignKey(blogDetails,on_delete=models.CASCADE,default=None)
	articleDate=models.DateField(default=timezone.now)

	def __str__(self):
		return self.articleName

class userSociallink(models.Model):
	sociallinkName=models.CharField(max_length=200)
	sociallink=models.URLField(max_length=200)
	linkUser=models.ForeignKey(User,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.sociallinkName

class comment(models.Model):
	commentBy=models.CharField(max_length=100)
	commentbyEmail=models.CharField(max_length=100)
	commentMsg=models.CharField(max_length=200)
	commentDate=models.DateField(default=timezone.now)
	commentOn=models.ForeignKey(blogDetails,on_delete=models.CASCADE,default=None)

	def __str__(self):
		return self.commentBy

class userSubscriber(models.Model):
	subscriber=models.CharField(max_length=200)
	subscribeTo=models.CharField(max_length=100)

	def __str__(self):
		return self.subscriber


	