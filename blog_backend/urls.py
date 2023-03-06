from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", views.blogPostOverview),
    path("blog/", views.BlogPostListView.as_view()),
    path("createblog/", views.BlogPostCreateBlog.as_view()),
    path("blog/<int:pk>/", views.BlogPostDetailedView.as_view()),
    path("updateblog/<int:pk>/", views.BlogPostUpdateView.as_view()),
    path("deleteblog/<int:pk>/", views.BlogPostDeleteView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
