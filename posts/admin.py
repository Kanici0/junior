from sys import modules

from django.contrib import admin

from posts import models
from posts.models import  Post
admin.site.register(Post)
admin.site.register(models.Category)
admin.site.register(models.Tag)





# Register your models here.
