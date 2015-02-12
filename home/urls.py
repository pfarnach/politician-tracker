from django.conf.urls import patterns, url
from home import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
)