from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('celebrity.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^play$', 'play', name='play'),
    url(r'^add$', 'add_celeb', name='add_celeb'),
    #url(r'^/static/css/bootstrap.css$', '')
    # url(r'^penvelopekravitz/', include('penvelopekravitz.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()