from django.conf.urls import patterns, include, url
from views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'transcription.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

	url(r'^home/$', home),
	url(r'^$', home),
	#url(r'^login/', login),
	# url(r'^logout/', logout),
	# url(r'^signup/',signup),
	# url(r'^legal/', legal),
	# url(r'^administration/',administration)),
)
