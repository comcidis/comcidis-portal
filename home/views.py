from django.shortcuts import render
from publication.models import Publication

def index(request):
    recent_publications = Publication.objects.all()[:4]
    context = {'recent_publications': recent_publications}
    return render(request, 'home/index.html', context)
