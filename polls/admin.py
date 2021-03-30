from django.contrib import admin
from .models import Profile,dataForward,blogTemplate,blogDetails,articleDetail,userSociallink,comment,userSubscriber

# Register your models here.
class Contactus(admin.ModelAdmin):
	list_display = ['yourname','youremail','websitename','yourmessage']

class templatedetails(admin.ModelAdmin):
	list_display = ['templatename','templateimg']

class blogdetails(admin.ModelAdmin):
	list_display = ['blogName','blogTitle','blogCatagories','blogAuthor','template','blogDate']

class articledetails(admin.ModelAdmin):
	list_display = ['articleName','article','articleCatagories','articleImage','articleKeyword','articleAuthor','blogAssociated','articleDate']

admin.site.register(Profile)
admin.site.register(dataForward , Contactus )
admin.site.register(blogTemplate , templatedetails )
admin.site.register(blogDetails , blogdetails)
admin.site.register(articleDetail , articledetails)
admin.site.register(userSociallink)
admin.site.register(comment)
admin.site.register(userSubscriber)

