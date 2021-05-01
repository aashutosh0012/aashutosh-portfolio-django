from django.contrib import admin

# Register your models here.
#Display Post Model in admin panel, Register Post class to admin
from .models import Post
admin.site.register(Post)
