from rest_framework import serializers
from .models import *


class NewsListSerializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NewsSerializers(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = '__all__'


class NewsTagsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'


class NewsCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

