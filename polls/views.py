from django.shortcuts import render, redirect
from .models import userProfile,dataForward,blogTemplate,blogDetails,articleDetail,userSociallink,userSubscriber,comment,categories,ReportedBlog
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
from django.db.models import Q
from datetime import datetime, timedelta


# Create your views here.
def index(request):
	article=blogDetails.objects.all().order_by("-id")[:10]
	return render(request,"main/home.html" ,{"article":article })


def index1(request):
	return render(request=request,template_name="main/about.html")

def index3(request):
	cat=categories.objects.all()
	return render(request,"main/createblog.html" ,{"cat":cat })





# def templateImage(request):
# 	us=blogTemplate.objects.all()
# 	template_paginator = Paginator(us, 6)
# 	page_num = request.GET.get('page')
# 	page = template_paginator.get_page(page_num)

# 	return render(request,"main/template.html" ,{"page": page})

#User Dashboard
def add_subscriber(request):
	subEmail=request.POST["EMAIL"]
	subTo=request.POST["name"]
	blogIn=request.POST["title"]
	id=User.objects.get(username=subTo)
	bid=blogDetails.objects.get(blogTitle=blogIn)
	subData=userSubscriber(subscriber=subEmail,subscribeTo=subTo)
	subData.save()
	return redirect(f"/{bid.template.templatename}?blogtitle={bid.blogTitle}")

def useraccount(request):
	author=request.user
	blogid=blogDetails.objects.filter(blogAuthor=author)
	articleid=articleDetail.objects.filter(articleAuthor=author)
	linkid=userSociallink.objects.filter(linkUser=author)
	time_threshold = datetime.now()
	for i in blogid:
		comm=comment.objects.filter(commentOn=i,commentDate=time_threshold)
	results = userSubscriber.objects.filter(subscribeTo=author,AddOn=time_threshold)
	return render(request,"dashboard/useraccount.html" ,{"articleid": articleid ,"linkid": linkid,"comm":comm ,"result":results})

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

def profile(request):
	author=request.user
	blogid=blogDetails.objects.filter(blogAuthor=author).count()
	articleid=articleDetail.objects.filter(articleAuthor=author).count()
	linkid=userSociallink.objects.filter(linkUser=author)
	subscriber=userSubscriber.objects.filter(subscribeTo=author).count()
	s=userSubscriber.objects.filter(subscribeTo=author)
	if userProfile.objects.filter(username=author).exists():
		udetails=userProfile.objects.get(username=author)
		return render(request,"dashboard/profile.html" ,{"linkid": linkid ,"sub": subscriber, "s": s,"blogid":blogid,"articleid":articleid,"udetails":udetails})
	else:
		return render(request,"dashboard/profile.html" ,{"linkid": linkid ,"sub": subscriber, "s": s,"blogid":blogid,"articleid":articleid})
	

def editprofile(request):
	uname=request.user
	if userProfile.objects.filter(username=uname).exists():
		udetails=userProfile.objects.get(username=uname)
		return render(request,"dashboard/editprofile.html" ,{"uname":uname,"udetails":udetails})
	else:
		return render(request,"dashboard/editprofile.html" ,{"uname":uname})

def updateprofile(request):
	uname=request.user
	if userProfile.objects.filter(username=uname).exists():
		udetails=userProfile.objects.get(username=uname)
		if request.POST:
			udetails.city=request.POST["city"]
			udetails.country=request.POST["country"]
			udetails.phone=request.POST["phone"]
			if request.FILES:
				udetails.profilepic=request.FILES["profilepic"]
			udetails.save()
			return redirect("/myaccount")
	else:
		username=uname
		city=request.POST["city"]
		country=request.POST["country"]
		phone=request.POST["phone"]
		if request.FILES:
			pic=request.FILES["profilepic"]
			info=userProfile(username=username,city=city,country=country,phone=phone,profilepic=pic)
		else:
			info=userProfile(username=username,city=city,country=country,phone=phone)
		info.save()
		return redirect("/myaccount")


def settings(request):
	author=request.user
	linkid=userSociallink.objects.filter(linkUser=author)
	return render(request,"dashboard/settings.html" ,{"linkid": linkid})

def sidebar(request):
	return render(request=request,template_name="dashboard/mainsidebar.html")
# def main(request):
# 	return render(request=request,template_name="dashboard/main.html")


