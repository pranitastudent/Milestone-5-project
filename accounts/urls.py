from django.conf.urls import url, include
from accounts.views import logout, login, register, Contact,Feedback_new
from accounts import url_reset




urlpatterns = [
    url(r'^register/$', register, name='register'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^login/$', login, name='login'),
    url(r'^password-reset/', include(url_reset)),
    url(r'^contact/$', Contact, name='contact'),
    url(r'^feedback_new/$', Feedback_new, name='feedback_new'),
    
  

]