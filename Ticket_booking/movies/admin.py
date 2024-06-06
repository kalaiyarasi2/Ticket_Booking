from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Movies_details,MovieIDChoices

admin.site.register(Movies_details)
