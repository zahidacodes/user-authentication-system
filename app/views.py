from django.shortcuts import render,HttpResponseRedirect
from .forms import myform,myuserform,myadminform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def display(request):
    if request.method == "POST":
        fm = myform(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/user/')
            
    else:
        fm = myform()
        
    return render(request,"index.html",{"fm":fm})



def show(request):
    if request.method == "POST":
        fm = AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data["username"]
            upass = fm.cleaned_data["password"]
            um =authenticate(username=uname,password=upass)
            if um is not None:
                login(request,um)
                um.save()
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm(request=request)
    return render(request,"user.html",{"fm":fm})


def userdata(request):
    if request.method == "POST":
        if request.user.is_superuser == True:
            fm = myadminform(request.POST, instance = request.user)
            users = User.objects.all()
        else:
            fm = myuserform(request.POST, instance = request.user)
            users = None
            if fm.is_valid():
                fm.save()
    else:
        if request.user.is_superuser == True:
            fm = myadminform(instance = request.user)
            users = User.objects.all()
            
        else:
            fm = myuserform(instance = request.user)
            users = None
    return render(request,"profile.html",{"fm":fm, "name":request.user.username ,"users":users})

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/user/')