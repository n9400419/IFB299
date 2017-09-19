from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from login import views_login


urlpatterns = [
    url(r'^$', views.homePageView, name='Home'),
    url(r'^about/$', views.aboutPageView, name='About'),
    url(r'^login/$', views_login.loginPageView, name='Login'),
    url(r'^register/$', views_login.registerPageView, name='Register'),
]

