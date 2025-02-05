from django.shortcuts import render
from rest_framework import generics
from .filters import PostModelViewSet
from .pagination import MyCategoryPagination, MyPostNumberPagination
from .serializers import CategorySerializer, PostSerializer
from .models import Category, Post


# Create your views here.


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = MyCategoryPagination


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = MyPostNumberPagination
    filter_class = PostModelViewSet
