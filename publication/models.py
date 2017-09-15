from django.db import models
from django.template.defaultfilters import slugify
from member.models import Member


class Conference(models.Model):
    name = models.CharField(max_length=125)
    initials = models.CharField(max_length=10)

    def __str__(self):
        return self.initials


    class Meta:
        ordering = ('name',)


class Publication(models.Model):
    pub_authors = models.ManyToManyField(Member, through='AuthorsOrder')
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, blank=True)
    abstract = models.TextField()
    resume = models.TextField(blank=True)
    date = models.DateField()
    link = models.CharField(max_length=150, blank=True)
    conference = models.ForeignKey(Conference)
    bibtex = models.TextField(blank=True)

    def authors_list(self):
        """Get an ordered authors list"""
        return [author_order.author 
                    for author_order in AuthorsOrder.objects.filter(
                        publication=self).order_by('order')]

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Publication, self).save(*args, **kwargs)

    def __str__(self):
        return '{} ({} {})'.format(self.title, self.conference.initials,
                                   self.date.year)


    class Meta:
        ordering = ('-date','title',)


class AuthorsOrder(models.Model):
    order = models.PositiveSmallIntegerField(default=0)
    publication = models.ForeignKey(Publication)
    author = models.ForeignKey(Member)

    def __str__(self):
        return '{} - {}'.format(self.publication.title,
                                self.author.citation_name)
    
    
    class Meta:
        ordering = ('order',)