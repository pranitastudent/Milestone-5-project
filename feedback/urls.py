from django.contrib import admin
from django.conf.urls import url
from .views import (get_posts, add_post, edit_post, delete_post)

urlpatterns = [
    url(r'^$', get_posts, name="get_posts"),
    url(r'add_post/$', add_post, name="add_post"),
    url(r'^(?P<pk>\d+)/edit_post/$', edit_post, name= "edit_post"),
    url(r'^(?P<pk>\d+)/delete_post/$', edit_post, name= "delete_post"),
    
    ]