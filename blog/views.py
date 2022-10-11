from pdb import post_mortem
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"
