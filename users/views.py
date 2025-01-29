from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from datetime import datetime
from django.template.context_processors import request
from unicodedata import category
from django.db import connection
from .models import *
from .forms import LoginForm


def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')

# def register(request):
#     return render(request,'users/register.html')
def register(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        address=request.POST.get('address')
        pincode=request.POST.get('pincode')
        city=request.POST.get('city')
        mobile=request.POST.get('mobile')
        picture=request.FILES['fu']
        x=tbl_register.objects.all().filter(email=email).count()
        if x==1:
            return HttpResponse("<script>alert('you are already registered');location.href='/register/'</script>")

        else :
            tbl_register(name=name,email=email,password=passwd,address=address,Pincode=pincode,city=city,mobile=mobile,picture=picture).save()
            return HttpResponse("<script>alert('Thanks for register with us....');location.href='/register/'</script>")
    return render(request,'users/register.html')

