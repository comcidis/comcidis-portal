from django.shortcuts import render
from .models import Member


def index(request):
    """List all members
    """
    advisors = Member.objects.filter(advisor=True)
    members = Member.objects.filter(advisor=False)
    context = {'advisors': advisors, 'members': members}
    return render(request, 'member/index.html', context)
