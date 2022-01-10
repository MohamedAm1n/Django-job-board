from django import http
from django.contrib.auth import authenticate , login
from django.shortcuts import redirect, render
from django.http import HttpResponse

from accounts.models import Profile
from .forms import SignupForm
# Create your views here.

def SignUp(request):
    if request.method=="POST":
        form =SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user= authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form =SignupForm()
    return render(request,'registration/sign_up.html',{'form':form})



def profile(request):
    profile=Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile':profile})