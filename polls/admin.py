from django.contrib import admin
from .models import Profile,dataForward,blogTemplate

# Register your models here.

admin.site.register(Profile)
admin.site.register(dataForward)
admin.site.register(blogTemplate)