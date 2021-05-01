from django.contrib import admin

# Register your models here.

#Register profile Model to Admin panel, New Profiles can be added from admin panel if registered in admin
from .models import Profile
admin.site.register(Profile)