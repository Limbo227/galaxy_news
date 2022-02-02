from django.urls import path
from .views import *


urlpatterns = [
    path('news/list/', NewsListView.as_view()),
    path('news/create/', NewsCreationView.as_view()),
    path('news/tags/', NewsTagsView.as_view()),
    path('news/category/', NewsCategoryView.as_view()),
    path('news/update/<int:pk>', NewsUpdateView.as_view()),
]