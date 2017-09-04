from django.contrib import admin
from .models import Conference
from .models import Publication
from .models import AuthorsOrder

admin.site.register(Publication)
admin.site.register(Conference)
admin.site.register(AuthorsOrder)
