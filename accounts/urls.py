from django.conf.urls import url, include
from accounts.views import index, logout, login, register, Contact, get_posts, post_detail, edit_post, create_post, delete_post
from accounts import url_reset





urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_post, name='edit_post'),
    url(r'^(?P<pk>\d+)/delete/$', delete_post, name='delete_post')
  ]