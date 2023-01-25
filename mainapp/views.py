from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post

class HomeView(ListView):
    model=Post
    template_name="mainapp_pages/index.html"
    context_object_name="posts"
    
