from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from .forms import PostForm


class HomeView(ListView):
    model = Post
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog_detail.html"


class AddBlogDetailView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_blog.html"
