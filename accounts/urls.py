from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_feedback
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^registration/', registration, name="register"),
    url(r'^feedback/', user_feedback, name="user_feedback"),
    url(r'^password-reset/', include(url_reset))
]