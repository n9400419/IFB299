from django.conf.urls import url
from . import views_login
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^login/$', views_login.loginPageView, name='Login'),
    url(r'^register/$', views_login.registerPageView, name='Register'),
    url(r'^success/$', views_login.registration_complete, name='Register'),
]

