from django.db import models
from django.utils import timezone


class Degree(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Institution(models.Model):
    name = models.CharField(max_length=70)
    initials = models.CharField(max_length=10)
    position = models.ForeignKey(Degree)

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
    initials = models.CharField(max_length=10)
    founder = models.ForeignKey(ScholarshipFounder, on_delete=models.CASCADE)
    hours_schedule = models.IntegerField(default=40)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class ScholarshipType(models.Model):
    name = models.CharField(max_length=20)
    scholarship = models.ForeignKey(Scholarship)

    def __str__(self):
        return '{}-{}'.format(self.scholarship.initials, self.name)


class Member(models.Model):
    """Define a team member"""
    name = models.CharField(max_length=125)
    email = models.EmailField()
    birthday = models.DateField()
    lattes_link = models.CharField(max_length=150)
    degree = models.ForeignKey(Degree)
    scholarship = models.ForeignKey(ScholarshipType, on_delete=models.CASCADE)
    institution = models.ForeignKey(InstitutionDepartment, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('scholarship', 'name',)
