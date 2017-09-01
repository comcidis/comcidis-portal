from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('home.urls'), name='home'),
    url(r'^members', include('member.urls'), name='member'),
]