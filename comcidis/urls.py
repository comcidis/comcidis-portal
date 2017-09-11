from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^members/', include('member.urls'), name='member'),
    url(r'^publications/', include('publication.urls'), name='publication'),
    url(r'^infrastructure/', include('infrastructure.urls'), name='infrastructure'),
    url(r'^', include('home.urls'), name='home'),
]
