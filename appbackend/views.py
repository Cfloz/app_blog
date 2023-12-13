from django.shortcuts import render
from .models import Blog
from rest_framework import permissions
from rest_framework import viewsets
from .serializers import BlogSerializer


# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.AllowAny]