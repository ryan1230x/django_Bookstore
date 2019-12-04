from django.conf.urls import url
from . import views # Import all the views

urlpatterns = [
    url(r'^$', views.fetch_all, name='all'),
    url(r'^search/$', views.search, name='search'),
    url(r'^(?P<type>[a-z A-Z -]+)/$',views.fetch_category, name='category'),
    url(r'^(?P<type>[a-z A-z -]+)/(?P<title>[a-z A-Z \']+)/$', views.fetch_single,name='single')
]
