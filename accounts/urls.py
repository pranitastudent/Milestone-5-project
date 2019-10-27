from django.conf.urls import url, include
from accounts.views import logout, login, register, Contact, Feedback, Feedback_detail,create_or_edit_post
from accounts import url_reset




urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^feedback/$', Feedback, name='post'),
    url(r'^(?P<pk>\d+)/$',Feedback_detail, name='Feedback_detail'),
    url(r'^new/$', create_or_edit_post, name= 'new_post'),
    url(r'^(?P<pk>\d+)/$',create_or_edit_post, name='edit_post'),
    
    
    
]