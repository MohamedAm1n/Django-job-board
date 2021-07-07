from django import forms
from django.forms import fields
from django.forms.fields import Field
from .models import Apply , Work


class ApplayForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','cv','cover_letter','webSite']

class JobForm(forms.ModelForm):
    class Meta:
        model=Work
        fields='__all__'
        #  if you want to select all fields in model without one of them,
        # use exclude and type the parameter 
        exclude=('slug','owner')