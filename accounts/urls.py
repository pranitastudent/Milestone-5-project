from django.conf.urls import url, include
from accounts.views import logout, login, register, feedback, feedback_detail, create_or_edit_feedback
from accounts import url_reset


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'feedback/$', feedback, name='feedback'),
    url(r'^(?P<pk>\d+)/$', feedback_detail, name='feedback_detail'),
    url(r'^new/$', create_or_edit_feedback, name='new_feedback'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_feedback, name='edit_feedback'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]