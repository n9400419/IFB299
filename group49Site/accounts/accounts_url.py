

from django.conf.urls import url
from django.contrib.auth.views import login
from . import views
from login import views_login


urlpatterns = [
    url(r'^$', views.accounts_page, name='accounts_home'),

]

