from django.views.generic import ListView, DetailView, CreateView
from .models import Post


class HomeView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"

class AddBlogDetailView(CreateView):
    model = Post
    template_name = "add_blog.html"
    fields = "__all__"
