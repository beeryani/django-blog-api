from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)

    def get_serializer_class(self):
        return BlogPostSerializer


class BlogPostDetailedView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)

    def get_serializer_class(self):
        return BlogPostSerializer
