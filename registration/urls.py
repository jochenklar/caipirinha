from django.conf.urls import include, url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # password change
    url(r'^password-change/$', auth_views.password_change, name='password_change'),
    url(r'^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    # password reset
    url(r'^password-reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password-reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^password-reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^password-reset/complete/$', auth_views.password_reset_complete, name='password_reset_complete'),
]

# {'template_name': 'auth/password_reset.html', 'email_template_name': 'auth/password_reset_email.html', 'subject_template_name': 'auth/password_reset_subject.txt'} {'template_name': 'auth/password_reset_confirm.html'} {'template_name': 'auth/password_reset_complete.html'}