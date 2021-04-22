"""projectdata URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from polls import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
app_name="main"

admin.site.site_header = " BlogBook Admin"
admin.site.site_title = "BlogBook Site Admin"



urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path("home",views.index,name="index"),
    path("about",views.index1,name="about"),
    path("category",views.index11,name="category"),
    path("contact",views.index2,name="contact"),
    path("createblog",views.index3,name="createblog"),
    path("signin",views.index4,name="signin"),
    path("login",views.login,name="login"),
    path("logout",views.handlelogout,name="logout"),
    path("signup",views.index5,name="signup"),
    path("solo",views.solo_templete,name="solo_templete"),
    # path("add_tag",views.add_tag,name="add_tag"),
    # path("tagDetails",views.tagDetails,name="tagDetails"),
    # path("tagResults",views.tagResults,name="tagResults"),
    
    path("add_subscriber",views.add_subscriber,name="add_subscriber"),

    path("single-audio",views.index6,name="single-audio"),
    path("single-gallery",views.index7,name="single-gallery"),
    path("single-standard",views.index8,name="single-standard"),
    path("single-video",views.index9,name="single-video"),  
    path("getdata",views.getdata),
    path("article_details",views.article_details,name="article_details"),
    path("userblogdetail",views.userblogdetail,name="userblogdetail"),
    path("userdashboard",views.dashboard,name="dashboard"),
    path("myaccount",views.useraccount,name="useraccount"),
    path("sociallink",views.sociallink,name="sociallink"),
    # path("main",views.main,name="main"),
    path("addarticle",views.add_article,name="addarticle"),
    path("profile",views.profile,name="profile"),
    path("editprofile",views.editprofile,name="editprofile"),
    path("updateprofile",views.updateprofile,name="updateprofile"),
    
    # path("profile_add",views.profile_add,name="profile_add"),
    path("settings",views.settings,name="settings"),
    path("sidebar",views.sidebar,name="sidebar"),
    path("template",views.templateImage,name="template"),
    path("report",views.report,name="report"),
    path("report_details",views.report_details,name="report_details"),

    path("blog_add",views.blog_add,name="blog_add"),
    path("blog_edit",views.edit_blog,name="blog_edit"),
    path("update_blog",views.update_blog,name="update_blog"),
    path("del/<int:id>",views.delete,name="delete"),

    path("viewarticle",views.viewarticle,name="viewarticle"),
    path("edit_article",views.edit_article,name="edit_article"),
    path("update_article",views.update_article,name="update_article"),
    path("delArticle/<int:id>",views.deleteArticle,name="deleteArticle"),

    path("contactInfoData",views.dataSend,name="contactInfoData"),
    path("search",views.search,name="search"),
    path("add_comment",views.add_comment,name="add_comment"),
    path("reset_password/",
        auth_views.PasswordResetView.as_view(template_name="main/forget-password.html"),
        name="reset_password"),

    path("reset_password_send/",
        auth_views.PasswordResetDoneView.as_view(template_name="main/password_reset_sent.html"),
        name="password_reset_done"),

    path("reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="main/resetpassword.html"),
        name="password_reset_confirm"),

    path("reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(template_name="main/password_reset_done.html"),
        name="password_reset_complete"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
