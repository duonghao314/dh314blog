import os
from uuid import uuid4
import time

from django.db import models
from django.contrib.auth.models import User
from Controller import Functions
from tinymce import HTMLField


# Create your models here.
class Category(models.Model):
    catName = models.CharField(max_length=20, null=False)
    catKeyWord = models.CharField(max_length=10, null=False)
    catViews = models.IntegerField(default=0)

    def __str__(self):
        return self.catName


class Article(models.Model):
    artName = models.CharField(max_length=200, null=False)
    artAuthor = models.ForeignKey(User, on_delete=models.CASCADE)
    artContent = HTMLField('Content')
    artViews = models.IntegerField(default=0)
    artDate = models.DateTimeField(auto_now=True)
    artCat = models.ForeignKey(Category, verbose_name='catName', on_delete=models.CASCADE)
    artImg = models.ImageField(upload_to=Functions.path_and_rename('upload/here/{}'.format(time.strftime("%Y/%m/%d"))))
    artUrl = models.CharField(max_length=255, null=False, default='null')

    def save(self, *args, **kwargs):
        if self.artUrl == 'null':
            self.artUrl = Functions.splitTitle(self.artName)
            super().save(*args, **kwargs)
        else:
            super().save(*args, **kwargs)


