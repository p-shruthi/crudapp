from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,DeleteView
from .models import Post 
from .forms  import PostForm
from django.urls import reverse_lazy
# Create your views here.

#def home(request):
 #   return render(request,'home.html',{})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'post_list.html'
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'
    #fields = '__all__'
class DeletePostView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')