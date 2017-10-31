from django.conf.urls import url
from . import views_accounts

urlpatterns = [

    url(r'^$', views_accounts.signup, name='Register'),
    url(r'^profile/$', views_accounts.profile_view, name='Profile'),
    url(r'^hotel/$', views_accounts.hotel_view, name='ViewHotel'),
    url(r'^library/$', views_accounts.library_view, name='ViewLibrary'),
    url(r'^college/$', views_accounts.college_view, name='ViewCollege'),
    url(r'^industry/$', views_accounts.industry_view, name='ViewIndustry'),
    url(r'^citymap/$', views_accounts.citymap_view, name='ViewCityMap'),
    url(r'^cityinformation/$', views_accounts.cityinformation_view, name='ViewCityInformation'),
    url(r'^zoos/$', views_accounts.zoos_view, name='ViewZoos'),
    url(r'^malls/$', views_accounts.malls_view, name='ViewMalls'),
    url(r'^museums/$', views_accounts.museums_view, name='ViewMuseums'),
    url(r'^restaurants/$', views_accounts.restaurants_view, name='ViewRestaurants'),
    url(r'^parks/$', views_accounts.parks_view, name='ViewParks'),
]
