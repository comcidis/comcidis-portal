from django.db import models
from member.models import Member


class Conference(models.Model):
    name = models.CharField(max_length=125)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.initials


    class Meta:
        ordering = ('name',)


class Publication(models.Model):
    authors = models.ManyToManyField(Member)
    title = models.CharField(max_length=150)
    abstract = models.TextField()
    resume = models.TextField()
    date = models.DateField()
    link = models.CharField(max_length=150, blank=True)
    conference = models.ForeignKey(Conference)

    def __str__(self):
        return '{} - {}'.format(self.title, self.authors.all()[0].name)


    class Meta:
        ordering = ('date','title')
