from django import forms
from django.forms import fields
from django.forms.fields import Field
from .models import Apply


class ApplayForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','cv','cover_letter','webSite']