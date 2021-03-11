from django.contrib import admin
from .models import Profile,dataForward,blogTemplate,blogDetails,articleDetail

# Register your models here.
class Contactus(admin.ModelAdmin):
	list_display = ['yourname','youremail','websitename','yourmessage']

class templatedetails(admin.ModelAdmin):
	list_display = ['templatename','templateimg']

admin.site.register(Profile)
admin.site.register(dataForward , Contactus )
admin.site.register(blogTemplate , templatedetails )
admin.site.register(blogDetails)
admin.site.register(articleDetail)
