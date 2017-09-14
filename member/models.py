from django.db import models
from django.utils import timezone


class Degree(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=70)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class InstitutionDepartment(models.Model):
    name = models.CharField(max_length=50)
    institution = models.ForeignKey(Institution)

    def __str__(self):
        return '{} ({})'.format(self.name, self.institution.initials)


class ScholarshipFounder(models.Model):
    name = models.CharField(max_length=70)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Scholarship(models.Model):
    name = models.CharField(max_length=70)
    initials = models.CharField(max_length=15)
    institution = models.ForeignKey(Institution)
    founder = models.ForeignKey(ScholarshipFounder, on_delete=models.CASCADE)
    hours_schedule = models.IntegerField(default=40)

    def __str__(self):
        return '{} ({}/{})'.format(self.name, self.institution.initials,
                                   self.founder.initials)

    class Meta:
        ordering = ('name',)


class ScholarshipType(models.Model):
    name = models.CharField(max_length=20)
    scholarship = models.ForeignKey(Scholarship)

    def __str__(self):
        return '{}-{} ({})'.format(self.scholarship.initials,
                                   self.name,
                                   self.scholarship.institution.initials)


class LineOfResearch(models.Model):
    name = models.CharField(max_length=125)
    
    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name',)


class Member(models.Model):
    """Define a team member"""
    name = models.CharField(max_length=125)
    advisor = models.BooleanField(default=False)
    email = models.EmailField()
    birthday = models.DateField()
    lattes_link = models.CharField(max_length=150)
    degree = models.ForeignKey(Degree)
    scholarship = models.ForeignKey(ScholarshipType, on_delete=models.CASCADE)
    institution = models.ForeignKey(InstitutionDepartment, on_delete=models.CASCADE)
    line_of_research = models.ForeignKey(LineOfResearch)
    citation_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


    class Meta:
        ordering = ('name', 'scholarship',)
