from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'caipirinha.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),
    url(r'^admin/', include(admin.site.urls)),
]
