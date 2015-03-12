from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.politician_index, name='politician_index'),
	url(r'^search_list/$', views.search_list, name="search_list"),
	url(r'^subscribe_to_pol/$', views.subscribe_to_pol, name="subscribe_to_pol"),
	url(r'^view_subscriptions/$', views.view_subscriptions, name="view_subscriptions"),
	url(r'(?P<politician_name_slug>[\w\-]+)/$', views.politician_profile, name='politician_profile'),
)