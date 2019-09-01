from django.conf.urls import url, include
from accounts.views import logout, login, register, feedback
from accounts import url_reset


urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^feedback/$', feedback, name='feedback'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
]