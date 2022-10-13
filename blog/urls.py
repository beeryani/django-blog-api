from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/blog/", views.BlogDetailView.as_view(), name="blog"),
    path("add_blog/", views.AddBlogDetailView.as_view(), name="add_blog"),
]
