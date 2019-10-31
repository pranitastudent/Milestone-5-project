# Django Libraries

from django.conf.urls import url, include
from django.views.generic import RedirectView
from django.views.static import serve
from django.contrib import admin
from .settings import MEDIA_ROOT
from accounts import urls as urls_accounts
from products import urls as urls_products
from products.views import all_products
from cart import urls as urls_cart
from django.views import static
from search import urls as urls_search
from checkout import urls as urls_checkout



# Url Patterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_products, name= "index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^media/(?P<path>.*)$', serve, {'document_root':MEDIA_ROOT}),
    url(r'^checkout/', include(urls_checkout)),
  
    
]

admin.site.site_header = "Pranita's T-shirt Shop"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome"

