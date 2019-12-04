from django.conf.urls import url

# Imports from Custom Apps views
from . import views
urlpatterns = [
    url(r'^$', views.home_view, name='index'),
    url(r'^about/$', views.about_view, name='about'),
]
