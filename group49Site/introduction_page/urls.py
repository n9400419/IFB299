from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from login import views_login
from accounts import views_accounts


urlpatterns = [
    url(r'^$', views.homePageView, name='Home'),
    url(r'^about/$', views.aboutPageView, name='About'),
    url(r'^login/$', views_login.loginPageView, name='Login'),
    url(r'^accounts/$', views_accounts.signup, name='Register'),
]

