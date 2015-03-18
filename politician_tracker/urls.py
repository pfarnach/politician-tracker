from django.conf.urls import patterns, include, url
from django.http import HttpResponseRedirect
from django.contrib import admin
from django.conf import settings
from registration.backends.simple.views import RegistrationView
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/', TemplateView.as_view(template_name='moneyinfo.html')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^user/register/$', RegistrationView.as_view(), name='registration_register'),
    (r'^user/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )