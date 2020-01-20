from django.shortcuts import render,redirect
from Neighbour.forms import UserForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post

def home(request):
    posts=Post.objects.all()   
    
    return render(request,'Neighbour/index.html',{"posts":posts})

