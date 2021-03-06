from django.shortcuts import render, redirect
from .models import Profile,dataForward,blogTemplate
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.conf import settings as conf_settings
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail


# Create your views here.
def index(request):
	return render(request=request,template_name="main/home.html")


def index1(request):
	return render(request=request,template_name="main/about.html")

def index11(request):
	return render(request=request,template_name="main/category.html")

def index2(request):
	return render(request=request,template_name="main/contact.html")

def index3(request):
	return render(request=request,template_name="main/createblog.html")

def index4(request):
	return render(request=request,template_name="main/signin.html")

def index5(request):
	return render(request=request,template_name="main/signup.html")

def index6(request):
	return render(request=request,template_name="main/single-audio.html")

def index7(request):
	return render(request=request,template_name="main/single-gallery.html")

def index8(request):
	return render(request=request,template_name="main/single-standard.html")

def index9(request):
	return render(request=request,template_name="main/single-video.html")


def dashboard(request):
	template=request.GET["template"]
	return render(request,"dashboard/index.html" ,{"temp": template})

def main(request):
	return render(request=request,template_name="dashboard/main.html")

def add_article(request):
	return render(request=request,template_name="dashboard/addarticle.html")

def profile(request):
	return render(request=request,template_name="dashboard/profile.html")

def editprofile(request):
	return render(request=request,template_name="dashboard/editprofile.html")

def settings(request):
	return render(request=request,template_name="dashboard/settings.html")

def sidebar(request):
	return render(request=request,template_name="dashboard/mainsidebar.html")
# def index12(request):
# 	return render(request=request,template_name="main/forget-password.html")

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
	email={{user.email}}
	uname={{request.user}}
	country=request.POST["country"]
	city=request.POST["city"]
	phone=request.POST["phone"]
	data=Proile(email=email, name=uname, password=psw, country=country,city=city,phone=phone)
	data.save()
	return render(request,"dashboard/profile.html",{})
	

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
	return render(request,"main/template.html" ,{"users": us})
