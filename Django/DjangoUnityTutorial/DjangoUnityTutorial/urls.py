"""
Definition of urls for DjangoUnityTutorial.
"""

from datetime import datetime
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    # Examples:
    #url(r'^$', 'app.views.home', name='home'),
    path('api/', include('unitybackendapp.urls', namespace='api')),

    # path('api/', include(router.urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
]
