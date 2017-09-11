from django.db import models


class Vendor(models.Model):
    name = models.CharField(max_length=75)
    
    def __str__(self):
        return self.name


class Resource(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Hardware(models.Model):
    resource = models.ForeignKey(Resource)
    number = models.PositiveSmallIntegerField()
    mhz = models.PositiveSmallIntegerField()
    vendor = models.ForeignKey(Vendor)
    family = models.CharField(max_length=75)
    GB = 'GB'
    TB = 'TB'
    CORES = 'CO'
    BPS = 'BP'
    UNIT_CHOICES = (
        (GB, 'GB'),
        (TB, 'TB'),
        (CORES, 'Cores'),
        (BPS, 'bps'),
    )
    unit = models.CharField(max_length=2, choices=UNIT_CHOICES, default=CORES)
    
    def __str__(self):
        return '{}: {} {} @ {}'.format(self.resource.name, self.vendor,
                                       self.family, self.mhz)
        
    
    class Meta:
        ordering = ('vendor', 'family', 'mhz')


class Node(models.Model):
    reference = models.CharField(max_length=75)
    size = models.PositiveIntegerField(default=1)
    hardware = models.ManyToManyField(Hardware, through='NodeHardware')
    vendor = models.ForeignKey(Vendor)

    def specs(self):
        resources = {}
        for node_hw in self.nodehardware_set.all():
            hw = node_hw.hardware
            resource = resources.get(hw.resource.name, {'label': hw.get_unit_display()})
            resource['total'] = resource.get('total', 0) + (hw.number * node_hw.amount)
            resources[hw.resource.name] = resource
        return resources

    def __str__(self):
        return '{}-{} ({}U)'.format(self.vendor.name, self.reference, self.size)


class NodeHardware(models.Model):
    amount = models.PositiveSmallIntegerField(default=1)
    hardware = models.ForeignKey(Hardware)
    node = models.ForeignKey(Node)

    def __str__(self):
        return '{}: {}x {}'.format(self.node, self.amount, self.hardware)


class Infrastructure(models.Model):
    name = models.CharField(max_length=75)
    short_description = models.CharField(max_length=125)
    description = models.TextField()
    nodes = models.ManyToManyField(Node, through='InfrastructureNode')

    def overview(self):
        resources = {}
        infrastructure_nodes = self.infrastructurenode_set.all()
        for node in infrastructure_nodes:
            node_specs = node.node.specs()
            for resource_name, resource in node_specs.items():
                resource['total'] *= node.amount
                if resources.get(resource_name, None):
                    resources[resource_name]['total'] += resource['total']
                else:
                    resources[resource_name] = resource
        return resources

    def __str__(self):
        return self.name
    
    
    class Meta:
        ordering = ('name',)


class InfrastructureNode(models.Model):
    amount = models.PositiveIntegerField(default=1)
    node = models.ForeignKey(Node)
    infrastructure = models.ForeignKey(Infrastructure)
    
    def __str__(self):
        return '{}x {} ({})'.format(self.amount, self.node, self.infrastructure.name)