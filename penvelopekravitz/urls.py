from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from celebrity.models import Celebrity
from rest_framework import routers, serializers, viewsets

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

class CelebSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Celebrity
        fields = ('name',)

class CelebViewSet(viewsets.ModelViewSet):
    queryset = Celebrity.objects.all()
    serializer_class = CelebSerializer

router = routers.DefaultRouter()
router.register(r'celebs', CelebViewSet)

urlpatterns = patterns('celebrity.views',
    
    url(r'^$', 'home', name='home'),
    url(r'^play$', 'play', name='play'),
    url(r'^add$', 'add_celeb', name='add_celeb'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns += staticfiles_urlpatterns()