from django.conf.urls import patterns, url
from profiles import views

urlpatterns = patterns('',
	url(r'^$', views.politician_index, name='politician_index'),
	url(r'^search_list/$', views.search_list, name="search_list"),
	url(r'^subscribe_to_pol/$', views.subscribe_to_pol, name="subscribe_to_pol"),
	url(r'^get_money_info/$', views.get_money_info, name="get_money_info"),
	url(r'^get_articles/$', views.get_articles, name="get_articles"),
	url(r'^post_article/$', views.post_article, name="post_article"),
	url(r'^article_vote/$', views.article_vote, name="article_vote"),
	url(r'^view_subscriptions/$', views.view_subscriptions, name="view_subscriptions"),
	url(r'(?P<politician_name_slug>[\w\-]+)/$', views.politician_profile, name='politician_profile'),
)