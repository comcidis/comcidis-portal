from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Publication


def index(request):
    publication_list = Publication.objects.all()
    paginator = Paginator(publication_list, 10)
    page = request.GET.get('page')
    
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)
        
    context = {'mobile_title_page': 'Produções',
               'publications': publications}
    
    return render(request, 'publication/index.html', context)

def detail(request, publication_id):
    publication = Publication.objects.get(id=publication_id)
    conference = '{} {}'.format(publication.conference, publication.date.year)
    context = {'mobile_title_page': conference,
               'publication': publication}
    return render(request, 'publication/detail.html', context)