from django.conf.urls import url, include
from accounts.views import logout, login, register, user_feedback
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^feedback/', user_feedback, name="feedback"),
    url(r'^password-reset/', include(url_reset))
]