from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views import View
from .models import blog
from calc.form import ResourceForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse
from django.db.models import F
def home(request):
    blogs=blog.objects.all().order_by('-count')
    return render(request,'blog.html',{'blogs': blogs})
def addresources(request):
    if request.method=="POST":
        form=ResourceForm(request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
        return redirect('home')
    else:
        form=ResourceForm()
        return render(request, 'addresources.html')
def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'An account already exists with thsi E-mail id')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print("user created")
                return redirect('home')
        else:
            messages.info(request, 'Passwords are not matching')
            return redirect('register')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=="POST":
         username=request.POST['username']
         password=request.POST['password']
         user=auth.authenticate(username=username,password=password)
         if user is not None:
             auth.login(request, user)
             return redirect('home')
         else:
             messages.info(request,'invalid password or username')
             return redirect('login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('home')
def like(request, pk):
    if request.user.is_authenticated:
        upbl = get_object_or_404(blog,id=pk)
        if upbl.upchek is False:
           blog.objects.filter(id=pk).update(count=F('count') + 1)
           blog.objects.filter(id=pk).update(upchek=True)
           blog.objects.filter(id=pk).update(downchek=False)
           return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('login')

def dislike(request, pk):
    if request.user.is_authenticated:
        dwbl = get_object_or_404(blog,id=pk)
        if dwbl.downchek is False:
            blog.objects.filter(id=pk).update(count=F('count') - 1)
            blog.objects.filter(id=pk).update(downchek=True)
            blog.objects.filter(id=pk).update(upchek=False)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return redirect('login')

    
