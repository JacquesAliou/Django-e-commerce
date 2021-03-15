from django.contrib import admin
from .models import Profile

# Be able to view user profile in admin panel
admin.site.register(Profile)

