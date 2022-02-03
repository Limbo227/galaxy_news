from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import *
from .permissions import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# Create your views here.


class NewsListView(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsListSerializers

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]
    filter_fields = ['title']
    search_fields = ['title', 'description']
    ordering_fields = ['title', 'created']


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


