from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'home'}, name='logout'),

    url(r'^registration/', include('registration.urls')),

    url(r'^openid/', include('oidc_provider.urls', namespace='oidc_provider')),

    url(r'^admin/', include(admin.site.urls)),
]
