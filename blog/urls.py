from django.urls import path
from . import views

app_name = "blog_app"
urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("<int:pk>/", views.BlogDetailView.as_view(), name="blog"),
]
