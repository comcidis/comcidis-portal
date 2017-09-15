from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.detail, name='publication.detail'),
    url(r'^$', views.index, name='publication.index'),
]
