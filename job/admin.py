from django.contrib import admin

# Register your models here.
from .models import Category, Work
admin.site.register(Work)
admin.site.register(Category)