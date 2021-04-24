from django.contrib import admin
from auth_.models import MainUser, Profile

# Register your models here.
admin.site.register(MainUser)
admin.site.register(Profile)
