from django.contrib import admin
from .models import ScholarshipFounder
from .models import ScholarshipType
from .models import Scholarship
from .models import Member
from .models import Institution
from .models import InstitutionDepartment
from .models import Degree


admin.site.register(ScholarshipFounder)
admin.site.register(ScholarshipType)
admin.site.register(Scholarship)
admin.site.register(Member)
admin.site.register(Institution)
admin.site.register(InstitutionDepartment)
admin.site.register(Degree)
