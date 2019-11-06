from django.conf.urls import url, include
from accounts.views import index, logout, login, register, Contact, profile
from accounts import url_reset

urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^profile/$', profile, name='profile'),
    
  ]