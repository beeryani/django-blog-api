from django.shortcuts import render
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .models import BlogPost
from .serializers import BlogPostSerializer
from django.http import Http404


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def blogPostOverview(request):
    api_overview = {
        "Take a look at 5 recent blogs": "blog/",
        "Detailed view of a Blog": "blog/<int:pk>/",
        "Create a Blog": "createblog/",
        "Update a Blog": "updateblog/<int:pk>/",
        "Delete a Blog": "deleteblog/<int:pk>/",
    }

    return Response(api_overview)


class BlogPostListView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        return self.list(request)

    def get_serializer_class(self):
        return BlogPostSerializer


class BlogPostCreateBlog(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
        queryset = self.get_object(pk)
        serializer = BlogPostSerializer(queryset)
        return Response(serializer.data)

    def get_serializer_class(self):
        return BlogPostSerializer


class BlogPostUpdateView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = BlogPostSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = BlogPostSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        return BlogPostSerializer


class BlogPostDeleteView(RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk, format=None):
        queryset = self.get_object(pk)
        serializer = BlogPostSerializer(queryset)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            return BlogPost.objects.get(pk=pk)
        except BlogPost.DoesNotExist:
            raise Http404

    def delete(self, request, pk, format=None):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def get_serializer_class(self):
        return BlogPostSerializer
