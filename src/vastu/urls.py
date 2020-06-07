#Basic settings for static files
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include

from properties.views import index,about,contact,properties,property_detail,search

urlpatterns = [
    path('vre-admin/', admin.site.urls),
    path('',index),
    path('home/about/',about),
    path('home/contact/',contact, name='contact'),
    path('home/properties/',properties, name='property_list'),
    path('home/search/',search, name='search'),
    path('home/properties/<id>/',property_detail,name='property_detail'),


]

#Basic settings
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)