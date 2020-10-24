from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout as logout_user
#from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .form import  addLink , addSong
from .models import Link , Song, Singer

# Create your views here.
def index(req):
	return render(req, 'myweb/index.html')

def showsongs(req):
	return render(req, 'myweb/showsongs.html')

def addsongs(req):
	return render(req, 'myweb/addsongs.html')

def signup(request):
    context = {}
    form = UserCreationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('index')
    context['form']=form
    return render(request,'myweb/signup.html',context)

def logout(req):
    logout_user(req)
    return redirect('login')

def Rcmsongs(req):
	return render(req, 'myweb/Rcmsongs.html')

def jpsongs(req):
	return render(req, 'myweb/jpsongs.html')

def Intersongs(req):
	return render(req, 'myweb/Intersongs.html')

#########	#########	#########	#########	#########	#########

def showsongs(req):
    song = Song.objects.all()
    return render(req ,'myweb/showsongs.html' ,{'song':song})


def showsongs(req):
    song = Song.objects.all()
    return render(req ,'myweb/showsongs.html' ,{'song':song})


def addLink(req):
    if req.method == "POST":
        form = addLink(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addLink()
        context = {'form':form}
        return render(req, 'myweb/addsongs.html',context)

def addsongs(req):
    if req.method == "POST":
        form = addSong(req.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = addSong()
        context = {'form':form}
        return render(req, 'myweb/addsongs.html',context)