from django.contrib import admin
from .models import Conference
from .models import Publication

admin.site.register(Publication)
admin.site.register(Conference)
