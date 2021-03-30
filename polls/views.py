from django.shortcuts import render, redirect
from .models import Profile,dataForward,blogTemplate,blogDetails,articleDetail,userSociallink,userSubscriber,comment
from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import resolve
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.conf import settings as conf_settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):
	return render(request=request,template_name="main/home.html")


def index1(request):
	return render(request=request,template_name="main/about.html")

def index11(request):
	cat=request.GET["cat"]
	blog=blogDetails.objects.filter(blogCatagories=cat)
	# articleid=articleDetail.objects.filter(articleAuthor=by)
	# return render(request=request,template_name="dashboard/userblogdetails.html")
	return render(request,"main/category.html" ,{"blog": blog})
	

def index2(request):
	return render(request=request,template_name="main/contact.html")

def index3(request):
	return render(request=request,template_name="main/createblog.html")

def index4(request):
	return render(request=request,template_name="main/signin.html")

def index5(request):
	return render(request=request,template_name="main/signup.html")

def solo_templete(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		return render(request,"main/solo.html" ,{"aid": aid ,"bid":bid ,"com":com ,"comno":comno })
	else:
		return render(request=request,template_name="main/solo.html")

def index6(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.get(blogAssociated=bid)
		return render(request,"main/single-audio.html" ,{"aid": aid ,"bid":bid})
	else:
		return render(request=request,template_name="main/single-audio.html")

def index7(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.get(blogAssociated=bid)
		return render(request,"main/single-gallery.html" ,{"aid": aid ,"bid":bid})
	else:
		return render(request=request,template_name="main/single-gallery.html")

def index8(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=blog).count()
		return render(request,"main/single-standard.html" ,{"aid": aid ,"bid":bid ,"com":com})
	else:
		return render(request=request,template_name="main/single-standard.html")

# def templateImage(request):
# 	us=blogTemplate.objects.all()
# 	template_paginator = Paginator(us, 6)
# 	page_num = request.GET.get('page')
# 	page = template_paginator.get_page(page_num)

# 	return render(request,"main/template.html" ,{"page": page})

def add_subscriber(request):
	subEmail=request.POST["EMAIL"]
	subTo=request.POST["name"]
	subData=userSubscriber(subscriber=subEmail,subscribeTo=subTo)
	subData.save()
	return redirect('')


def index9(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.get(blogAssociated=bid)
		return render(request,"main/single-video.html" ,{"aid": aid ,"bid":bid})
	else:
		return render(request=request,template_name="main/single-video.html")

def useraccount(request):
	author=request.user
	articleid=articleDetail.objects.filter(articleAuthor=author)
	linkid=userSociallink.objects.filter(linkUser=author)
	return render(request,"dashboard/useraccount.html" ,{"articleid": articleid ,"linkid": linkid})

def userblogdetail(request):
	by=request.user
	userblog=blogDetails.objects.filter(blogAuthor=by)
	# articleid=articleDetail.objects.filter(articleAuthor=by)
	# return render(request=request,template_name="dashboard/userblogdetails.html")
	return render(request,"dashboard/userblogdetails.html" ,{"userblog": userblog})


def sociallink(request):

	sname=request.POST["sname"]
	slink=request.POST["slink"]
	linkby=request.user

	link=userSociallink(sociallinkName=sname,sociallink=slink,linkUser=linkby)
	link.save()
	return redirect('/myaccount')

def dashboard(request):
	author=request.user
	articleid=articleDetail.objects.filter(articleAuthor=author)
	template=request.GET["template"]
	return render(request,"dashboard/index.html" ,{"temp": template,"articleid": articleid})

def main(request):
	return render(request=request,template_name="dashboard/main.html")

def add_article(request):
	author=request.user
	blogid=blogDetails.objects.filter(blogAuthor=author)
	return render(request,"dashboard/addarticle.html" ,{"blogid":blogid})
	# return render(request=request,template_name="dashboard/addarticle.html")
def viewarticle(request):
	author=request.user
	viewarticle_id=request.GET['articleId']
	aid=articleDetail.objects.get(id=viewarticle_id)
	return render(request,"dashboard/viewarticle.html" ,{"aid":aid})

def article_details(request):
	articlename=request.POST["articlename"]
	articlecontent=request.POST["articlecontent"]
	articlecatagory=request.POST["articlecatagory"]
	image=request.FILES['articleimage']
	keyword=request.POST["keyword"]
	articleauthor=request.user
	articleblog=request.POST["articleblog"]
	blognameid=blogDetails.objects.get(id=articleblog)
	articles=articleDetail(articleName=articlename,article=articlecontent,articleCatagories=articlecatagory,articleImage=image,articleKeyword=keyword,articleAuthor=articleauthor,blogAssociated=blognameid)
	articles.save()
	return redirect('/myaccount')

def profile(request):
	author=request.user
	linkid=userSociallink.objects.filter(linkUser=author)
	subscriber=userSubscriber.objects.filter(subscribeTo=author).count()
	
	return render(request,"dashboard/profile.html" ,{"linkid": linkid ,"sub":subscriber})
	

def editprofile(request):
	return render(request=request,template_name="dashboard/editprofile.html")

def settings(request):
	author=request.user
	linkid=userSociallink.objects.filter(linkUser=author)
	return render(request,"dashboard/settings.html" ,{"linkid": linkid})

def sidebar(request):
	return render(request=request,template_name="dashboard/mainsidebar.html")

def blog_details(request):
	return render(request=request,template_name="dashboard/blogdetails.html")

# def index13(request):
# 	return render(request=request,template_name="main/resetpassword.html")

def getdata(request):
	
	if request.method=='POST':
		email=request.POST["email"]
		name=request.POST["name"]
		psw=request.POST["password"]
		# gen=request.POST["gender"]
		# country=request.POST["country"]
		# city=request.POST["city"]
		# phone=request.POST["phone"]
		if User.objects.filter(username=name).exists():
			messages.info(request,'username taken..')
			return redirect('/signup')
		else :
			user=User.objects.create_user(username=name,password=psw,email=email)
			user.save()
			# print('done')
			return redirect('/signin')
	else:
		return render(request, "main/signup.html",{}) 

	# if request.method=='POST':
	# 	email=request.POST["email"]
	# 	name=request.POST["name"]
	# 	psw=request.POST["password"]
	# 	gen=request.POST["gender"]
	# 	country=request.POST["country"]
	# 	city=request.POST["city"]
	# 	phone=request.POST["phone"]
	# 	data=User(email=email, name=name, password=psw, gender=gen, country=country,city=city,phone=phone)
	# 	data.save()
	# 	return render(request,"main/signin.html",{})
	# else:
	# 	return render(request,"main/signup.html",{})
def profile_add(request):
	#print("email=",request["email"])

	email=request.POST["email"]
	uname=request.POST["uname"]
	country=request.POST["country"]
	city=request.POST["city"]
	phone=request.POST["phone"]
	data=Profile(email=email,name=uname, country=country,city=city,phone=phone)
	data.save()
	return redirect('/profile')
	
def blog_add(request):
	
	blogname=request.POST["blogname"]
	blogtitle=request.POST["title"]
	blogcat=request.POST["blogcatagory"]
	author=request.user
	temp=request.POST["template"]
	tempid=blogTemplate.objects.get(templatename=temp)
	data=blogDetails(blogName=blogname,blogTitle=blogtitle, blogCatagories=blogcat,blogAuthor=author,template=tempid)
	data.save()	
	return redirect('/myaccount')

def login(request):
	if request.method=='POST':
		name=request.POST["name"]
		psw=request.POST["password"]

		user =auth.authenticate(username=name,password=psw)

		if user is not None:
			auth.login(request, user)
			messages.success(request,'success fully logged in')
			return redirect('/home')
			
		else:
			messages.error(request,'invaliid Username or password')
			return redirect('/signin')

	else:
		return render(request,"main/home.html",{})

def handlelogout(request):
	logout(request)
	# messages.success(request, "successfully loggedout")
	return redirect('/home')
	return HttpResponse('handlelogout')

# def sendemail(request):
# 	email=request.POST["email"]
# 	subject = 'Request to change password'
# 	message = f'To initiate the password reset process for your Blogbook Account, click the link below: http://127.0.0.1:8000/resetpassword'
# 	email_from = settings.EMAIL_HOST_USER 
# 	recipient_list = [email, ]
# 	send_mail( subject, message, email_from, recipient_list )
# 	messages.success(request, "We've emailed you for setting your password, if you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder.")
# 	return redirect('/forget')

# def change_password(request):
# 	if request.method == 'POST':
#         form = PasswordChangeForm(request.user, request.POST)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user)  # Important!
#             messages.success(request, 'Your password was successfully updated!')
#             return redirect('/resetpassword')
#         else:
#             messages.error(request, 'Please correct the error below.')
#             return redirect('/resetpassword')
#     else:
#         form = PasswordChangeForm(request.user)

def dataSend(request):
	
	yourname=request.POST["cName"]
	youremail=request.POST["cEmail"]
	websitename=request.POST["cWebsite"]
	yourmessage=request.POST["cMessage"]
	data=dataForward(yourname=yourname, youremail=youremail, websitename=websitename, yourmessage=yourmessage)
	data.save()
	subject = 'Thanks for contacting us'
	message = f'Thank you for contacting us, our team will soon respond you.'
	email_from = conf_settings.EMAIL_HOST_USER 
	recipient_list = [youremail, ]
	send_mail( subject, message, email_from, recipient_list )
	return redirect('/contact')

def templateImage(request):
	us=blogTemplate.objects.all()
	template_paginator = Paginator(us, 4)
	page_num = request.GET.get('page')
	page = template_paginator.get_page(page_num)

	return render(request,"main/template.html" ,{"page": page})
