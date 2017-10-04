

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views_accounts
from login import views_login


urlpatterns = [
    url(r'^$', views_accounts.signup, name='accounts_home'),

]

