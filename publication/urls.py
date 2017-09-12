from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^([0-9]+)/$', views.detail, name='publication.detail'),
    url(r'^$', views.index, name='publication.index'),
]
