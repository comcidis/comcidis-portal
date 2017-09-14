from django.shortcuts import render
from publication.models import Publication
from member.models import LineOfResearch
from .models import Section

def index(request):
    recent_publications = Publication.objects.all()[:4]
    sections = Section.objects.all()
    lines_of_research = LineOfResearch.objects.all()
    half_of_list_length = round(len(lines_of_research) / 2)
    research_columns = [lines_of_research[:half_of_list_length],
                        lines_of_research[half_of_list_length:]]
    context = {'recent_publications': recent_publications,
               'sections': sections, 'research_columns': research_columns}
    return render(request, 'home/index.html', context)
