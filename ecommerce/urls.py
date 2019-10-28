# Django Libraries

from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.views.static import serve
from django.contrib import admin
from .settings import MEDIA_ROOT
from accounts.views import index
from accounts import urls as accounts_urls


# Url Patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
  
    
]

admin.site.site_header = "Pranita's T-shirt Shop"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome"

