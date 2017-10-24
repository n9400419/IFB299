from django.conf.urls import url
from . import views_accounts

urlpatterns = [

    url(r'^$', views_accounts.signup, name='Register'),
    url(r'^profile/$', views_accounts.profile_view, name='Profile'),
    url(r'^hotel/$', views_accounts.hotel_view, name='ViewHotel'),
    url(r'^library/$', views_accounts.library_view, name='ViewLibrary'),
    url(r'^college/$', views_accounts.college_view, name='ViewCollege'),
    url(r'^industry/$', views_accounts.industry_view, name='ViewIndustry'),
]