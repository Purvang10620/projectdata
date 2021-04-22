from django.contrib import admin
from .models import userProfile,dataForward,blogTemplate,blogDetails,articleDetail,userSociallink,comment,userSubscriber,categories,ReportedBlog

# Register your models here.
class ProfileDetails(admin.ModelAdmin):
	list_display = ['username','city','country','phone','profilepic']

class Contactus(admin.ModelAdmin):
	list_display = ['yourname','youremail','websitename','yourmessage']

class templatedetails(admin.ModelAdmin):
	list_display = ['templatename','templateimg']
	fieldsets = [
        ('Name', {'fields': ['templatename']}),
        ('Image', {'fields': ['templateimg']}),
        
    ]

class blogdetails(admin.ModelAdmin):
	list_display = ['blogTitle','blogCatagories','blogProfile','blogAuthor','template','blogDate']
	list_filter = ['blogDate','blogCatagories','blogAuthor']
	

class articledetails(admin.ModelAdmin):
	list_display = ['articleName','articleCatagories','articleImage','articleAuthor','blogAssociated','articleDate']
	list_filter = ['articleDate','articleCatagories','articleAuthor']

class commentsdetails(admin.ModelAdmin):
	list_display = ['commentBy','commentMsg','commentDate','commentOn']

class reportDetails(admin.ModelAdmin):
	list_display = ['report','reportedBlog']
	list_filter = ['reportedBlog']


admin.site.register(userProfile,ProfileDetails)
admin.site.register(dataForward , Contactus )
admin.site.register(blogTemplate , templatedetails )
admin.site.register(blogDetails , blogdetails)
admin.site.register(articleDetail , articledetails)
admin.site.register(userSociallink)
admin.site.register(comment , commentsdetails)
admin.site.register(userSubscriber)
admin.site.register(categories)
admin.site.register(ReportedBlog,reportDetails)

