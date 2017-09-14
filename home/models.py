from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=100)
    short_description = models.CharField(max_length=175)
    description = models.TextField()
    
    def __str__(self):
        return self.title