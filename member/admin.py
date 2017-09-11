from django.contrib import admin
from .models import ScholarshipFounder
from .models import ScholarshipType
from .models import Scholarship
from .models import Member
from .models import Institution
from .models import InstitutionDepartment
from .models import Degree
from .models import LineOfResearch


admin.site.register(ScholarshipFounder)
admin.site.register(ScholarshipType)
admin.site.register(Scholarship)
admin.site.register(Member)
admin.site.register(Institution)
admin.site.register(InstitutionDepartment)
admin.site.register(Degree)
admin.site.register(LineOfResearch)