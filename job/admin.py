from django.contrib import admin

# Register your models here.
from .models import Category, Work, Apply
admin.site.register(Work)
admin.site.register(Category)
admin.site.register(Apply)