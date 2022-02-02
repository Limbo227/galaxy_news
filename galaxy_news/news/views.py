from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.

class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializers
    queryset = News.objects.all()


class NewsCreationView(generics.CreateAPIView):
    serializer_class = NewsSerializers
    permission_classes = (IsAdminUser, IsAuthenticated,)


class NewsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsSerializers
    queryset = News.objects.all()
    permission_classes = (OwnerOrReadOnly, IsAuthenticated, )


class NewsTagsView(generics.CreateAPIView):
    serializer_class = NewsTagsSerializers
    permission_classes = (IsAdminUser, IsAuthenticated, )


class NewsCategoryView(generics.CreateAPIView):
    serializer_class = NewsCategorySerializers
    permission_classes = (IsAdminUser, IsAuthenticated, )


