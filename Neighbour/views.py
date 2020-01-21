from django.shortcuts import render,redirect
from Neighbour.forms import UserForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post,Neighbourhood,
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
def home(request):
    posts=Post.objects.all()   
    
    return render(request,'Neighbour/index.html',{"posts":posts})

class PostListView(ListView):
    model = Post
    template_name = 'Neighbour/index.html'
    context_object_name = 'posts'
    ordering =['-date_posted']

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView( LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url ='/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False