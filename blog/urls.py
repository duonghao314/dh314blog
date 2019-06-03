from django.contrib import admin
from django.urls import path, include
from blog import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('upload-comment', views.uploadCmnt),
    url(r'^cat/(?P<catName>[a-z]+)/$', views.cat),
    url(r'^art/(?P<url>[-\w]+)/(?P<id>[0-9])$', views.art),

]
