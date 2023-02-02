from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Post

class HomeView(ListView):
    model=Post
    # template_name="mainapp_pages/index.html"
    context_object_name="posts"
    paginate_by=2

    def get_template_names(self):
        print("kasndkjn")
        if self.request.htmx:
            print("htmx is calling u")

        return "mainapp_pages/index.html"

            

    
