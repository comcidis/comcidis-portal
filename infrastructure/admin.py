from django.contrib import admin
from .models import Hardware
from .models import Node
from .models import Resource
from .models import Vendor
from .models import Infrastructure
from .models import InfrastructureNode
from .models import NodeHardware


admin.site.register(Hardware)
admin.site.register(Node)
admin.site.register(Resource)
admin.site.register(Vendor)
admin.site.register(Infrastructure)
admin.site.register(InfrastructureNode)
admin.site.register(NodeHardware)