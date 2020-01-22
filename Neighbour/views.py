from django.shortcuts import render,redirect
from Neighbour.forms import UserForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Post,Neighbourhood,Business
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# def home(request):
#     posts=Post.objects.all()   
    
#     return render(request,'Neighbour/index.html',{"posts":posts})

class PostListView(ListView):
    model = Post
    template_name = 'Neighbour/index.html'
    context_object_name = 'posts'
    ordering =['-date_posted']

class NeighbourhoodListView(ListView):
    model = Neighbourhood
    template_name =  'Neighbour/neiba.html'
    context_object_name = 'neibas'

class BusinessListView(ListView):
    model = Business
    template_name =  'Neighbour/business.html'
    context_object_name = 'business'


class PostDetailView(DetailView):
    model = Post
class NeighbourhoodDetailView(DetailView):
    model = Neighbourhood
class BusinessDetailView(DetailView):
    model = Business
    
class PostCreateView( LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content','image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class NeighbourhoodCreateView(LoginRequiredMixin,CreateView):
    model = Neighbourhood
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BusinessCreateView(LoginRequiredMixin,CreateView):
    model = Business
    fields = '__all__'

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

class NeighbourhoodUpdateView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Neighbourhood
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user: 
            return True
        return False

class BusinessUpdateView( LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Business
    fields = '__all__'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user: 
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

class NeighbourhoodDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Neighbourhood
    success_url = reverse_lazy('')
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False

class BusinessDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Business
    success_url = reverse_lazy('')
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user: 
            return True
        return False


def search_results(request):

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        searched_articles = Post.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'Neighbour/search.html',{"message":message,"projects": searched_articles})

    else:
        message = "You haven't searched for any term"
        return render(request, 'Neighbour/search.html',{"message":message}) 
