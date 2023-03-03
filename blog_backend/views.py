from django.shortcuts import render
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.http import Http404


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

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = BlogPostSerializer(snippet)
        return Response(serializer.data)

    def get_serializer_class(self):
        return BlogPostSerializer
    