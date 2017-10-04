from django.conf.urls import url
from . import views_accounts

urlpatterns = [

    url(r'^$', views_accounts.signup, name='Register'),
]