#Comment Module
def add_comment(request):
	cname=request.POST["cName"]
	
	cmessage=request.POST["cMessage"]
	con=request.POST["cOn"]
	bid=blogDetails.objects.get(blogTitle=con)
	comm=comment(commentBy=cname,commentMsg=cmessage,commentOn=bid)
	comm.save()
	return redirect(f"/{bid.template.templatename}?blogtitle={bid.blogTitle}")








# def sendemail(request):
# 	email=request.POST["email"]
# 	subject = 'Request to change password'
# 	message = f'To initiate the password reset process for your Blogbook Account, click the link below: http://127.0.0.1:8000/resetpassword'
# 	email_from = settings.EMAIL_HOST_USER 
# 	recipient_list = [email, ]
# 	send_mail( subject, message, email_from, recipient_list )
# 	messages.success(request, "We've emailed you for setting your password, if you don't receive an email, please make sure you've entered the address you registered with, and check your spam folder.")
# 	return redirect('/forget')

# Contact Us Page
def index2(request):
	return render(request=request,template_name="main/contact.html")

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

#template management Module

def solo_templete(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		sociallink=userSociallink.objects.filter(linkUser=bid.blogAuthor)
		return render(request,"main/solo.html" ,{"aid": aid ,"bid":bid ,"com":com ,"comno":comno,"sociallink":sociallink })
	else:
		return render(request=request,template_name="main/solo.html")

def index6(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		return render(request,"main/single-audio.html" ,{"aid": aid ,"bid":bid,"com":com ,"comno":comno})
	else:
		return render(request=request,template_name="main/single-audio.html")

def index7(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		return render(request,"main/single-gallery.html" ,{"aid": aid ,"bid":bid,"com":com ,"comno":comno})
	else:
		return render(request=request,template_name="main/single-gallery.html")

def index8(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		
		return render(request,"main/single-standard.html" ,{"aid": aid ,"bid":bid ,"com":com,"comno":comno})
	else:
		return render(request=request,template_name="main/single-standard.html")

def index9(request):
	if request.GET:
		title=request.GET["blogtitle"]
		bid=blogDetails.objects.get(blogTitle=title)
		aid=articleDetail.objects.filter(blogAssociated=bid)
		com=comment.objects.filter(commentOn=bid)
		comno=comment.objects.filter(commentOn=bid).count()
		return render(request,"main/single-video.html" ,{"aid": aid ,"bid":bid,"com":com ,"comno":comno})
	else:
		return render(request=request,template_name="main/single-video.html")

def templateImage(request):
	us=blogTemplate.objects.all()
	template_paginator = Paginator(us, 4)
	page_num = request.GET.get('page')
	page = template_paginator.get_page(page_num)

	return render(request,"main/template.html" ,{"page": page})

#search Module

def index11(request):
	cat=request.GET["cat"]
	blog=blogDetails.objects.filter(blogCatagories=cat)
	# articleid=articleDetail.objects.filter(articleAuthor=by)
	# return render(request=request,template_name="dashboard/userblogdetails.html")
	return render(request,"main/category.html" ,{"blog": blog})

def search(request):
    query=request.GET['s']
    if len(query)>78:
        blog=blogDetails.objects.none()
    else:
        allPostsTitle= blogDetails.objects.filter(blogTitle__icontains=query)
        allPostsAuthor= blogDetails.objects.filter(Q(blogAuthor__username__icontains=query) | Q(blogAuthor__first_name__icontains=query) | Q(blogAuthor__last_name__icontains=query))
        allPostsContent =blogDetails.objects.filter(blogCatagories__icontains=query)
        
        blog=  allPostsTitle.union(allPostsContent,allPostsAuthor)
    if blog.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'blog': blog ,'query':query}
    return render(request, 'main/search.html', params)

#Blog manangement Module

def blog_details(request):
	return render(request=request,template_name="dashboard/blogdetails.html")
	
def blog_add(request):

	
	blogtitle=request.POST["title"]
	image=request.FILES['profileImg']
	blogcat=request.POST["blogcatagory"]

	author=request.user
	temp=request.POST["template"]
	tempid=blogTemplate.objects.get(templatename=temp)
	data=blogDetails(blogTitle=blogtitle, blogProfile=image,blogCatagories=blogcat,blogAuthor=author,template=tempid)
	data.save()	
	
	subscriber=userSubscriber.objects.filter(subscribeTo=author)
	list=[]
	for email in subscriber:
		list.append(email.subscriber)
	if list:
		subject = 'Added new article'
		message = f'{request.user} has add new blog {blogtitle}'
		email_from = conf_settings.EMAIL_HOST_USER
		for i in range(len(list)): 
			recipient_list = [list[i] ]
		send_mail( subject, message, email_from, recipient_list )
	messages.info(request,'Blog Add Successfully..')
	return redirect('/myaccount')



def userblogdetail(request):
	by=request.user
	userblog=blogDetails.objects.filter(blogAuthor=by)
	# articleid=articleDetail.objects.filter(articleAuthor=by)
	# return render(request=request,template_name="dashboard/userblogdetails.html")
	return render(request,"dashboard/userblogdetails.html" ,{"userblog": userblog})


def edit_blog(request):
	blog_id=request.GET['id']
	blog=blogDetails.objects.get(id=blog_id)
	cat=categories.objects.all()

	return render(request,"dashboard/editblog.html" ,{"blog": blog,"cat":cat})

def update_blog(request):

	blog_id=request.POST["blogid"]
	blog=blogDetails.objects.get(id=blog_id)
	blog.blogTitle=request.POST["title"]
	blog.blogCatagories=request.POST["blogcatagory"]
	
	blog.save()
	return redirect("/userblogdetail")

#Article Management Module

def add_article(request):
	author=request.user
	blogid=blogDetails.objects.filter(blogAuthor=author)
	cat=categories.objects.all()
	return render(request,"dashboard/addarticle.html" ,{"blogid":blogid,"cat":cat})
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
	articleauthor=request.user
	articleblog=request.POST["articleblog"]
	blognameid=blogDetails.objects.get(id=articleblog)
	articles=articleDetail(articleName=articlename,article=articlecontent,articleCatagories=articlecatagory,articleImage=image,articleAuthor=articleauthor,blogAssociated=blognameid)
	articles.save()

	subscriber=userSubscriber.objects.filter(subscribeTo=articleauthor)
	list=[]
	for email in subscriber:
		list.append(email.subscriber)
	if list:
		subject = 'Added new article'
		message = f'{request.user} has add new article in blog {blognameid.blogTitle}'
		email_from = conf_settings.EMAIL_HOST_USER
		for i in range(len(list)): 
			recipient_list = [list[i] ]
		send_mail( subject, message, email_from, recipient_list )
	
	messages.info(request,'Article Add Successfully..')
	return redirect('/myaccount')

def edit_article(request):
	article_id=request.GET['articleId']
	aid=articleDetail.objects.get(id=article_id)
	cat=categories.objects.all()
	return render(request, 'dashboard/editarticle.html',{"aid": aid,"cat": cat})

def update_article(request):
	article_id=request.POST["id"]
	article=articleDetail.objects.get(id=article_id)
	article.articleName=request.POST["articlename"]
	article.article=request.POST["articlecontent"]
	article.articleCatagories=request.POST["articlecatagory"]
	if request.FILES:
		article.articleImage=request.FILES["articleimage"]
	article.save()
	return redirect("/myaccount")

def delete(request,id):
	ar=blogDetails.objects.get(pk=id)
	ar.delete()
	# return render(request,'dashboard/userblogdetails.html',{})
	return redirect("/userblogdetail")

def deleteArticle(request,id):
	ar=articleDetail.objects.get(pk=id)
	ar.delete()
	return redirect("/myaccount")


#User Module
#Register Here	
def getdata(request):
	
	if request.method=='POST':
		email=request.POST["email"]
		name=request.POST["name"]
		
		fname=request.POST["fname"]
		lname=request.POST["lname"]
		psw=request.POST["password"]
		# city=request.POST["city"]
		# phone=request.POST["phone"]
		if User.objects.filter(username=name).exists():
			messages.info(request,'username taken..')
			return redirect('/signup')
		else :
			user=User.objects.create_user(username=name,password=psw,email=email,first_name=fname,last_name=lname)
			user.save()
			# print('done')
			return redirect('/signin')
	else:
		return render(request, "main/signup.html",{}) 

#login Here
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

#logout
def handlelogout(request):
	logout(request)
	# messages.success(request, "successfully loggedout")
	return redirect('/home')
	return HttpResponse('handlelogout')

def index4(request):
	return render(request=request,template_name="main/signin.html")

def index5(request):
	return render(request=request,template_name="main/signup.html")

#report
def report(request):
	return render(request=request,template_name="main/report.html")

def report_details(request):
	if request.POST:
		report_value=request.POST["reportvalue"]
		optional=request.POST["Optional"]
		blogName=request.POST["blogName"]
			
		data=ReportedBlog(report=report_value,optional=optional,reportedBlog=blogName)
		data.save()
	return redirect("/home")
		