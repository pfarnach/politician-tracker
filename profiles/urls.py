from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search_list/$', views.search_list, name="search_list"),
	url(r'(?P<politician_name_slug>[\w\-]+)/$', views.politician_profile, name='politician_profile'),
)