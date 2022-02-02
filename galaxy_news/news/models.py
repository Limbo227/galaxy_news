from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


class News(models.Model):
    User = get_user_model()
    title = models.CharField('title', max_length=50)
    description = models.CharField('description', max_length=299)
    author = models.ForeignKey(User, verbose_name='author', on_delete=models.PROTECT)
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        verbose_name='image',
        blank=True)
    phone_number = models.CharField('phone_number', max_length=100)
    tags = models.ForeignKey('Tags', verbose_name='tags', on_delete=models.CASCADE)
    category = models.ForeignKey('Categories', verbose_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Tags(models.Model):
    title = models.CharField('title', max_length=20)

    def __str__(self):
        return self.title

class Categories(models.Model):
    title = models.CharField('title', max_length=20)

    def __str__(self):
        return self.title