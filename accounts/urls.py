from django.conf.urls import url, include
from accounts.views import logout, login, register, Contact, get_posts, post_detail, create_or_edit_post, post_update,post_delete
from accounts import url_reset




urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/$', post_update, name='post_update'),
    url(r'^(?P<pk>\d+)/$', post_delete, name='post_delete'),
    
    
]